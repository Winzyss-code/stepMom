from django.shortcuts import render


def index(request):
    title = 'Head Page'
    context = {
        'title' = title,
    }
    return render(request,'index.html',context)

def products(request):
    return render(request,'products.html')