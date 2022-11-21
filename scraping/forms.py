from django import forms
from .models import Product


class AddProductLinkForm(forms.ModelForm):
    add = forms.BooleanField(widget=forms.HiddenInput, initial=True)
    class Meta:
        model = Product
        fields = ("url",)
        widgets = {
            "url": forms.TextInput(attrs={"class":"form-control", "placeholder":"URL"}),
        }
        labels = {
            "url":"",
        }


    
