from django.shortcuts import render

def essays(request):
	return render(request, 'essay/essays.html')