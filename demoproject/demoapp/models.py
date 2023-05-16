from django.db import models

class Todo(models.Model):
    Name = models.CharField(max_length=30)
    Date_Of_Birth = models.DateField()
    email = models.EmailField()
    Designation = models.CharField(max_length=100)
    Salary = models.IntegerField()

    class Meta:
        unique_together = ('Name', 'Date_Of_Birth', 'email')
