from django.forms import (Form,
                          CharField,
                          PasswordInput,
                          EmailField)


class AddUserForm(Form):
    username = CharField(label='Nazwa użytkownika', strip=True)
    password = CharField(label='Hasło', widget=PasswordInput)
    first_name = CharField(label='Imię', strip=True, required=False)
    last_name = CharField(label='Nazwisko', strip=True, required=False)
    email = EmailField(label='Email', required=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'placeholder': 'Wymagane'})
        self.fields['password'].widget.attrs.update({'placeholder': 'Wymagane'})


class LoginUserForm(Form):
    username = CharField(label='Nazwa użytkownika', strip=True)
    password = CharField(label='Hasło', widget=PasswordInput)
