from django.contrib.auth.models import User
from django.shortcuts           import render
from django.contrib import messages
from django.contrib.auth.forms  import UserCreationForm


def inicio(request):
	template_name="inicio.html"
	ctx= {}
	return render(request,template_name, ctx)

def contacto(request):
	template_name="contacto.html"
	ctx={}
	return render(request, template_name, ctx)
"""
def login(request):
	template_name="login.html"
	ctx={}
	return render(request, template_name, ctx)
"""
def principal(request):
	template_name="principal.html"
	ctx={}
	return render(request, template_name, ctx)

def registrarse(request):
	if request.method == 'POST':
		form = UserCreationForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data['username']
			messages.success(request, f'Usuario {username} creado')
			return redirect('principal.html')
	else:
		form = UserCreationForm()

	ctx = { 'form' : form }
	return render(request, 'registrarse.html', ctx)



