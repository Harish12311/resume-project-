from django.shortcuts import render


def home(requerst):
    return render(requerst, 'core/home.html')


def sevices(requerst):
    return render(requerst, 'core/servicess.html')


def skill(request):
    return render(request, 'core/skill.html')


def contact(requests):
    return render(requests, 'core/contact.html')
