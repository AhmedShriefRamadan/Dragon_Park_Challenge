from django.db import models
from datetime import timedelta,datetime
import pytz

class Dragon(models.Model):
    name = models.CharField(max_length=100,unique=True)
    species = models.CharField(max_length=50)
    gender = models.CharField(max_length=10)
    digestion_period = models.PositiveIntegerField()
    herbivore = models.BooleanField()
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.name




class Park(models.Model):
    name = models.CharField(max_length=20)
    
    def __str__(self) -> str:
        return self.name
    


class Zone(models.Model):
    column = models.CharField(max_length=1)
    row = models.PositiveSmallIntegerField()
    park = models.ForeignKey(Park,
                                related_name='park_zone',
                                on_delete=models.CASCADE)
    maintainence_time = models.DateTimeField(default=datetime.now())

    def __str__(self) -> str:
        return f'{self.column}{self.row} with id -> {self.id}'
    
    @property
    def get_zone(self):
        return f'{self.column}{self.row}'
    
    @property
    def is_need_maintaine(self):
        next_maintenance = self.maintainence_time + timedelta(days=30)
        utc=pytz.UTC
        return utc.localize(datetime.now()) >= next_maintenance





class DragonLocation(models.Model):
    dragon = models.OneToOneField(Dragon,
                                related_name='dragon_location',
                                on_delete=models.CASCADE,
                                primary_key=True)
    location = models.ForeignKey(Zone,
                                    on_delete=models.CASCADE,
                                    related_name='dragon_zone')
    time = models.DateTimeField()


    def __str__(self) -> str:
        return f'{self.location}'
    

class DragonFed(models.Model):
    dragon = models.OneToOneField(Dragon,
                                    related_name='time_dragon_fed',
                                    on_delete=models.CASCADE)
    time = models.DateTimeField()

    @property
    def digestion_period_end(self):
        return self.time + timedelta(hours=self.dragon.digestion_period)
    
    def __str__(self) -> str:
        return f'{self.dragon}'