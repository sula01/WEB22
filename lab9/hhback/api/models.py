from django.db import models
from django.db.models import CharField, FloatField, TextField
from django.db.models.fields.related import ForeignKey

class Company(models.Model):
    name = CharField(max_length=255)
    description = TextField()
    city = CharField(max_length=30)
    address = TextField()

    class Meta:
        verbose_name_plural = 'Companies'

    def to_json(self):
        return {
            'id': self.pk,
            'name': self.name,
            'description': self.description,
            'city': self.city,
            'address': self.address,
        }
    
    def __str__(self):
        return self.name

class Vacancy(models.Model):
    name = CharField(max_length=255)
    description = TextField()
    salary = FloatField()
    company = ForeignKey(Company, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'Vacancies'

    def to_json(self):
        return {
            'id': self.pk,
            'name': self.name,
            'description': self.description,
            'salary': self.salary,
            # 'company': self.company,
        }
    
    def __str__(self):
        return f'{self.name} | {str(self.company)}'
