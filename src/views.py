from django.contrib.auth.models import User
from django.shortcuts           import render


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
	template_name="registrarse.html"
	ctx={}
	return render(request, template_name, ctx)


