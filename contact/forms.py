from django import forms
from .models import Contact

# our new form
class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = [
            'Name',
            'Email',
            'Message'
            ]

    # the new bit we're adding
    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        self.fields['Name'].label = "Your Name:"
        self.fields['Email'].label = "Your Email:"
        self.fields['Message'].label = "Message:"
