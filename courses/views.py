from django.shortcuts import render


# HTTP METHODS
def my_fbv(request, *args, **kwargs):
    print(request.method)
    return render(request, 'about.html', {})
