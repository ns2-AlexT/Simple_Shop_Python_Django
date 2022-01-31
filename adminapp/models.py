from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserChangeForm
from django.db import models
from django.forms import HiddenInput


class ShopUserUserChangeForm(UserChangeForm):
    class Meta:
        model = get_user_model()
        fields = ("username", "email", "password", "first_name", "last_name", "age", "ava")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if field_name == 'password':
                field.widget = HiddenInput()
                continue
            field.widget.attrs['class'] = f'form-control {field_name}'
