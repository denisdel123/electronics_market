from django import forms

from marketApp.models import Product, Category, Version


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'photo': forms.FileInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'price': forms.NumberInput(attrs={'class': 'form-control'}),
            'in_stock': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'country': forms.TextInput(attrs={'class': 'form-control'}),
        }

    def clean_name(self):
        forbidden_words = ['казино', 'криптовалюта', 'крипта', 'биржа',
                           'дешево', 'бесплатно', 'обман', 'полиция', 'радар']
        cleaned_data = self.cleaned_data['name']
        for word in forbidden_words:
            if word in cleaned_data.lower():
                raise forms.ValidationError('В названии товара не допустимо использования слова: {}'.format(word))
        return cleaned_data

    def clean_description(self):
        forbidden_words = ['казино', 'криптовалюта', 'крипта', 'биржа',
                           'дешево', 'бесплатно', 'обман', 'полиция', 'радар']
        cleaned_data = self.cleaned_data['description']
        for word in forbidden_words:
            if word in cleaned_data.lower():
                raise forms.ValidationError('В описании товара не допустимо использования слова: {}'.format(word))
        return cleaned_data


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'photo': forms.FileInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
        }


class VersionForm(forms.ModelForm):
    class Meta:
        model = Version
        fields = '__all__'
        widgets = {
            'number_version': forms.TextInput(attrs={'class': 'form-control'}),
            'name_version': forms.FileInput(attrs={'class': 'form-control'}),
            'is_active': forms.Textarea(attrs={'class': 'form-control'}),
        }
