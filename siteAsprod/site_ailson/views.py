from django.shortcuts import render

from .models import *

def home(request):
    projeto = Projeto.objects.all()

    dados = {

        'projeto': projeto
    }

    return render(request, "home.html", dados)

# Create your views here.
