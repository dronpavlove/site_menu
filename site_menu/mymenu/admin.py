from django.contrib import admin
from django_mptt_admin.admin import DjangoMpttAdmin
from .models import PodCategoryMenu, CategoryMenu


class PodCategoryMenuAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}


class CategoryMenuAdmin(DjangoMpttAdmin):
    prepopulated_fields = {"slug": ("title",)}


admin.site.register(PodCategoryMenu, PodCategoryMenuAdmin)
admin.site.register(CategoryMenu, CategoryMenuAdmin)
