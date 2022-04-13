from django.contrib import admin
from .models import Expense, feedback, rg_signup

# Register your models here.
admin.site.register(Expense)
admin.site.register(rg_signup)
admin.site.register(feedback)