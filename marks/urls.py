from django.urls import path
from .views import  add_student,student_list, signin_view

urlpatterns = [
    path('', signin_view, name='signin'),  # Handle the root path
    path('list/', student_list, name='student_list'),
    path('add/', add_student, name='add_student'),
    # Add other URL patterns...
]
