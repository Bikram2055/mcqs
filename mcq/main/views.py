from django.http import HttpResponse
# from django.shortcuts import render
from django.views import View

# Create your views here.


class Index(View):
    def get(self, request):
        return HttpResponse("<h1>this is the project for mcq</h1>")
<<<<<<< HEAD
=======

    def post(self, request):
        return HttpResponse("abc")
>>>>>>> 0b691d5363afa313b4a49b63f8f5bd38e1838c7b
