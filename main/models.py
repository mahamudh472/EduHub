from django.db import models
import os
from django.utils import timezone

# ---------------------------------------------
# Managinig Students, Teachers and Course Data
# ---------------------------------------------
class Course(models.Model):
    FEE_TYPES = (
        ('one-time', 'One-time'),
        ('monthly', 'Monthly'),
    )

    course_name = models.CharField(max_length=100, null=True, blank=True)
    desc = models.TextField(null=True, blank=True, default='N/A')
    fee_type = models.CharField(max_length=20, choices=FEE_TYPES)
    fee = models.IntegerField(null=True, blank=True)
    first_roll = models.IntegerField(default=1)
    def __str__(self) -> str:
        return self.course_name
    
    def student_count(self):
        return self.student_set.count()
    

class Student(models.Model):
    GENDERS = (
        ('male', "Male"),
        ('female', 'Female'),
        ('custom', 'Custom'),
    )
    STATUS = (
        ('running', 'Running'),
        ('finished', 'Finished')
    )
    student_id = models.IntegerField(unique=True, null=True, blank=True)
    student_photo = models.ImageField(upload_to='student_photos/', null=True, blank=True)
    student_name = models.CharField(max_length=40, null=True, blank=True)
    date_of_birth = models.DateField(blank=True, null=True, default='N/A')
    gender = models.CharField(max_length=20,choices=GENDERS, null=True, blank=True, default='N/A')
    religion = models.CharField(max_length=20, null=True, blank=True, default='N/A')
    contact_number = models.CharField(max_length=20, null=True, blank=True, default='N/A')
    father_name = models.CharField(max_length=20, null=True, blank=True, default='N/A')
    mother_name = models.CharField(max_length=20, null=True, blank=True, default='N/A')
    home_number = models.CharField(max_length=20, null=True, blank=True, default='N/A')
    address = models.CharField(max_length=20, null=True, blank=True, default='N/A')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, default=0)
    status = models.CharField(max_length=15, choices=STATUS, default="N/A")

    def get_status(self):
        temp = True
        for i in self.monthlyfee_set.all():
            if i.status == False:
                temp = False
            
        return temp



    def __str__(self) -> str:
        return self.student_name
    
    def delete(self, *args, **kwargs):
        # Delete the associated photo when the student is deleted
        if self.student_photo:
            # Delete the file from the media folder
            if os.path.isfile(self.student_photo.path):
                os.remove(self.student_photo.path)

        super().delete(*args, **kwargs)

class Teacher(models.Model):
    GENDERS = (
        ('male', "Male"),
        ('female', 'Female'),
        ('custom', 'Custom'),
    )
    STATUS = (
        ('available', 'Available'),
        ('unavailable', 'Unavailable')
    )
    teacher_photo = models.ImageField(upload_to='teacher_photos', null=True, blank=True)
    teacher_name = models.CharField(max_length=50, null=True, blank=True)
    teacher_position = models.CharField(max_length=50, null=True, blank=True)
    date_of_birth = models.DateField(blank=True, null=True, default='N/A')
    gender = models.CharField(max_length=20, choices=GENDERS, null=True, blank=True, default='N/A')
    religion = models.CharField(max_length=20, null=True, blank=True, default='N/A')
    contact_number = models.CharField(max_length=20, null=True, blank=True, default='N/A')
    email = models.EmailField(null=True, blank=True, default='N/A')
    qualifications = models.CharField(max_length=100, null=True, blank=True, default='N/A')
    address = models.CharField(max_length=20, null=True, blank=True)
    status = models.CharField(max_length=20, null=True, blank=True, choices=STATUS, default="available")

    def __str__(self) -> str:
        return self.teacher_name

    def delete(self, *args, **kwargs):
        # Delete the associated photo when the student is deleted
        if self.teacher_photo:
            # Delete the file from the media folder
            if os.path.isfile(self.teacher_photo.path):
                os.remove(self.teacher_photo.path)

        super().delete(*args, **kwargs)

# ---------------------------------------------
# Managinig Fee Status
# ---------------------------------------------

class OneTimeFee(models.Model):
    name = models.CharField(max_length=100)
    student = models.OneToOneField(Student, on_delete=models.CASCADE, blank=True, null=True)
    status = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.name
MONTHS = (
    ('january', 'January'),
    ('february', 'February'),
    ('march', 'March'),
    ('april', 'April'),
    ('may', 'May'),
    ('june', 'June'),
    ('july', 'July'),
    ('august', 'August'),
    ('september', 'September'),
    ('october', 'October'),
    ('november', 'November'),
    ('december', 'December'),
)

class MonthlyFee(models.Model):
    month_name = models.CharField(max_length=100)
    student = models.ForeignKey(Student, on_delete=models.CASCADE, blank=True, null=True)
    status = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.month_name    
    
# ---------------------------------------------
# Managinig Exams and Results
# ---------------------------------------------

class Exam(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    exam_date = models.DateField()
    exam_type = models.CharField(max_length=20, default="Regular Exam")
    max_marks = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.exam_type} - {self.course}"

class Result(models.Model):
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    obtained_marks = models.PositiveIntegerField()

    def __str__(self):
        return f"Result for {self.student} in {self.exam}"

