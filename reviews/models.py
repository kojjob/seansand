from django.db import models

class Review(models.Model):
  user = models.ForeignKey('users.User', on_delete=models.CASCADE)
  room = models.ForeignKey('rooms.Room', on_delete=models.CASCADE)
  review = models.TextField()
  accuracy = models.IntegerField()
  communication = models.IntegerField()
  cleanliness = models.IntegerField()
  location = models.IntegerField()
  check_in = models.IntegerField()
  value = models.IntegerField()

  def __str__(self):
    return f"{self.review} - {self.room}"