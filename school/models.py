from django.db import models
from django.contrib.auth.models import AbstractUser, User

# Create your models here.
class User(AbstractUser):
    ROLE_CHOICES = (
        ("T", "Teacher"),
        ("S", "Student"),
    )
    
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default="S")


class AcademicSession(models.Model):
    name = models.CharField(max_length=9)
    start_date = models.DateField()
    end_date = models.DateField()
    
class Term(models.Model):
    TERMS = (
        ("1st", "1st Term"),
        ("2nd", "2nd Term"),
        ("3rd", "3rd Term"),
    )
    
    name = models.CharField(max_length=9, choices=TERMS)
    academic_session = models.ForeignKey(AcademicSession, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    
    
class SchoolClass(models.Model):
    CLASSES = (
        ("JSS1", "JSS1"),
        ("JSS2", "JSS2"),
        ("JSS3", "JSS3"),
        ("SSS1", "SSS1"),
        ("SSS1", "SSS1"),
        ("SSS1", "SSS1"),
    )
    
    name = models.CharField(max_length=9, choices=CLASSES)
    teacher = models.ForeignKey("Teacher", on_delete=models.SET_NULL, null=True)


class Student(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="student_profile")
    academic_session = models.ForeignKey(AcademicSession, on_delete=models.CASCADE)
    school_class = models.ForeignKey(SchoolClass, on_delete=models.CASCADE)


class Teacher(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    academic_session = models.ForeignKey(AcademicSession, on_delete=models.CASCADE)
    
