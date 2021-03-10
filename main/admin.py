from django.contrib import admin
from django.forms import ModelForm

from .models import *


class SofaAdminForm(ModelForm):
    VALID_RESOLUTION = (400,400)
    def __init__(self, *args, **kwargs):
        super().__init__(*args,**kwargs)
        self.fields['image'].help_text = 'Загрузите изображение размером  минимум {}x{}'.format(*self.VALID_RESOLUTION)


class SofaAdmin(admin.ModelAdmin):
    form = SofaAdminForm

admin.site.register(Category)
admin.site.register(Sofa)
admin.site.register(Table)
admin.site.register(Bed)
admin.site.register(Cart)
admin.site.register(Customer)
admin.site.register(CartProduct)


