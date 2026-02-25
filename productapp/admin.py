from django.contrib import admin
from .models import Product
#(.models => productapp.models) no need to write package_name if you are in/working in same package


# Register your models here.

admin.site.register(Product)