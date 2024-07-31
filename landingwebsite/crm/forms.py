from django import forms


class OrderForm(forms.Form):
    name = forms.CharField(max_length=200,
                           widget=forms.TextInput(attrs={'class': 'css_input'}))
    # required=False, чтобы указать можно ли оставить поле пустым
    phone = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'class': 'css_input'}))