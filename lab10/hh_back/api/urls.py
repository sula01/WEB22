from django.urls import path
from rest_framework_jwt.views import obtain_jwt_token
from api.views import CompanyListAPIView,CompanyDetailAPIView, VacancyDetail, VacancyList, TopTen, CompanyVacanciesAPIView

urlpatterns=[
    path('login/', obtain_jwt_token),
    path('companies/', CompanyListAPIView.as_view()),
    path('companies/<int:pk>/', CompanyDetailAPIView.as_view()),
    path('companies/<int:pk>/vacancies/', CompanyVacanciesAPIView.as_view()),
    path('vacancies/', VacancyList),
    path('vacancies/<int:pk>/', VacancyDetail),
    path('vacancies/top_ten/', TopTen.as_view()),

]
