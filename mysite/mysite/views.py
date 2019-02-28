from django.shortcuts import render

def lodge(request):
    return render(request, 'lodge.html', context={})


def contact(request):
    return render(request, 'contact.html', context={})
