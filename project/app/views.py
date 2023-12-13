from django.http import HttpResponse
from django.shortcuts import render, redirect

from .forms import AddForm
from .models import Person

def create(request):
    if request.method == "POST":
        form = AddForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            surname = form.cleaned_data['surname']
            age = form.cleaned_data['age']
            gender = form.cleaned_data['gender']
            birthDay = form.cleaned_data['birthDay']
            person, _ = Person.objects.get_or_create(
                name=name, surname=surname, age=age, gender=gender, birthDay=birthDay
            )
            return redirect('home')
    else:
        form = AddForm()
    return render(request, 'user/create.html', context={'form': form})
def index(request):
    # makeMen()
    people = Person.objects.all()
    return render(request, 'user/index.html', context={'people':people})

def delete(request, id):
    try:
        men = Person.objects.get(pk=id)
        men.delete()
        return redirect('home')
    except:
        return HttpResponse('все плохо')
def update(request, id):
    men = Person.objects.get(pk=id)
    if request.method == "POST":
        name=request.POST.get('name')
        age = request.POST.get('age')
        birthDay = request.POST.get('birthDay')
        gender = request.POST.get('gender')
        surname = request.POST.get('surname')
        men.name = name
        men.surname = surname
        men.age = age
        men.gender = gender
        men.birthDay = birthDay
        men.save()
        return redirect('home')
    else:
        return render(request, 'user/update.html', context={'men': men})
# def makeMen():
#     p, _ = Person.objects.get_or_create(name='Tom', surname='egeg', age=18, gender=True, birthDay='2011-12-12')
#     p, _ = Person.objects.get_or_create(name='Tom1', surname='egegвм', age=28, gender=True, birthDay='2011-11-22')
#     p, _ = Person.objects.get_or_create(name='Tom2', surname='egegвм', age=48, gender=True, birthDay='2011-07-02')
#     p, _ = Person.objects.get_or_create(name='Tom3', surname='egegыаыау', age=3, gender=True, birthDay='2011-02-12')
#     p, _ = Person.objects.get_or_create(name='Tom4', surname='egegцац', age=17, gender=True, birthDay='2011-10-12')
