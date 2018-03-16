from django.shortcuts import render

# Create your views here.
def timeline_image(request):
    return render(request, 'timeline/timeline_image.html')
