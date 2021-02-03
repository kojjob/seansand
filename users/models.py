
from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
  """ Custom User Model """

  GENDER_MALE  = "male"
  GENDER_FEMALE = "female"
  GENDER_OTHER  = "other"

  GENDER_CHOICES = (
    ( GENDER_MALE, "Male"),
    (GENDER_FEMALE, "Female"),
    (GENDER_OTHER, "Other"),
  )


  LANGUAGE_ENGLISH ="en"
  LANGUAGE_FRENCH ="fr"
  LANGUAGE_SWAHILI = "sw"
  LANGUAGE_WOLOF = "wf"
  LANGUAGE_HAUSA ="ha"
  LANGUAGE_PORTUGUESE ="pe"
  LANGUAGE_SPANISH ="sp"

  LANGUAGE_CHOICES = (
    (LANGUAGE_ENGLISH, "English"),
    (LANGUAGE_FRENCH, "France"),
    (LANGUAGE_SWAHILI,  "Swahili"),
    (LANGUAGE_WOLOF,  "Wolof"),
    (LANGUAGE_HAUSA, "Hausa"),
    (LANGUAGE_PORTUGUESE, "Portuguese"),
    (LANGUAGE_SPANISH, "Spanish"),
  )

  CURRENCY_USD = "usd"
  CURRENCY_GBP = "gbp"
  CURRENCY_EUR = "eur"
  CURRENCY_GHS = "ghs"
  CURRENCY_NGN = "ngn"
  CURRENCY_XPF = "xpf"
  CURRENCY_ZAR = "zar"

  CURRENCY_CHOICES = (
    (CURRENCY_USD, "USD"),
    (CURRENCY_GBP, "GBP"),
    (CURRENCY_EUR, "EUR"),
    (CURRENCY_GHS, "GHS"),
    (CURRENCY_NGN, "NGN"),
    (CURRENCY_XPF, "XPF"),
    (CURRENCY_ZAR, "ZAR"),
  )

  avatar =  models.ImageField(blank=True)
  bio = models.TextField(default="")
  date_of_birth = models.DateField(blank=True, null=True)
  gender = models.CharField(choices=GENDER_CHOICES, max_length=10, blank=True)
  language = models.CharField(choices=LANGUAGE_CHOICES, max_length=16, blank=True)
  currency = models.CharField(choices=CURRENCY_CHOICES, max_length=3)
  superhost = models.BooleanField(default=False)
  date = models.DateField(blank=True, null=True) 