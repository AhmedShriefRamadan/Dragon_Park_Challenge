from rest_framework import generics
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework import status

from .serializers import DragonSerializer, DragonLocationSerializer, DragonFedSerializer,   ZoneSerializer
from .models import Dragon, DragonLocation, DragonFed, Zone
from actions.utils import create_action

class DragonListCreateAPIView(generics.ListCreateAPIView):
    queryset = Dragon.objects.all()
    serializer_class = DragonSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        action = self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        all_data = {
            'kind': action.kind,
            'Data Saved':serializer.data
        }
        return Response(all_data, status=status.HTTP_201_CREATED, headers=headers,)

    def perform_create(self, serializer):
        dragon_save = serializer.save()
        dragon = get_object_or_404(Dragon, name=dragon_save.name)
        location = get_object_or_404(Zone, column='A', row=0)
        time = dragon_save.time
        DragonLocation.objects.create(dragon=dragon_save,
                                        location=location,
                                        time=time)
        DragonFed.objects.create(dragon=dragon, time=time)
        action = create_action('dragon_added', dragon_save)
        return action
    
class DragonDestroy(generics.DestroyAPIView):
    queryset = Dragon.objects.all()
    serializer_class = DragonSerializer

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        action = create_action('dragon_removed', instance)
        self.perform_destroy(instance)
        data = {
            'kind': action.kind,
            'id': action.target_id,
            'time': action.created
        }
        return Response(data=data)


class DragonLocationUpdateAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = DragonLocation.objects.all()
    serializer_class = DragonLocationSerializer



    # I implement it like that, to make user just use human readable language when he request to update location
    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        dargon_location = get_object_or_404(DragonLocation,dragon__id=kwargs['pk'])

        data=request.data
        dragon = get_object_or_404(Dragon, name=data['dragon'])
        column = data['location'][0:1]
        row = data['location'][1:]
        location = get_object_or_404(Zone, column=column, row=row)
        location_id = location.id

        new_data = {
            'dragon':dragon.id,
            'location':location_id,
            'time':data['time']
        }

        serializer = self.get_serializer(dargon_location, data=new_data, partial=partial)
        serializer.is_valid(raise_exception=True)
        instance=serializer.save()
        action = create_action('dragon_location_updated', instance)

        all_data = {
            'kind':action.kind,
            'Data': serializer.data
        }
        return Response(all_data)


class DragonFedUpdateAPIView(generics.UpdateAPIView):
    queryset = DragonFed.objects.all()
    serializer_class = DragonFedSerializer

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)

        dragon = get_object_or_404(DragonFed, dragon__id=kwargs['pk'])

        serializer = self.get_serializer(dragon, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        instance = serializer.save()
        action = create_action('dragon fed', instance)
        all_data = {
            'kind': action.kind,
            'Data': serializer.data
        }
        return Response(all_data)
    



class ZoneUpdateAPIView(generics.UpdateAPIView):
    queryset = Zone.objects.all()
    serializer_class = ZoneSerializer




@api_view(['GET'])
def check_zone(request):
    zones = Zone.objects.all()
    data = {}
    for zone in zones:
        if not zone.dragon_zone.exists() and zone.is_need_maintaine:
            data[zone.get_zone] = True
        else:
            data[zone.get_zone] = False
    
    return Response(data)





