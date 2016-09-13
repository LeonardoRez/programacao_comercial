from django.http import HttpResponse


def index(request):
    return HttpResponse("Esta e a pagina index de aluguel")
