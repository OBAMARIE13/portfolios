from django.shortcuts import render
from . import models

# Create your views here.

def index(request):
    service = models.Service.objects.filter(status=True)
    banners = models.Banner.objects.filter(status=True).first()
    sites = models.Site.objects.filter(status=True).first()
    abouts = models.About.objects.filter(status=True).first()
    fonction = models.Fonction.objects.filter(status=True)
    experiences = models.Experience.objects.filter(status=True)
    return render(request, "index.html", locals())