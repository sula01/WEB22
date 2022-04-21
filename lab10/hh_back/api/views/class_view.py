from django.shortcuts import Http404
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated

from api.serializers import Company2Serializer, CompanySerializer, Vacancy2Serializer, CompanyVacancySerializer
from api.models import Company,Vacancy

class CompanyListAPIView(APIView):
    def get(self, request):
        companies = Company.objects.all()
        serializer = CompanySerializer(companies, many=True)
        permission_classes = (IsAuthenticated,)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = CompanySerializer(data=request.data)
        permission_classes = (IsAuthenticated,)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CompanyDetailAPIView(APIView):
    def get_object(self, pk):
        try:
            return Company.objects.get(id=pk)
        except Company.DoesNotExist as e:
            raise Http404

    def get(self, request, pk=None):
        company = self.get_object(pk)
        serializer = Company2Serializer(company)
        permission_classes = (IsAuthenticated,)
        return Response(serializer.data)
    def put(self, request, pk=None):
        permission_classes = (IsAuthenticated,)
        company = self.get_object(pk)
        serializer = Company2Serializer(instance=company, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def delete(self, request, pk=None):
        permission_classes = (IsAuthenticated,)
        company = self.get_object(pk)
        company.delete()
        return Response({'message': 'deleted'}, status=204)

class CompanyVacanciesAPIView(APIView):
    def get_object(self, pk):
        try:
            return Company.objects.get(id=pk)
        except Company.DoesNotExist as e:
            raise Http404

    def get(self, request, pk=None):
        company = self.get_object(pk)
        serializer = CompanyVacancySerializer(company)
        return Response(serializer.data)

@api_view(['GET', 'POST'])
def VacancyList(request):
    if request.method == 'GET':
        vac = Vacancy.objects.all()
        serializer = Vacancy2Serializer(vac, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        permission_classes = (IsAuthenticated,)
        serializer = Vacancy2Serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)


@api_view(['GET', 'PUT', 'DELETE'])
def VacancyDetail(request, pk):
    try:
        vac = Vacancy.objects.get(id=pk)
    except Vacancy.DoesNotExist as e:
        return Response({'message': str(e)}, status=400)

    if request.method == 'GET':
        serializer = Vacancy2Serializer(vac)
        return Response(serializer.data)
    elif request.method == 'PUT':
        permission_classes = (IsAuthenticated,)
        serializer = Vacancy2Serializer(instance=vac, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    elif request.method == 'DELETE':
        permission_classes = (IsAuthenticated,)
        vac.delete()
        return Response({'message': 'deleted'}, status=204)

class TopTen(APIView):
    def get(self, request):
        vac = Vacancy.objects.order_by('-salary')[:10]
        serializer = Vacancy2Serializer(vac, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)