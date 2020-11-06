from django.contrib import admin

# Register your models here.
from .models import Mailbox, Template, Email


admin.site.register(Mailbox)
admin.site.register(Template)

admin.site.register(Email)