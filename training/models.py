from django.db import models

class Employee(models.Model):
    DEPARTMENTS = [
        ('IT', 'Information Technology'),
        ('HR', 'Human Resources'),
        ('Sales', 'Sales'),
    ]
    full_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    department = models.CharField(max_length=50, choices=DEPARTMENTS)

    def __str__(self):
        return f"{self.full_name} ({self.department})"

class Course(models.Model):
    CATEGORIES = [
        ('Technical', 'Technical'),
        ('Security', 'Security Awareness'),
        ('Soft Skills', 'Soft Skills'),
        ('Compliance', 'Compliance and Safety'),
    ]
    title = models.CharField(max_length=200)
    category = models.CharField(max_length=50, choices=CATEGORIES)
    duration_minutes = models.PositiveIntegerField()

    def __str__(self):
        return self.title

class Session(models.Model):
    MODES = [
        ('Online', 'Online'),
        ('In-Person', 'In-Person'),
    ]
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    session_date = models.DateField()
    instructor_name = models.CharField(max_length=100)
    mode = models.CharField(max_length=20, choices=MODES)

    def __str__(self):
        return f"{self.course.title} - {self.session_date}"

class Enrollment(models.Model):
    STATUSES = [
        ('ENROLLED', 'Enrolled'),
        ('COMPLETED', 'Completed'),
        ('CANCELLED', 'Cancelled'),
    ]
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    session = models.ForeignKey(Session, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=STATUSES, default='ENROLLED')

    class Meta:
        unique_together = ('employee', 'session')

    def __str__(self):
        return f"{self.employee.full_name} -> {self.session.course.title} ({self.status})"

