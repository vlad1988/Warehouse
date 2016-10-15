from django.shortcuts import render

class MainView():
    def main_page(request):
        return render(request, 'main.html')
