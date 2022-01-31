from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from django.forms import HiddenInput, ModelForm

from authapp.forms import ShopUserUserChangeForm
from authapp.models import ShopUser
from mainapp.models import ProductCategory, Product


class AdminShopUserUpd(ShopUserUserChangeForm):
    class Meta:
        model = get_user_model()
        fields = ("username", "email", "password", "first_name", "last_name", "age", "ava", "is_superuser", "is_staff",
                  "is_active")


class ProductCatCreatForm(ModelForm):
    class Meta:
        model = ProductCategory
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = f'form-control {field_name}'


class ProductUpdForm(ModelForm):
    class Meta:
        model = Product
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = f'form-control {field_name}'
            if field_name == 'category':
                field.widget = HiddenInput()
