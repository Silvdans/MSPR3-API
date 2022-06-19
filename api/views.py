import json
from django.db.models import Sum
from rest_framework.generics import RetrieveAPIView, UpdateAPIView
from rest_framework import status
from rest_framework.response import Response

from api.models import  Demande, Detaildemande, Modele, Tournee, Typedechet, Ville
# Create your views here.

class WasteList(RetrieveAPIView):
    
    def get(self, request):
        data = dict(request.GET)
        demandes = Demande.objects.filter(datedemande__range = [data['datedemande'][0], data['dateenlevement'][0]])
        listeDemande = []
        for demande in demandes:
            listeDemande.append(Detaildemande.objects.filter(nodemande=demande.nodemande,noville=Ville.objects.get(noville=data['ville'][0]), notypedechet=Typedechet.objects.get(notypedechet=data['notypedechet'][0])).aggregate(Sum('quantiteenlevee')))
        somme = 0
        for data in listeDemande:
            if(data['quantiteenlevee__sum']):
                somme += data['quantiteenlevee__sum']
        return Response(data=somme,status=status.HTTP_200_OK)

class WasteNational(RetrieveAPIView):
    def get(self,request):
        data = dict(request.GET)
        demandes = Demande.objects.filter(datedemande__range = [data['datedemande'][0], data['dateenlevement'][0]])
        listeDemande = []
        for demande in demandes:
            listeDemande.append(Detaildemande.objects.filter(nodemande=demande.nodemande, notypedechet=Typedechet.objects.get(notypedechet=data['notypedechet'][0])).aggregate(Sum('quantiteenlevee')))

        somme = 0
        for data in listeDemande:
            if(data['quantiteenlevee__sum']):
                somme += data['quantiteenlevee__sum']

        return Response(data=somme,status=status.HTTP_200_OK)
    

class MakeDemandInTrip(UpdateAPIView):
    def put(self, request):
        data = json.loads(request.body) 
        demands_to_make_in_trip = Demande.objects.filter(notournee=None)
        demands = []
        for item in demands_to_make_in_trip:
            demands.append(item.nodemande)
        count = len(Tournee.objects.filter(noimmatric=Tournee.objects.get(pk=data['tournee']).noimmatric))
        modele = Modele.objects.filter(camion=Tournee.objects.get(pk=data['tournee']).noimmatric).first()
        if count > modele.maxenlevement:
            return Response(data={"message":"Le tournee ne peux pas accepter plus de demande: le camion ne peut plus assurer d'enlevement de plus", "journal":json.dumps(demands)},status=status.HTTP_400_BAD_REQUEST)
        for demand in demands_to_make_in_trip:
            d = Demande.objects.get(pk=demand.nodemande)
            d.notournee = Tournee.objects.get(pk=data["tournee"])
            d.save()
        return Response(status=status.HTTP_200_OK)
