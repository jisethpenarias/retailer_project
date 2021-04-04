from django.contrib import admin
from .models import Users, Shippings, Payments, Orders
# Register your models here handle models from Django admin (localhost:8000/admin)
admin.site.register(Users)
admin.site.register(Shippings)
admin.site.register(Payments)
admin.site.register(Orders)