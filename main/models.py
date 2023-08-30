from django.db import models

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
    fee = models.IntegerField()

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
    student_id = models.CharField(max_length=20, null=True, blank=True)
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
    def __str__(self) -> str:
        return self.student_name

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
    teacher_name = models.CharField(max_length=50, null=True, blank=True)
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


# ---------------------------------------------
# Managinig Fee Status
# ---------------------------------------------

class OneTimeFee(models.Model):
    name = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    students = models.ManyToManyField(Student, through='Payment')

    def __str__(self) -> str:
        return self.name
    

class Month(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self) -> str:
        return self.name

class MonthlyFee(models.Model):
    name = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    months = models.ManyToManyField(Month)
    students = models.ManyToManyField(Student, through='Payment')


class Payment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    fee = models.ForeignKey('OneTimeFee', on_delete=models.CASCADE, null=True, blank=True)
    monthly_fee = models.ForeignKey('MonthlyFee', on_delete=models.CASCADE, null=True, blank=True)
    month = models.ForeignKey(Month, on_delete=models.CASCADE)
    paid = models.BooleanField(default=False)
    payment_date = models.DateField()


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

