from django.shortcuts import render


# Create your views here.
def data_render(request):
    data='this is our assumption'
    d={'assumption':data}

    return render(request,'data_render.html',context=d)

