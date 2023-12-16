from django.shortcuts import render

# Create your views here.

def design_ltda_index(request):
    return render(
        request,
        "index.html"
    )

def design_ltda_elemento_design.html(request):
    return render(
        request,
        "elementos_design.html"
    )

def design_ltda_contato.html(request):
    return render(
        request,
        "contato.html"
    )