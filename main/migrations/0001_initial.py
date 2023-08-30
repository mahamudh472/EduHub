# Generated by Django 4.2.4 on 2023-08-26 15:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_name', models.CharField(blank=True, max_length=100, null=True)),
                ('desc', models.TextField(blank=True, default='N/A', null=True)),
                ('fee_type', models.CharField(choices=[('one-time', 'One-time'), ('monthly', 'Monthly')], default='monthly', max_length=20)),
                ('fee', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Exam',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('exam_date', models.DateField()),
                ('exam_type', models.CharField(default='Regular Exam', max_length=20)),
                ('max_marks', models.PositiveIntegerField()),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.course')),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('teacher_name', models.CharField(blank=True, max_length=50, null=True)),
                ('date_of_birth', models.DateField(blank=True, default='N/A', null=True)),
                ('gender', models.CharField(blank=True, choices=[('male', 'Male'), ('female', 'Female'), ('custom', 'Custom')], default='N/A', max_length=20, null=True)),
                ('religion', models.CharField(blank=True, default='N/A', max_length=20, null=True)),
                ('contact_number', models.CharField(blank=True, default='N/A', max_length=20, null=True)),
                ('email', models.EmailField(blank=True, default='N/A', max_length=254, null=True)),
                ('qualifications', models.CharField(blank=True, default='N/A', max_length=100, null=True)),
                ('address', models.CharField(blank=True, max_length=20, null=True)),
                ('status', models.CharField(blank=True, choices=[('available', 'Available'), ('unavailable', 'Unavailable')], default='available', max_length=20, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_id', models.CharField(blank=True, max_length=20, null=True)),
                ('student_name', models.CharField(blank=True, max_length=40, null=True)),
                ('date_of_birth', models.DateField(blank=True, default='N/A', null=True)),
                ('gender', models.CharField(blank=True, default='N/A', max_length=20, null=True)),
                ('religion', models.CharField(blank=True, default='N/A', max_length=20, null=True)),
                ('contact_number', models.CharField(blank=True, default='N/A', max_length=20, null=True)),
                ('father_name', models.CharField(blank=True, default='N/A', max_length=20, null=True)),
                ('mother_name', models.CharField(blank=True, default='N/A', max_length=20, null=True)),
                ('home_number', models.CharField(blank=True, default='N/A', max_length=20, null=True)),
                ('address', models.CharField(blank=True, default='N/A', max_length=20, null=True)),
                ('course', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='main.course')),
            ],
        ),
        migrations.CreateModel(
            name='Result',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('obtained_marks', models.PositiveIntegerField()),
                ('exam', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.exam')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.student')),
            ],
        ),
        migrations.CreateModel(
            name='Fee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fee_type', models.CharField(choices=[('one-time', 'One-time'), ('monthly', 'Monthly')], max_length=10)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('due_date', models.DateField()),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.student')),
            ],
        ),
    ]