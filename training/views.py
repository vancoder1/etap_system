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

    def get_queryset(self):
        qs = super().get_queryset()
        department = self.request.GET.get('department')
        if department:
            qs = qs.filter(department=department)
        return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['departments'] = Employee.DEPARTMENTS
        context['selected_dept'] = self.request.GET.get('department', '')
        return context

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

    def get_queryset(self):
        qs = super().get_queryset()
        category = self.request.GET.get('category')
        if category:
            qs = qs.filter(category=category)
        return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Course.CATEGORIES
        context['selected_cat'] = self.request.GET.get('category', '')
        return context

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

    def get_queryset(self):
        qs = super().get_queryset()
        start_date = self.request.GET.get('start_date')
        end_date = self.request.GET.get('end_date')
        instructor = self.request.GET.get('instructor')

        if start_date:
            qs = qs.filter(session_date__gte=start_date)
        if end_date:
            qs = qs.filter(session_date__lte=end_date)
        if instructor:
            qs = qs.filter(instructor_name__icontains=instructor)
            
        return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['selected_start'] = self.request.GET.get('start_date', '')
        context['selected_end'] = self.request.GET.get('end_date', '')
        context['selected_instructor'] = self.request.GET.get('instructor', '')
        return context

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

    def get_queryset(self):
        qs = super().get_queryset()
        status = self.request.GET.get('status')
        if status:
            qs = qs.filter(status=status)
        return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['statuses'] = Enrollment.STATUS_CHOICES
        context['selected_status'] = self.request.GET.get('status', '')
        return context

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

