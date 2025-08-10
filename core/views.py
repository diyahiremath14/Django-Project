# views.py
from django.shortcuts import render, redirect
from .models import StudentCIE
from .models import ExamFee
from .models import Employee,ExamStudent,FinalYearPlacement,Faculty,StudentGrade

def home(request):
    return render(request, 'core/home.html')

def add_student(request):
    if request.method == 'POST':
        StudentCIE.objects.create(
            usn=request.POST['usn'],
            name=request.POST['name'],
            subject_code=request.POST['subject_code'],
            cie_marks=request.POST['cie_marks']
        )
        return redirect('cie_list')
    return render(request, 'add_cie.html')

def cie_list(request):
    students = StudentCIE.objects.filter(cie_marks__lt=20)
    return render(request, 'cie_list.html', {'students': students})

def exam_fee_form(request):
    if request.method == 'POST':
        ExamFee.objects.create(
            name=request.POST['name'],
            usn=request.POST['usn'],
            semester=request.POST['semester'],
            fee_paid='fee_paid' in request.POST
        )
        return redirect('delete_unpaid')
    return render(request, 'fee_form.html')

def delete_unpaid(request):
    ExamFee.objects.filter(fee_paid=False).delete()
    return render(request, 'deleted.html')

def add_employee(request):
    if request.method == 'POST':
        Employee.objects.create(
            name=request.POST['name'],
            email=request.POST['email'],
            phone=request.POST['phone'],
            hired_date=request.POST['hired_date'],
            job_title=request.POST['job_title'],
            salary=request.POST['salary']
        )
        return redirect('high_salary')
    return render(request, 'add_employee.html')

def high_salary(request):
    employees = Employee.objects.filter(salary__gt=50000)
    return render(request, 'high_salary.html', {'employees': employees})

def add_exam_student(request):
    if request.method == 'POST':
        ExamStudent.objects.create(
            name=request.POST['name'],
            usn=request.POST['usn'],
            grade=request.POST['grade']
        )
        return redirect('o_grade')
    return render(request, 'exam_form.html')

def o_grade(request):
    students = ExamStudent.objects.filter(grade='O')
    return render(request, 'o_grade_list.html', {'students': students})

def add_placement(request):
    if request.method == 'POST':
        FinalYearPlacement.objects.create(
            name=request.POST['name'],
            usn=request.POST['usn'],
            company=request.POST['company']
        )
        return redirect('amazon_placed')
    return render(request, 'placement_form.html')

def amazon_placed(request):
    students = FinalYearPlacement.objects.filter(company__iexact='Amazon')
    return render(request, 'amazon_list.html', {'students': students})

def add_faculty(request):
    if request.method == 'POST':
        Faculty.objects.create(
            fid=request.POST['fid'],
            title=request.POST['title'],
            name=request.POST['name'],
            branch=request.POST['branch']
        )
        return redirect('cse_professors')
    return render(request, 'faculty_form.html')

from django.shortcuts import render
from .models import Faculty

def cse_professors(request):
    faculty = Faculty.objects.filter(branch__iexact='CSE', title__iexact='Professor')
    return render(request, 'faculty_list.html', {'faculty': faculty})


def update_grade(request):
    if request.method == 'POST':
        name = request.POST['name']
        new_grade = request.POST['grade']
        StudentGrade.objects.filter(name=name).update(grade=new_grade)
        students = StudentGrade.objects.all()
        return render(request, 'grade_list.html', {'students': students})
    return render(request, 'update_grade.html')
