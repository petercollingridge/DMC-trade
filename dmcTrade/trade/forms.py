from django import forms


class OrderForm(forms.Form):
    required_css_class = 'required'
    
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    billing_address = forms.CharField()
    delivery_address = forms.CharField()
    comments = forms.CharField(required=False)
    order = forms.CharField(widget=forms.HiddenInput(), required=False)
    