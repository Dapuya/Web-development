from django.db import models

class Company(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(max_length=255)
    city = models.CharField(max_length=20)
    address = models.TextField(max_length=255)

    class Meta:
        verbose_name_plural = 'Companies'

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'city': self.city,
            'address': self.address,
        }

    def __str__(self):
        return self.name


class Vacancy(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(max_length=255)
    salary = models.FloatField(default=0)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)

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