from django.http import HttpResponse


def index(request):
    return HttpResponse("Esta e a pagina index de aluguel")

def agendaMes(request, mes_id):
    return HttpResponse("Esta e a agenda do mes %s." % mes_id)

def agendaSemana(request, semana_id, mes_id):
    return HttpResponse("Esta e a agenda da semana %s do mes %s." % semana_id % mes_id)
