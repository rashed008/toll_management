from django.db import models
from django.utils import timezone


class tollcounter(models.Model):
  counter_no = models.CharField(max_length = 80,primary_key=True)
  counter_rate = models.CharField(max_length = 50)

  def __unicode__(self):
      return '%s' % self.counter_no
  def get_absolute_url(self):
      return '%s' % self.counter_no 




class TollTransaction(models.Model):
  counterno = models.ForeignKey("tollcounter")
  Registration_no = models.CharField(max_length = 50)
  counter_rate = models.CharField(max_length = 50)
  Date_time= models.DateTimeField(default=timezone.now)

  def __unicode__(self):
      return '%s' % self.counter_no
  def get_absolute_url(self):
      return '%s' % self.counter_no



class Accounts(models.Model):
  Registration_no = models.CharField(max_length=50)
  Payments = models.CharField(max_length = 80)
  Receive = models.CharField(max_length = 50)
  Date_time= models.DateTimeField(default=timezone.now)
  Balance = models.CharField(max_length = 80)

  def __unicode__(self):
      return '%s' % self.Payments
  def get_absolute_url(self):
      return '%s' % self.Payments
