from django.contrib import admin
from homepage.models import UserProfileInfo, User, CalculatePrice

# Register your models here.
admin.site.register(UserProfileInfo)
admin.site.register(CalculatePrice)