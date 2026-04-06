from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DeleteView
from .models import Employee

# Home View
class HomeView(TemplateView):
    template_name = 'training/home.html'

# Employee Views
class EmployeeListView(ListView):
    model = Employee
    template_name = 'training/employee_list.html'
    context_object_name = 'employees'

class EmployeeCreateView(CreateView):
    model = Employee
    fields = ['full_name', 'email', 'department']
    template_name = 'training/form.html'  # Generic form template
    success_url = reverse_lazy('employee_list')

class EmployeeUpdateView(UpdateView):
    model = Employee
    fields = ['full_name', 'email', 'department']
    template_name = 'training/form.html'
    success_url = reverse_lazy('employee_list')

class EmployeeDeleteView(DeleteView):
    model = Employee
    template_name = 'training/confirm_delete.html'  # Generic delete template
    success_url = reverse_lazy('employee_list')
