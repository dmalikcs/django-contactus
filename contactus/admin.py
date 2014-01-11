from django.contrib import admin
from contactus.models import ContactUs


class ContactUsAdmin(admin.ModelAdmin):
    fields = (('name', 'email', 'status'), 'message')
    list_display = ('name', 'email', 'status',)
    list_filter = ('status', )
    search_fields = ('name', 'email', )

admin.site.register(ContactUs, ContactUsAdmin)
