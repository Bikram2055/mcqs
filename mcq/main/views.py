from django.http import HttpResponse
# from django.shortcuts import render
from django.views import View

# Create your views here.


class Index(View):
    def get(self, request):
        return HttpResponse("<h1>this is the project for mcq</h1>")