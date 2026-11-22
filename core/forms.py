from django import forms
from .models import ContactMessage


class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ["name", "email", "message"]
        widgets = {
            "name": forms.TextInput(attrs={"placeholder": "Your name", "aria-label": "Your name"}),
            "email": forms.EmailInput(attrs={"placeholder": "Your email", "aria-label": "Your email"}),
            "message": forms.Textarea(attrs={"placeholder": "What would you like to build?", "aria-label": "Message", "rows": 4}),
        }
