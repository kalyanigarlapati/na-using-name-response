from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def wish(request,na):
    return HttpResponse(f' how {na} r u')