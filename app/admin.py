from django.contrib import admin
from .models import Product, College, Course, Student, User

# Register your models here.

admin.site.register(Product)
admin.site.register(College)
admin.site.register(Course)
admin.site.register(Student)
admin.site.register(User)
