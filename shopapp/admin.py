from django.contrib import admin
from .models import Product, Category, Subsection, Section

# Register your models here.
admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Subsection)
admin.site.register(Section)
