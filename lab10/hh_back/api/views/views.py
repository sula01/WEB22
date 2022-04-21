from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http.response import JsonResponse
from api.models import Company,Vacancy
import json

# Create your views here.
@csrf_exempt
def company_list(request):
    if request.method == 'GET':
        company = Company.objects.all()
        company_json = [comp.to_json() for comp in company]
        return JsonResponse(company_json, safe=False)
    elif request.method == 'POST':
        data = json.loads(request.body)
        try:
            company = Company.objects.create(name=data['name'], description=data['description'], city=data['city'], address=data['address'])
        except Exception as e:
            return JsonResponse({'message': str(e)})

        return JsonResponse(company.to_json())


@csrf_exempt
def company_detail(request, company_id):
    try:
        company = Company.objects.get(id=company_id)
    except Company.DoesNotExist as e:
        return JsonResponse({'message': str(e)}, status=400)

    if request.method == 'GET':
        return JsonResponse(company.to_json())
    elif request.method == 'PUT':
        data = json.loads(request.body)
        company.name = data['name']
        company.description = data['description']
        company.city = data['city']
        company.address = data['address']
        company.save()
        return JsonResponse(company.to_json())
    elif request.method == 'DELETE':
        company.delete()
        return JsonResponse({'message': 'deleted'}, status=204)

def company_vacancies(request, company_id):
    try:
        company = Company.objects.get(id=company_id).vacancy.all()
        company_json = [vacan.to_json() for vacan in company]
        return JsonResponse(company_json, safe=False)
    except Company.DoesNotExist as e:
        return JsonResponse({'message': str(e)}, status=400)

@csrf_exempt
def vacancy_list(request):
    if request.method == 'GET':
        vacancy_list = Vacancy.objects.all()
        vacancy_json = [vac.to_json() for vac in vacancy_list]
        return JsonResponse(vacancy_json, safe=False)
    elif request.method == 'POST':
        data = json.loads(request.body)
        try:
            vacancy = Vacancy.objects.create(name=data['name'], description=data['description'], salary=data['salary'], company_id = data['company_id'])
        except Exception as e:
            return JsonResponse({'message': str(e)})

        return JsonResponse(vacancy.to_json())

@csrf_exempt
def vacancy_detail(request, vacancy_id):
    try:
        vacancy = Vacancy.objects.get(id=vacancy_id)
    except Vacancy.DoesNotExist as e:
        return JsonResponse({'message': str(e)}, status=400)

    if request.method == 'GET':
        return JsonResponse(vacancy.to_json())
    elif request.method == 'PUT':
        data = json.loads(request.body)
        vacancy.name = data['name']
        vacancy.description = data['description']
        vacancy.salary = data['salary']
        vacancy.company_id = data['company_id']
        vacancy.save()
        return JsonResponse(vacancy.to_json())
    elif request.method == 'DELETE':
        vacancy.delete()
        return JsonResponse({'message': 'deleted'}, status=204)


def top_ten_vacancies(request):
    try:
        vacancy_list = Vacancy.objects.all()[:10]
        vacancy_json = [vac.to_json() for vac in vacancy_list]
        return JsonResponse(vacancy_json, safe=False)
    except Company.DoesNotExist as e:
        return JsonResponse({'message': str(e)}, status=400)
