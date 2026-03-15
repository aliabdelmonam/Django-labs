from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('instructor/',include('Instrcutor.urls')),
    path('student/',include('Students.urls'))
]
