from project1.bot import main
import asyncio
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt

from project1.models import ModelAlex, ModelReg


@csrf_exempt
def index(request):
    if request.method == 'POST':
        asyncio.run(main()) #запуск бота
    return render(request, 'index.html')

@csrf_exempt
def login(request):
    reg = ModelReg()
    if request.method == 'POST':
        data = ModelReg.objects.all()
        for i in data:
            if request.POST['email'] == i.email:
                return render(request, 'index.html', {"err": f'Email: {i.email} занят другим пользователем'})
        reg.email = request.POST['email']
        reg.password = request.POST['password']
        reg.login = request.POST['login']
        reg.save()
        return HttpResponse(f'Пользователь с Email: {reg.email} успешно зарегистрирован!')
    return render(request, 'login.html')


@csrf_exempt
def author(request):
    if request.method == 'POST':
        data = ModelReg.objects.all()
        print(data)
        print(f"Из пост запроса. Почта: {request.POST['email']} Pass: {request.POST['password']}")
        for i in data:
            print(f'Текущий объект из базы данных. Почта: {i.email} Pass: {i.password}')
            if request.POST['email'] == i.email and request.POST['password'] == i.password:
                return HttpResponse('авторизация прошла успешно')
        return render(request, 'index.html', {'err': 'авторизация не пройдена'})
    return render(request, 'author.html')
