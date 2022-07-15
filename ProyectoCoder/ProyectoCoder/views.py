from django.http import HttpResponse

def inicio (request):
    pagina = "Pagina Blanca"
    return HttpResponse(pagina)