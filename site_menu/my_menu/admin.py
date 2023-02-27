from my_menu import models
from django.contrib import admin


class MenuItemInline(admin.TabularInline):
    model = models.MenuItem

    list_display = ['menu']  # , 'uri', 'name']
    search_fields = ['menu']  # , 'uri', 'title']


class MenuAdmin(admin.ModelAdmin):
    model = models.Menu
    list_display = ['name', 'position', 'visible']
    search_fields = ['name', 'position', 'visible']

    prepopulated_fields = {'position': ('name',)}
    inlines = [MenuItemInline]


admin.site.register(models.Menu, MenuAdmin)
