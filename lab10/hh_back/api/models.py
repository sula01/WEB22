from django.db import models

class Company(models.Model):
    name = models.CharField(max_length=250)
    description = models.TextField(max_length=1000)
    city = models.CharField(max_length=250)
    address = models.TextField(max_length=1000)

    class Meta:
        verbose_name = 'Компания'
        verbose_name_plural = 'Компании'
        # ordering = ('name',)

    def to_json(self):
        return {
            'name': self.name,
            'description': self.description,
            'city': self.city,
            'address': self.address
        }

    def __str__(self):
        return f'{self.id}: {self.name} | {self.description}'

class Vacancy(models.Model):
    name = models.CharField(max_length=250)
    description = models.TextField(max_length=1000)
    salary = models.FloatField()
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='vacancy')
    class Meta:
        verbose_name = 'Вакансия'
        verbose_name_plural = 'Вакансии'
        ordering = ('-salary',)

    def to_json(self):
        return {
            'name': self.name,
            'description': self.description,
            'salary': self.salary,
            'company': self.company_id
        }

    def __str__(self):
        return f'{self.id}: {self.name}, {self.description}'