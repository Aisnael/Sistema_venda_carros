
from django.shortcuts import render

# função para view de carros.
def cars_view(request):
    return render(request, 'cars.html')
