from django.urls import path
from medic_search_app.views.MedicView import list_medic_view

urlpatterns = [
    path('', list_medic_view, name='medics')
]
