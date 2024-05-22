from django.http import HttpResponse

# Create your views here.
def index(request):
  return HttpResponse('<h1>Django and Python Chat App</h1><iframe src="https://deadsimplechat.com/0J6Nv6aDa" width="100%" height="600px"></iframe>')
