from django.http import HttpResponse
def page_view(request):
    html='<h1>test</h1>'
    return HttpResponse(html)