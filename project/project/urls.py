"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# from http.client import HTTPResponse
# from turtle import width
# from urllib import request, response
from urllib import response
from django.contrib import admin
from django.urls import path
from django.http import HttpResponse
import math


def my_route(request):
    response = HttpResponse("<h1>Hello World</h1>")
    return response

def rectArea(request):
    height = int(request.GET.get("height"))
    width = int(request.GET.get("width"))
    area = height * width
    response = HttpResponse(f"<h1>The area of a rectangle with the height of: {height} and width of: {width} is {area}</h1>")
    return response

def rectPeri(request):
    height = int(request.GET.get("height"))
    width = int(request.GET.get("width"))
    perimeter = (2 * height) + (2 * width)
    response = HttpResponse(f"<h1>The perimeter of a rectangle with the height of: {height} and width of {width} is {perimeter}</h1>")
    return 
    
def circleArea(request):
    radius = int(request.GET.get('radius'))
    area = math.pi * (radius ** 2)
    response = HttpResponse(f"<h1>The area of a cicle with the radius of: {radius} is {area}</h1>")
    return response

def circlePeri(request):
    radius = int(request.GET.get("radius"))
    perimeter = math.pi * (radius * 2)
    response = HttpResponse(f"<h1>The perimeter of a circle with a radius of: {radius} is {perimeter}</h1>")
    return response

# Now we will use variables

def rectangleArea(request, height, width):
    try:
        height = height
        width = width
        area = width * height
        response = HttpResponse(f"<h1>The area of a rectangle with the height of: {height} and width of: {width} is {area}</h1>")
        return response
    except:
        response = HttpResponse()
        response.status_code = 400
        return response

def rectanglePerimeter(request, height, width):
    height = height
    width = width
    perimeter = (height * 2) + (width * 2)
    response = HttpResponse(f"<h1>The perimeter of a rectangle with the height of: {height} and width of: {width} is {perimeter}</h1>")
    return response

def circArea(response, radius):
    radius = radius
    area = math.pi * (radius ** 2)
    response = HttpResponse(f"<h1>The area of a cicle with the radius of: {radius} is {area}</h1>")
    return response

def circlePerimeter(response, radius):
    radius = radius
    perimeter = math.pi * (radius * 2)
    response = HttpResponse(f"<h1>The perimeter of a circle with a radius of: {radius} is {perimeter}</h1>")
    return response

    

urlpatterns = [
    path("", my_route),
    path('admin/', admin.site.urls),
    path("rectangle/area", rectArea),
    path("rectangle/perimeter", rectPeri),
    path("circle/area", circleArea),
    path("circle/perimeter", circlePeri),
    path("rectangle/area/<int:height>/<int:width>", rectangleArea),
    path("rectangle/perimeter/<int:height>/<int:width>", rectanglePerimeter),
    path("circle/area/<int:radius>", circArea),
    path("circle/perimeter/<int:radius>", circlePerimeter)
]
