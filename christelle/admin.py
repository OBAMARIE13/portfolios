from django.contrib import admin
from . import models
from django.utils.safestring import mark_safe
from django.utils.safestring import mark_safe

# Register your models here.

@admin.register(models.Site)
class SiteAdmin(admin.ModelAdmin):
	list_display = ('nom_site', 'lieu', 'phone', 'date_add', 'date_update', 'status')
	

@admin.register(models.Banner)
class BannerAdmin(admin.ModelAdmin):
	list_display = ('nom', 'profession', 'picture_view', 'date_add', 'date_update', 'status')
	

	def picture_view(self, obj):
		return mark_safe(f'<img src="{obj.photo}" style="height:100px; width:150px">')
	picture_view.short_description = 'Aperçu des images'


@admin.register(models.About)
class AboutAdmin(admin.ModelAdmin):
	list_display = ('description', 'picture_view', 'date_add', 'date_update', 'status')
	

	def picture_view(self, obj):
		return mark_safe(f'<img src="{obj.photo}" style="height:100px; width:150px">')
	picture_view.short_description = 'Aperçu des images'


@admin.register(models.Fonction)
class FonctionAdmin(admin.ModelAdmin):
	list_display = ('nom', 'niveau', 'date_add', 'date_update', 'status')
	

@admin.register(models.Service)
class ServiceAdmin(admin.ModelAdmin):
	list_display = ('titre', 'icone', 'description', 'date_add', 'date_update', 'status')
	

@admin.register(models.Experience)
class ExperienceAdmin(admin.ModelAdmin):
	list_display = ('periode', 'fonction_occupee', 'lieu_fonction', 'description', 'date_add', 'date_update', 'status')


@admin.register(models.Portfolios)
class PortfoliosAdmin(admin.ModelAdmin):
	list_display = ('nom', 'picture_view', 'categorie', 'date_add', 'date_update', 'status')
	

	def picture_view(self, obj):
		return mark_safe(f'<img src="{obj.photo}" style="height:100px; width:150px">')
	picture_view.short_description = 'Aperçu des images'


@admin.register(models.Categorie)
class CategorieAdmin(admin.ModelAdmin):
	list_display = ('nom', 'date_add', 'date_update', 'status')
	

@admin.register(models.Contact)
class ContactAdmin(admin.ModelAdmin):
	list_display = ('nom', 'email', 'message', 'sujet', 'date_add', 'date_update', 'status')


@admin.register(models.Sociaux)
class SociauxAdmin(admin.ModelAdmin):
	list_display = ('icone', 'nom', 'lien', 'date_add', 'date_update', 'status')
	