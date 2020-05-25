from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import Note

# Create your views here.
def index(request):
    return render(request, 'app/index.html')

def createNote (request):
    if request.method == 'POST':
        noteHeading = request.POST.get('noteHeading')
        noteBody = request.POST.get('noteBody')
        note = Note.objects.create(author=request.user,noteHeading=noteHeading, noteBody=noteBody)
        note.save()
        return redirect('notes')

def notes (request):
    notes = Note.objects.filter(author = request.user)
    return render(request, 'app/notes.html')

def p1(request):
    return HttpResponse("You are in p1 view")

def logout(request):
    return render(request, 'app/logout.html')

def public(request):
    return HttpResponse('This is visible to everyone')