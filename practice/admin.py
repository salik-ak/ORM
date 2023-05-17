from django.contrib import admin
from .models import Entry
from .models import Blog
from .models import Author


# Register your models here.
admin.site.register(Entry)
admin.site.register(Blog)
admin.site.register(Author)