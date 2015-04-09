from django import forms
from models import Contact
class ContactForm(forms.ModelForm):

    Email = forms.EmailField(label="Your Email id" , required=True)


    class Meta:
        model = Contact
        fields = ('first_name','last_name')
