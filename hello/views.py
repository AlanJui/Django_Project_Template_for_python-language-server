import re

from django.http import HttpResponse
from django.utils.timezone import datetime


def home(request):
    return HttpResponse("Hello, Django!")


def hello_there(request, name):
    now = datetime.now()
    formatted_now = now.strftime("%A, %d %B, %Y ad %X")

    # Filter the name argument to letters only using regular expressions. URL arguments
    # can contain arbitrary text, so we restrict to safe characters only.
    match_object = re.match("[a-zA-Z]+", name)

    if match_object:
        clean_name = match_object.group(0)
    else:
        clean_name = "friend"

    content = "Hello there, " + clean_name + "! It's " + formatted_now
    return HttpResponse(content)