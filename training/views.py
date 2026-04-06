from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DeleteView
from .models import Employee, Course, Session, Enrollment

# Home View
class HomeView(TemplateView):
    template_name = 'training/home.html'

# --- Employee Views ---
class EmployeeListView(ListView):
    model = Employee
    template_name = 'training/employee_list.html'
    context_object_name = 'employees'

class EmployeeCreateView(CreateView):
    model = Employee
    fields = ['full_name', 'email', 'department']
    template_name = 'training/form.html'
    success_url = reverse_lazy('employee_list')

class EmployeeUpdateView(UpdateView):
    model = Employee
    fields = ['full_name', 'email', 'department']
    template_name = 'training/form.html'
    success_url = reverse_lazy('employee_list')

class EmployeeDeleteView(DeleteView):
    model = Employee
    template_name = 'training/confirm_delete.html'
    success_url = reverse_lazy('employee_list')

# --- Course Views ---
class CourseListView(ListView):
    model = Course
    template_name = 'training/course_list.html'
    context_object_name = 'courses'

class CourseCreateView(CreateView):
    model = Course
    fields = ['title', 'category', 'duration_minutes']
    template_name = 'training/form.html'
    success_url = reverse_lazy('course_list')

class CourseUpdateView(UpdateView):
    model = Course
    fields = ['title', 'category', 'duration_minutes']
    template_name = 'training/form.html'
    success_url = reverse_lazy('course_list')

class CourseDeleteView(DeleteView):
    model = Course
    template_name = 'training/confirm_delete.html'
    success_url = reverse_lazy('course_list')

# --- Session Views ---
class SessionListView(ListView):
    model = Session
    template_name = 'training/session_list.html'
    context_object_name = 'sessions'

class SessionCreateView(CreateView):
    model = Session
    fields = ['course', 'session_date', 'instructor_name', 'mode']
    template_name = 'training/form.html'
    success_url = reverse_lazy('session_list')

class SessionUpdateView(UpdateView):
    model = Session
    fields = ['course', 'session_date', 'instructor_name', 'mode']
    template_name = 'training/form.html'
    success_url = reverse_lazy('session_list')

class SessionDeleteView(DeleteView):
    model = Session
    template_name = 'training/confirm_delete.html'
    success_url = reverse_lazy('session_list')

# --- Enrollment Views ---
class EnrollmentListView(ListView):
    model = Enrollment
    template_name = 'training/enrollment_list.html'
    context_object_name = 'enrollments'

class EnrollmentCreateView(CreateView):
    model = Enrollment
    fields = ['employee', 'session', 'status']
    template_name = 'training/form.html'
    success_url = reverse_lazy('enrollment_list')

class EnrollmentUpdateView(UpdateView):
    model = Enrollment
    fields = ['employee', 'session', 'status']
    template_name = 'training/form.html'
    success_url = reverse_lazy('enrollment_list')

