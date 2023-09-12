from django import forms

class MyForm(forms.Form):
    input_field = forms.CharField(label='EnterSomething')