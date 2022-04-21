from rest_framework import serializers
from .models import Company, Vacancy

class CompanySerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField()
    description = serializers.CharField()
    city = serializers.CharField()
    address = serializers.CharField()

    def create(self, validated_data):
        company = Company.objects.create(name=validated_data['name'], description=validated_data['description'], city = validated_data['city'], address=validated_data['address'])
        return company

    def update(self, instance, validated_data):
        instance.name = validated_data['name']
        instance.description = validated_data['description']
        instance.city = validated_data['city']
        instance.address = validated_data['address']
        instance.save()
        return instance


#name, description, salary, company
class VacancySerializer(serializers.ModelSerializer):
    name = serializers.CharField()
    class Meta:
        model = Vacancy
        fields = ('id', 'name', 'description', 'salary', 'company')
        # read_only_fields = ('name',)

class Company2Serializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ('id', 'name', 'description', 'city', 'address')

class CompanyVacancySerializer(serializers.ModelSerializer):
    #vacancy = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    #vacancy = serializers.StringRelatedField(many=True, read_only=True)
    vacancy = VacancySerializer(many=True, read_only=True)
    class Meta:
        model = Company
        fields = ('id', 'name', 'description', 'city', 'address', 'vacancy')


class Vacancy2Serializer(serializers.ModelSerializer):
    class Meta:
        model = Vacancy
        fields = ('id', 'name', 'description', 'salary', 'company')
        # read_only_fields = ('name',)
