# marks/forms.py
from django import forms
from .models import Student, MarkSheet

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'roll_number']


class MarkSheetForm(forms.ModelForm):
    class Meta:
        model = MarkSheet
        fields = ['hindi', 'english', 'science', 'maths', 'total_marks']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['hindi'].label = 'Hindi Marks'
        self.fields['english'].label = 'English Marks'
        self.fields['science'].label = 'Science Marks'
        self.fields['maths'].label = 'Maths Marks'
