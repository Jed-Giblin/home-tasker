from django.shortcuts import render
from django.views import View
from django.contrib.auth.forms import AuthenticationForm
from django.views.decorators.cache import never_cache


class HomeView(View):
    @never_cache
    def get(self, request):
        return render(request, "home.html")