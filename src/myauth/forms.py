from django import forms


class UserLoginForm(forms.Form):
    username = forms.CharField(label="نام کاربری", widget=forms.TextInput(
        attrs={"class": "LoginPageField"}))
    password = forms.CharField(label="رمز عبور", widget=forms.PasswordInput(
        attrs={"class": "LoginPageField"}))
