from django.shortcuts import render

# Create your views here.
def tutorial_list(request):
    return render(request, 'tutorials/tutorial_list.html')
