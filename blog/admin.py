from django.contrib import admin
from . import models
# Register your models here.

@admin.register(models.Topic)
class TopicAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'slug',
    )
    prepopulated_fields = {'slug': ('name',)}

class PostAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'author',
        'created',
        'updated',
        #order is typed order
    )
    list_filter = (
        'status',
        'topics'
    )
    search_fields = (
        'title',
        'author__username',
        'author__first_name',
        'author__last_name',
    )

    prepopulated_fields = {
        'slug': ('title',) #populate the field with title
    }

admin.site.register(models.Post, PostAdmin)
