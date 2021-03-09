from django.contrib import admin

# Register your models here.

from .models import *


admin.site.register(Category)
admin.site.register(Sofa)
admin.site.register(Table)
admin.site.register(Bed)
admin.site.register(Cart)
admin.site.register(Customer)
admin.site.register(CartProduct)


