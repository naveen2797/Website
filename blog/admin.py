from django.contrib import admin
from .models import Contact,Post
# Register your models here.
@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['name','email','phone','desc']

admin.site.register(Post)
