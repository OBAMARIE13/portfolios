from django.db import models

# Create your models here.

class Site(models.Model):
    nom_site = models.CharField(max_length=255)
    lieu = models.CharField(max_length=255)
    phone = models.CharField(max_length=200)
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)
    

    class Meta:
        verbose_name = 'Site'
        verbose_name_plural = 'Sites'

    def __str__(self):
        return self.nom_site



class Banner(models.Model):
    nom = models.CharField(max_length=255)
    profession = models.CharField(max_length=255)
    photo = models.FileField(upload_to="banner_photo")
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)
    

    class Meta:
        verbose_name = 'Banner'
        verbose_name_plural = 'Banners'

    def __str__(self):
        return self.nom



class About(models.Model):
    description = models.CharField(max_length=255)
    photo = models.FileField(upload_to="banner_photo")
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)
    

    class Meta:
        verbose_name = 'About'
        verbose_name_plural = 'Abouts'

    def __str__(self):
        return self.description



class Service(models.Model):
    titre = models.CharField(max_length=200)
    icone = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)
    

    class Meta:
        verbose_name = 'Service'
        verbose_name_plural = 'Services'

    def __str__(self):
        return self.titre



class Experience(models.Model):
    periode = models.CharField(max_length=200)
    fonction_occupee = models.CharField(max_length=255)
    lieu_fonction = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)
    

    class Meta:
        verbose_name = 'Experience'
        verbose_name_plural = 'Experiences'

    def __str__(self):
        return self.periode



class Portfolios(models.Model):
    nom = models.CharField(max_length=200)
    photo = models.FileField(upload_to="portfolios")
    categorie = models.ForeignKey('christelle.Categorie', related_name='categorie_portfolios', on_delete=models.CASCADE)
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)
    

    class Meta:
        verbose_name = 'Portfolios'
        verbose_name_plural = 'Portfolioss'

    def __str__(self):
        return self.nom


class Categorie(models.Model):
    nom= models.CharField(max_length=255)
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Categorie'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.nom



class Contact(models.Model):
    nom = models.CharField(max_length=255)
    email = models.EmailField()
    message = models.CharField(max_length=255)
    sujet = models.CharField(max_length=50)
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Contact'
        verbose_name_plural = 'Contacts'

    def __str__(self):
        return self.nom


class Sociaux(models.Model):
    icone = models.CharField(max_length=255)
    nom = models.CharField(max_length=255)
    lien = models.TextField()
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Sociaux'
        verbose_name_plural = 'Sociaux'

    def __str__(self):
        return self.nom



class Fonction(models.Model):
    nom = models.CharField(max_length=255)
    niveau = models.CharField(max_length=50)
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Fonction'
        verbose_name_plural = 'Fonctions'

    def __str__(self):
        return self.nom