from django import forms
from .models import ShippingDetail


class ShippingForm(forms.ModelForm):
    address = forms.CharField(widget=forms.Textarea(attrs={'rows':3}))
    email = forms.CharField(widget=forms.EmailInput(attrs={'id':'email'}))

    class Meta: 
        model = ShippingDetail
        fields = ['fullname','contactno','email','address','city','state','zipcode']
