from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . import models

# Register your models here.
@admin.register(models.User)
class CustomUserAdmin(UserAdmin):

  """Custom UserAdmin"""

  fieldsets = UserAdmin.fieldsets + (
    (
      'Custom Profile',
      {
        "fields": (
          "avatar",
          "gender",
          "bio",
          "date_of_birth",
          "language",
          "currency",
          "superhost"

        )
      },
    ),
  )
