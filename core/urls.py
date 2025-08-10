from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add_student/', views.add_student, name='add_student'),
    path('cie_list/', views.cie_list, name='cie_list'),
    path('exam_fee_form/', views.exam_fee_form, name='exam_fee_form'),
    path('delete_unpaid/', views.delete_unpaid, name='delete_unpaid'),
    path('add_employee/', views.add_employee, name='add_employee'),
    path('high_salary/', views.high_salary, name='high_salary'),
    path('add_exam_student/', views.add_exam_student, name='add_exam_student'),
    path('o_grade/', views.o_grade, name='o_grade'),
    path('add_placement/', views.add_placement, name='add_placement'),
    path('amazon_placed/', views.amazon_placed, name='amazon_placed'),
    path('add_faculty/', views.add_faculty, name='add_faculty'),
    path('cse_professors/', views.cse_professors, name='cse_professors'),
    path('update_grade/', views.update_grade, name='update_grade'),
]
