from django.shortcuts import render
from django.views import View
from django.contrib.auth.forms import AuthenticationForm


class LoginView(View):
    def get(self, request):
        return render(request, "login.html", {'form': AuthenticationForm})