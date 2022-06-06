from django import forms

class Login_Form(forms.Form):
    # user_name = forms.CharField(label="用户名", min_length=3, max_length=10,widget=forms.TextInput(attrs={'placeholder':"用户名"}))
    user_account = forms.CharField(label="用户账号", min_length=3, max_length=10,widget=forms.TextInput(attrs={'placeholder':"用户账号"}))
    password = forms.CharField(label="密码", min_length=6, max_length=10,widget=forms.TextInput(attrs={'placeholder':"密码",'type':"password"}))
    remeber = forms.BooleanField(required=None)

class Register_Form(forms.Form):
    user_name = forms.CharField(label="用户名", min_length=3, max_length=10,widget=forms.TextInput(attrs={'placeholder':"用户名"}))
    user_account = forms.CharField(label="用户账号", min_length=3, max_length=10,widget=forms.TextInput(attrs={'placeholder':"用户账号"}))
    password = forms.CharField(label="密码", min_length = 6, max_length=20,widget=forms.TextInput(attrs={'placeholder':"密码",'type':"password"}))
    password_confirm = forms.CharField(label="确认密码", min_length=6, max_length=10,widget=forms.TextInput(attrs={'placeholder':"确认密码",'type':"password"}))