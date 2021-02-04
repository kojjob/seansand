from django.db import models
from django_countries.fields import CountryField
from core import models as core_models
from users import models as user_models



class AbstractItem(core_models.TimeStampedModel):
  
  """ Abstract Item """

  name = models.CharField(max_length=100)
  subtitle = models.CharField(max_length=100, blank=True) 
  class Meta:
    abstract = True

  def __str__(self):
    return self.name

class RoomType(AbstractItem):  
  """ Room Type Object Definition """
  pass 
  class Meta:
    verbose_name = ("Room Type")
    ordering = ["name"] #name => alphabetical,  created => date

class Amenity(AbstractItem):  
  """ Amenity Model Definition """
  pass 
  class Meta:
    verbose_name_plural = 'Amenities' # pluralise
class Facility(AbstractItem):  
  """ Facilities Model Definition """
  pass 
  class Meta:
    verbose_name_plural = 'Facilities'
class HouseRule(AbstractItem):  
  """ House Rules Model Definition """
  pass 

class Photo(core_models.TimeStampedModel):
  """ Photo Model Definition """
  caption = models.CharField(max_length=100)
  file = models.ImageField(null=True)
  room = models.ForeignKey("Room", on_delete=models.CASCADE)

class Room(core_models.TimeStampedModel):  

  """ Room Model Definition """

  name = models.CharField(max_length=255, null=True)
  description = models.TextField(null=True)
  country = CountryField(null=True)
  city = models.CharField(max_length=80, null=True)
  price = models.IntegerField(null=True) 
  address = models.CharField(max_length=255, null=True)
  guests = models.IntegerField(null=True)
  beddrooms = models.IntegerField(null=True)
  beds = models.IntegerField(null=True)
  baths = models.IntegerField(null=True)
  check_in = models.DateTimeField(null=True)
  check_out = models.DateTimeField(null=True)
  instant_book = models.BooleanField(default=False)
  host = models.ForeignKey(user_models.User, on_delete=models.CASCADE, null=True)
  room_type = models.ManyToManyField(RoomType, null=True)
  amenities = models.ManyToManyField(Amenity)
  facilities = models.ManyToManyField(Facility)
  house_rules = models.ManyToManyField(HouseRule)

  def __str__(self):
    return self.name
