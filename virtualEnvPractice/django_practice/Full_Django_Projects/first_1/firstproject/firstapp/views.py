from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    # create simple html page as a string
    template = "<html>" \
                "This is your first view" \
                "</html>"

    return HttpResponse(content=template)


