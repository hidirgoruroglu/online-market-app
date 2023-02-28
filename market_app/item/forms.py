from django import forms

from .models import Item

INPUT_CLASSES = 'w-full py-4 px-6 rounded-xl border'

class NewItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ("name","description","price","category","image","is_sold")

        widgets = {
            'category':forms.Select(attrs={
                'class':INPUT_CLASSES
            }),
            'name':forms.TextInput(attrs={
                "placeholder": "Ürün ismi",
                'class':INPUT_CLASSES
            }),
            'description':forms.Textarea(attrs={
                "placeholder": "Ürün açıklaması",
                'class':INPUT_CLASSES
            }),
            'price':forms.TextInput(attrs={
                "placeholder": "Ürün fiyatı",
                'class':INPUT_CLASSES
            }),
            'image':forms.FileInput(attrs={
                'class':INPUT_CLASSES
            }),
            'is_sold':forms.CheckboxInput(attrs={
                'class':INPUT_CLASSES
            }),
        }

class EditItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ("name","description","price","image","is_sold")
        widgets = {
            'name':forms.TextInput(attrs={
                "placeholder": "Ürün ismi",
                'class':INPUT_CLASSES
            }),
            'description':forms.Textarea(attrs={
                "placeholder": "Ürün açıklaması",
                'class':INPUT_CLASSES
            }),
            'price':forms.TextInput(attrs={
                "placeholder": "Ürün fiyatı",
                'class':INPUT_CLASSES
            }),
            'image':forms.FileInput(attrs={
                'class':INPUT_CLASSES
            }),
            'is_sold':forms.CheckboxInput(attrs={
                'class':INPUT_CLASSES
            }),
        }