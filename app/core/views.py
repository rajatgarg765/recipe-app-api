from django.shortcuts import render # noqa

# Create your views here.
import os
from app.app import calc

from django.contrib.admin import AdminSite
from django.views.decorators.cache import never_cache

# class MyAdminSite(AdminSite):
#     @never_cache
#     def index(self, request, extra_context=None):

#         ans=    os.command("python3 /home/rajat/Documents/Django/Udemy/recipe-app-api/app/app/calc.py")

#     return 

# admin_site = MyAdminSite()