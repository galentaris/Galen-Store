from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'name': 'Galen Taris Bariqi',
        'class': 'PBP C'
    }

    return render(request, "main.html", context)