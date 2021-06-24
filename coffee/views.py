from django.shortcuts import render, redirect
from django.http import HttpResponse

from .forms import RegisterForm


def index(request):

    form = RegisterForm()

    # if request.method == 'POST':
    #     form = RegisterForm(request.POST)
    #     if form.is_valid():
    #         # name = form.cleaned_data.get('name')
    #         # # password = form.cleaned_data.get('password')
    #         # print(name)
    #         form.save()

    #     return redirect("/welcome/")

    context = {'form': form}
    return render(request, 'index.html', context)
    # return render(request, 'index.html')


def welcome(request):

    form = RegisterForm()
    form = RegisterForm(request.POST)
    name = request.POST.get('name')
    email = request.POST.get('email')
    context = {'name': name}

    return render(request, 'welcome.html', context)


def message(request):
    coffee = request.POST.get('coffee')

    method = request.POST.get('method')

    instruction = request.POST.get('instruction')

    context = {'coffee': coffee, 'method': method,
               'instruction': instruction}

    return render(request, "message.html", context)
