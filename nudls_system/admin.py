from django.contrib import admin

from .models import Dragon, DragonLocation, Park, Zone, DragonFed

admin.site.register(Dragon)
admin.site.register(DragonLocation)
admin.site.register(Park)
admin.site.register(Zone)
admin.site.register(DragonFed)