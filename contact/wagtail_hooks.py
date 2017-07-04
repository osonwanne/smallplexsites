from wagtail.contrib.modeladmin.options import (
    ModelAdmin, modeladmin_register)
from .models import Contact


class ContactsAdmin(ModelAdmin):
    model = Contact
    menu_label = 'Contacts'
    menu_icon = 'date'  # change as required
    menu_order = 400  # will put in 5th place (000 being 1st, 100 2nd)
    add_to_settings_menu = False  # or True to add your model to the Settings sub-menu
    list_display = ('Name', 'Email', 'Message', 'Created')
    list_filter = ('Created',)
    search_fields = ('Name', 'Email', 'Message')

# Now you just need to register your customised ModelAdmin class with Wagtail
modeladmin_register(ContactsAdmin)