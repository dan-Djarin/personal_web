from django.shortcuts import render, HttpResponse

# Create your views here.

html_base = """
<h1>My personal web</h1>
<ul>
    <li><a href="/">Cover page</a></li>
    <li><a href="/about-me/">About</a></li>
</ul>
"""

def home(request):
    return HttpResponse(f"{html_base}<h2>Cover page</h2><p>This is the cover</p>")

def about(request):
    return HttpResponse(f"{html_base} <h2>About</h2><p>My name is Daniel and I am a programmer</p>")


