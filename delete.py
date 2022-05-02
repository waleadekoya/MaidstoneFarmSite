# from django.db import models
#
#
# # Create your models here.
#
# class Pen(models.Model):
#     SIZE_CHOICES = [("3 x 6 feet", "3 x 6 feet"), ("5 x 6 feet", "5 x 6 feet")]
#     number = models.IntegerField(unique=True, null=False, primary_key=True)
#     size = models.CharField(max_length=100, null=False, choices=SIZE_CHOICES)
#
#     class Meta:
#         managed = True
#         db_table = 'pen_numbers'
#
#
# class SnailsCurrentInventory(models.Model):
#     SPECIE_CHOICES = [("AMO", "AMO"), ("AMS", "AMS")]
#     penNumber = models.ForeignKey(Pen, to_field='number', on_delete=models.CASCADE)
#     species = models.CharField(max_length=100, null=True, choices=SPECIE_CHOICES)
#     dateRecorded = models.DateField()
#     totalCount = models.IntegerField()
#
#     class Meta:
#         managed = True
#         db_table = 'snails_current_totals'
#
#
# class SnailsActivity(models.Model):
#     SPECIE_CHOICES = [("AMO", "AMO"), ("AMS", "AMS")]
#     penNumber = models.ForeignKey(Pen, to_field='number', on_delete=models.CASCADE)
#     species = models.CharField(max_length=100, null=True, choices=SPECIE_CHOICES)
#     dateRecorded = models.DateField()
#     totalMortalities = models.IntegerField()
#     newBreederStocks = models.IntegerField()
#     newEggsCollected = models.IntegerField()
#     newBabySnails = models.IntegerField()
#     hatchedEggsCount = models.IntegerField()
#     damagedEggsCount = models.IntegerField()
#     snailReshuffle = models.IntegerField()
#
#     class Meta:
#         managed = True
#         db_table = 'snails_activities'
#
# from django.contrib import admin
# from .models import SnailsActivity, SnailsCurrentInventory, Pen
#
#
# # Register your models here.
#
# admin.site.register(SnailsActivity)
# admin.site.register(SnailsCurrentInventory)
# admin.site.register(Pen)