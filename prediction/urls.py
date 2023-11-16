# urls.py
from django.urls import path
from . import views

urlpatterns = [
    # ... other URL patterns ...
    path('prediction', views.embedded_streamlit_view, name='prediction'),
]
