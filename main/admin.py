from django.contrib import admin
from .models import *

class BookAdmin(admin.ModelAdmin):
    search_fields = ('title',)
   

class UserAdmin(admin.ModelAdmin):
    search_fields = ('username',)

admin.site.register(Book, BookAdmin)
admin.site.register(User, UserAdmin)