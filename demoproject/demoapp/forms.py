from django import forms
from .models import Todo

class Employee(forms.ModelForm):
    class Meta:
        model = Todo
        unique_together = ('Name', 'Date_Of_Birth', 'email')
        fields = [
            "Name",
            "Date_Of_Birth",
            "email",
            "Designation",
            "Salary",
        ]
