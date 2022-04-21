from django.contrib import admin
from django.urls import path
from .views import companies_list, company_detail, company_vacancies, vacancies_list, vacancies_top_ten, vacancy_detail

urlpatterns = [
    path('companies/', companies_list),
    path('companies/<int:company_id>/', company_detail),
    path('companies/<int:company_id>/vacancies/', company_vacancies),
    path('vacancies/', vacancies_list),
    path('vacancies/<int:vacancy_id>/', vacancy_detail),
    path('vacancies/top_ten/', vacancies_top_ten),
]
