from django.urls import path
from tasker_ui.views import LoginView ,HomeView

urlpatterns = [
    path('', HomeView.as_view(), name='Home'),
]