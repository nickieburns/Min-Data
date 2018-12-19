from django.shortcuts import render

# Create your views here.
def j_notebooks(request):
	return render(request, 'jupyterNb/j_notebooks.html')