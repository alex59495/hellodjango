from django.db import models

# Create your models here.
class Device(models.Model):
  OS_ANDROID = 'android'
  OS_IOS = 'ios'
  FAC_PHONE = 'phone'
  FAC_TABLET = 'tablet'

  OS_CHOICES = [
    (OS_IOS, 'iOS'),
    (OS_ANDROID, 'Android')
    ]
  FACTORS_CHOICES = [
    (FAC_PHONE, 'Phone'),
    (FAC_TABLET, 'Tablet')
    ]

  os = models.CharField(max_length = 7, choices = OS_CHOICES, default=OS_ANDROID)
  form_factor = models.CharField(max_length = 6, choices = FACTORS_CHOICES, default=FAC_PHONE)
  model = models.CharField(max_length = 100)
  created_at = models.DateTimeField(auto_now_add = True)
  description = models.TextField(blank=True)
  enabled = models.BooleanField(default=False)

  def __str__(self):
    return "id : {id} - OS : {os} - Type : {type} - Modele: {model} - Crée : {created_at} -  Description : {description} - enanled: {enabled}".format(
      id = self.id, 
      os = self.get_os_display(),
      type = self.get_form_factor_display(), 
      model = self.model, 
      created_at = self.created_at, 
      description = self.description, 
      enabled = self.enabled)