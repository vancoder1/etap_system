from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    
    # Employee URLs
    path('employees/', views.EmployeeListView.as_view(), name='employee_list'),
    path('employees/add/', views.EmployeeCreateView.as_view(), name='employee_add'),
    path('employees/<int:pk>/edit/', views.EmployeeUpdateView.as_view(), name='employee_edit'),
    path('employees/<int:pk>/delete/', views.EmployeeDeleteView.as_view(), name='employee_delete'),

    # Course URLs
    path('courses/', views.CourseListView.as_view(), name='course_list'),
    path('courses/add/', views.CourseCreateView.as_view(), name='course_add'),
    path('courses/<int:pk>/edit/', views.CourseUpdateView.as_view(), name='course_edit'),
    path('courses/<int:pk>/delete/', views.CourseDeleteView.as_view(), name='course_delete'),

    # Session URLs
    path('sessions/', views.SessionListView.as_view(), name='session_list'),
    path('sessions/add/', views.SessionCreateView.as_view(), name='session_add'),
    path('sessions/<int:pk>/edit/', views.SessionUpdateView.as_view(), name='session_edit'),
    path('sessions/<int:pk>/delete/', views.SessionDeleteView.as_view(), name='session_delete'),

    # Enrollment URLs
    path('enrollments/', views.EnrollmentListView.as_view(), name='enrollment_list'),
    path('enrollments/add/', views.EnrollmentCreateView.as_view(), name='enrollment_add'),
    path('enrollments/<int:pk>/edit/', views.EnrollmentUpdateView.as_view(), name='enrollment_edit'),
]