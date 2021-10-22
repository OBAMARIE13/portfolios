import re
from django.shortcuts import render
from . import models
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

def index(request):
    service = models.Service.objects.filter(status=True)
    banners = models.Banner.objects.filter(status=True).first()
    sites = models.Site.objects.filter(status=True).first()
    abouts = models.About.objects.filter(status=True).first()
    fonction = models.Fonction.objects.filter(status=True)
    experiences = models.Experience.objects.filter(status=True)
    portfolio = models.Portfolios.objects.filter(status=True)
    categories = models.Categorie.objects.filter(status=True) 
    return render(request, "index.html", locals())





@csrf_exempt
def checkup(request):
    success = True
    text = ''
    if request.method == 'POST':
        email = request.POST.get('email')
        name = request.POST.get('name')
        sujet = request.POST.get('sujet')
        message = request.POST.get('message')

        if email.isspace() or email == '' or name.isspace() or name == ''  or sujet.isspace() or sujet == '' or message.isspace() or message == '':
            success = False
            text = 'Veuillez remplir les champs vides'
        elif not re.fullmatch('(\w\.?)+@(\w\.?)+\.[A-Za-z]{2,3}', email):
            success = False
            text = 'Veuillez saisir un email valide'
        elif not re.fullmatch("[A-Za-z'éèëöüïäû ]+", name):
            success = False
            text = 'Veuillez saisir un nom valide'
        else:
            contact = models.Contact(name=name, sujet=sujet, message=message, email=email)
            contact.save()
            text = 'Votre message a bien été enregistré'

    datas = {
        'success':success,
        'text':text
    }

    return JsonResponse(datas, safe=False)