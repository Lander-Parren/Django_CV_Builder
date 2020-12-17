from django.shortcuts import render
from django.http import HttpResponse
import requests

def html_head():
    return('''
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.5.3/dist/css/bootstrap.min.css" integrity="sha384-TX8t27EcRE3e/ihU7zmQxVncDAy5uIKz4rEkgIXeMed4M0jlfIDPvg6uqKI2xXr2" crossorigin="anonymous">
            <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
            <title>CV Builder</title>
        </head>
    ''')

def html_nav():
    return('''
        <nav class="navbar navbar-dark bg-dark">
            <span class="navbar-brand mb-0 h1">FossCvBuilder</span>
        </nav>
    ''')

def html_body():
    return('''
        <body>
            '''+ html_nav() +'''
        </body>
    ''')

def index(request):
    return HttpResponse(html_head() + html_body())
