from django import forms
from .widgets import CustomClearableFileInput
from .models import Product, Category, Colour, Comment


class ProductForm(forms.ModelForm):
    '''Allows Superuser to add products to site'''
    class Meta:
        model = Product
        fields = '__all__'

    image = forms.ImageField(label='Image', required=False, widget=CustomClearableFileInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        friendly_names = [(c.id, c.get_friendly_name()) for c in categories]

        self.fields['category'].choices = friendly_names
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'


class ColourForm(forms.ModelForm):
    '''Allows Superuser to add colours to site'''
    class Meta:
        model = Colour
        fields = '__all__'

    image = forms.ImageField(label='Image', required=False, widget=CustomClearableFileInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        products = Product.objects.all()
        print(products)
        product_names = [(p.id, p.get_name()) for p in products]

        self.fields['product'].choices = product_names
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'


class CommentForm(forms.ModelForm):
    ''' Allows users to leave comments on site '''
    class Meta:
        model = Comment
        fields = ('name', 'body')
        widgets = {
            'name': forms.TextInput(attrs={"class": "col-sm-12"}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
        }