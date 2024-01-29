# marks/views.py

from django.shortcuts import render, redirect
from .models import Student, MarkSheet
from .forms import StudentForm, MarkSheetForm
from django.contrib.auth import authenticate, login
from django.contrib import messages


def student_list(request):
    students = Student.objects.all()
    return render(request, 'student_list.html', {'students': students})

def signin_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('student_list')  # Redirect to student list upon successful login
        else:
            # Authentication failed, you might want to display an error message
            return render(request, 'signin.html', {'error': 'Invalid credentials'})

    return render(request, "signin.html")

def add_student(request):
    if request.method == 'POST':
        student_form = StudentForm(request.POST)
        mark_sheet_form = MarkSheetForm(request.POST)

        if student_form.is_valid() and mark_sheet_form.is_valid():
            student = student_form.save(commit=False)
            mark_sheet = mark_sheet_form.save()
            student.marks = mark_sheet
            student.save()
            
            messages.success(request, 'Student added successfully.')
            return redirect('add_student')

    else:
        student_form = StudentForm()
        mark_sheet_form = MarkSheetForm()

    return render(request, "add_student.html", {'student_form': student_form, 'mark_sheet_form': mark_sheet_form})