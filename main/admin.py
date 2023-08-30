from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Student)
admin.site.register(Course)
admin.site.register(Teacher)
admin.site.register(OneTimeFee)
admin.site.register(Month)
admin.site.register(MonthlyFee)
admin.site.register(Payment)
admin.site.register(Exam)
admin.site.register(Result)
