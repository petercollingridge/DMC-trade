from django import forms


class OrderForm(forms.Form):
    name = forms.CharField(max_length=100)
    sender = forms.EmailField()
    order = forms.CharField(widget=forms.HiddenInput(), required=False)
    
