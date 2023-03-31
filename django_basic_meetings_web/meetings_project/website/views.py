from django.shortcuts import render
from django.http import HttpResponse
from meetings.models import Meetings


def welcome(request):
    return render(request, "website/welcome.html",
                  {"meetings": Meetings.objects.all()})


# About page with some info about me
def about_me(request):
    return HttpResponse("21 years old from Plovdiv, Bulgaria")

