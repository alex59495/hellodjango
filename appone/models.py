from django.db import models

# Create your models here.
class Album(models.Model):
  name = models.CharField(max_length=255)
  artist_name = models.CharField(max_length=255)
  release_date = models.DateField(auto_now_add=True)

  def __str__(self):
    return '{} - {}'.format(self.name, self.artist_name)


class Song(models.Model):
  name = models.CharField(max_length=255)
  album = models.ForeignKey('Album', on_delete=models.CASCADE)
  duration = models.IntegerField(default=0)
  lyrics = models.TextField(blank=True)

  def __str__(self):
    return '{} - {}'.format(self.name, self.duration)


class Company(models.Model):
  name = models.CharField(max_length=255)

class Department(models.Model):
  name = models.CharField(max_length=255)

class Employee(models.Model):
  company = models.ForeignKey('Company', on_delete=models.CASCADE)
  department = models.ForeignKey('Department', on_delete=models.CASCADE)
  name = models.CharField(max_length=255)
  age = models.IntegerField()
  salary = models.DecimalField(max_digits=6, decimal_places=2)

  def __str__(self):
    return '{} - {} - {} - {} - {}'.format(
      self.name, 
      self.company,
      self.department,
      self.age,
      self.salary
      )

