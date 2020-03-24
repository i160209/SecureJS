from django.urls import path
from .import views

app_name='DashBoard'

urlpatterns = [
	path('', views.DashBoard, name='DashBoard'),
	path('DetectVulnerability/File/', views.DetectVulnerability_File, name='DetectVulnerability_File'),
	path('DetectVulnerability/SourceCode/', views.DetectVulnerability_Code, name='DetectVulnerability_Code'),
	path('DetectVulnerability/VulnerableLibraries/', views.DetectVulnerability_Library, name='DetectVulnerability_Library'),
	path('Vulnerability/XSS/', views.XSS, name='XSS'),
	path('Vulnerability/Injection/', views.Injection, name='Injection'),
	path('Vulnerability/BrokenAccessControl/', views.BAC, name='BrokenAccessControl'),
	path('Vulnerability/BrokenAuthentication/', views.BA, name='BrokenAuthentication'),
	path('Scan/', views.Scan, name='Scan'),
]
