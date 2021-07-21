from django.contrib import admin
from .models import djangoClasses

# have to register the admin before it can be launched.

admin.site.register(djangoClasses)