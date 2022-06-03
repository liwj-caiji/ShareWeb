from django import forms

class Article_Create_Form(forms.Form):
    #提交article不需要用户名
    title  = forms.CharField( label="标题", max_length=30,  widget=forms.TextInput(attrs={'placeholder':"标题"}))
    body   = forms.CharField( widget=forms.Textarea)

class Article_Search_Form(forms.Form):
    search_content = forms.CharField( label="搜所内容", max_length=30, widget=forms.TextInput(attrs={'place_holder':"搜索内容"}))
    search_type = forms.ChoiceField( label="搜索类型",choices=[('article_title','title'),('article_author','author')])