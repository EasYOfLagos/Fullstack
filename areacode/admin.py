from django.contrib import admin
from .models import User, Food, Cart

# Register your models here.

admin.site.register(User)
admin.site.register(Food)
admin.site.register(Cart)