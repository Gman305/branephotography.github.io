from django.contrib import admin
from django.core.exceptions import ValidationError
from BranePhr.models import *

# Register your models here.

class BranePhotographyAdmin(admin.ModelAdmin):
    def get_queryset(self, request):
        qs=super(BranePhotographyAdmin, self).get_queryset(request)
        return qs

    def has_add_permission(self, request):
        if request.user.is_superuser:
            return True
        else:
            return False

    def has_delete_permission(self, request, obj=None):
        if request.user.is_superuser:
            return True
        else:
            return False

    def has_change_permission(self, request, obj=None):
        if request.user.is_superuser:
            return True
        else:
            return False


class ImageAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        if request.user.is_superuser:
            return True
        else:
            return False

    def has_delete_permission(self, request, obj=None):
        if request.user.is_superuser:
            return True
        else:
            return False

    def has_change_permission(self, request, obj=None):
        if request.user.is_superuser:
            return True
        else:
            return False

class CarouselAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        if request.user.is_superuser:
            return True
    def has_delete_permission(self, request, obj=None):
        if request.user.is_superuser:
            return True

    def has_change_permission(self, request, obj=None):
        if request.user.is_superuser:
            return True

admin.site.register(Brane, BranePhotographyAdmin)
admin.site.register(Images, ImageAdmin)
admin.site.register(Carousel, CarouselAdmin)