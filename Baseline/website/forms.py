from django import forms

class MyForm(forms.Form):
    title_input = forms.CharField(label='Title')
    # output_field = forms.CharField(label = 'Output', required=False)
    description_input = forms.CharField(
        label='Decription',
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control', 'style': 'width: 500px; height: 100px;'}),
    )

