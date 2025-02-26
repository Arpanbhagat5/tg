from django.contrib import admin
from users.models import CustomUser

# Register your models here.
# can check created users in the admin panel: http://localhost:8000/admin/login/?next=/admin/
admin.site.register(CustomUser)
