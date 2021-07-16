from django.contrib import admin

# Register your models here.

from .models import Author, Country, Question, Choice

admin.site.register(Question)
admin.site.register(Choice)
admin.site.register(Country)
admin.site.register(Author)
