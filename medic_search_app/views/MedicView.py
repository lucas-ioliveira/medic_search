from django.http import HttpResponse
from medic_search_app.models import Profile

def list_medic_view(request):
    name = request.GET.get('name')
    speciality = request.GET.get('speciality')
    neighborhood = request.GET.get("neighborhood")
    city = request.GET.get("city")
    state = request.GET.get("state")
    medics = Profile.objects.all()
    print(medics)
    return HttpResponse('Listagem de 1 ou mais méidicos')
