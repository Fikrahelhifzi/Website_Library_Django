from django.contrib import admin


# Register your models here.

from .models import Book,Library,Rent,Student,Study_programs,University

admin.site.register(Book)
admin.site.register(Library)
admin.site.register(Rent)
admin.site.register(Student)
admin.site.register(Study_programs)
admin.site.register(University)
