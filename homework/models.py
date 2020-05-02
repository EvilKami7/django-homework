from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=32, null=False)
    surname = models.CharField(max_length=32, null=False)

    def __str__(self):
        return f'{self.surmane} {self.name}'

    def __repr__(self):
        return f'Student(name="{self.name}", surname="{self.surname}"'

class Subject(models.Model):
    name = models.TextField()

class Score(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)

    value = models.IntegerField(default=8)