# from .models import Profile
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.core.exceptions import ValidationError

# 회원가입


class RegisterForm(forms.ModelForm):
    username = forms.CharField()
    password1 = forms.CharField(widget=forms.PasswordInput())
    password2 = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ['username']

    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)
        self.fields['username'].label = "닉네임"
        self.fields['password1'].label = "비밀번호"
        self.fields['password2'].label = "비밀번호 확인"

    def clean_password2(self):
        cleaned_password1 = self.cleaned_data.get('password1', '')
        cleaned_password2 = self.cleaned_data.get('password2', '')

        if cleaned_password1 != cleaned_password2:
            raise ValidationError('두 비밀번호가 다릅니다.')


# 로그인
class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        self.fields['username'].label = ""
        self.fields['password'].label = ""

    error_messages = {
        'invalid_login': (
            "일치하는 아이디/비밀번호가 없습니다."
        ),
    }
