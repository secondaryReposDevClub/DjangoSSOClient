from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse(f"HI {request.user}")

def p1(request):
    return HttpResponse("You are in p1 view")