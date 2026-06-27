# my_django_project/urls.py
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    # ➕ CHANGE .split to .urls right here:
    path('admin/', admin.site.urls),
    
    # This is your ML app route we added earlier
    path('api/', include('api.urls')), 

    path('api/', include('api.urls')), # Routes requests to http://localhost:8000/api/predict/
]