from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    # return HttpResponse("Blog Index")
    return render(request, "blog/index.html")
