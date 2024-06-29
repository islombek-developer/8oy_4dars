from django.contrib import admin
from .models import Travel,Hotel,Klass, Review, Category, Products


admin.site.register(Travel)
admin.site.register(Hotel)
admin.site.register(Klass)


admin.site.register(Review)
admin.site.register(Category)
admin.site.register(Products)