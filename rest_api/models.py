from datetime import datetime

from django.utils import timezone
from django.db import models
from rest_framework import serializers


# Create your models here.
class Staff(models.Model):
    name = models.CharField(max_length=100, null=False, unique=True, default="TBC")

    def __str__(self):
        return f"{self.name}"


class Pen(models.Model):
    SIZE_CHOICES = [("3 x 6 feet", "3 x 6 feet"), ("5 x 6 feet", "5 x 6 feet")]
    number = models.IntegerField(unique=True, null=False, primary_key=True)
    size = models.CharField(max_length=100, null=False, choices=SIZE_CHOICES)
    created_date = models.DateTimeField(default=timezone.now)
    modified_date = models.DateTimeField(auto_now=True)
    responsible = models.ForeignKey(Staff, to_field='name', on_delete=models.CASCADE, default="TBC")

    def __str__(self):
        return f"Pen {self.number}"

    class Meta:
        managed = True
        db_table = 'pen_numbers'
        verbose_name_plural = 'Snails Pen Structure'


class Specie(models.Model):
    SPECIE_CHOICES = [("AMO", "AMO"), ("AMS", "AMS"), ("AF", "AF")]
    specie = models.CharField(max_length=100, null=True, choices=SPECIE_CHOICES, unique=True)
    specieDescription = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.specie

    class Meta:
        managed = True
        db_table = 'snails_species'
        verbose_name_plural = 'Snails Species'


class SnailsInventory(models.Model):
    penNumber = models.ForeignKey(Pen, to_field='number', on_delete=models.CASCADE)
    specieType = models.ForeignKey(Specie, to_field='specie', on_delete=models.CASCADE, default="AMO")
    dateTimeRecorded = models.DateTimeField(default=timezone.now)
    totalCount = models.IntegerField(default=0)
    comments = models.TextField(null=True)

    def __str__(self):
        return f"Pen {self.penNumber.number} position @ {self.dateTimeRecorded.strftime('%H:%M:%S on %d %b %Y')}"

    class Meta:
        managed = True
        db_table = 'snails_inventory'
        verbose_name_plural = 'Snails Inventory'


class EggsInventory(models.Model):
    penNumber = models.ForeignKey(Pen, to_field='number', on_delete=models.CASCADE)
    dateTimeRecorded = models.DateTimeField(default=timezone.now)
    totalCount = models.IntegerField(default=0)
    specieType = models.ForeignKey(Specie, to_field='specie', on_delete=models.CASCADE, default="AMO",
                                   related_name='specie_type')
    comments = models.TextField(null=True)

    def __str__(self):
        return f"{self.totalCount} Eggs as at @ {self.dateTimeRecorded.strftime('%H:%M:%S on %d %b %Y')}"

    class Meta:
        managed = True
        db_table = 'eggs_inventory'
        verbose_name_plural = 'Eggs Inventory'


class SnailsActivity(models.Model):
    penNumber = models.ForeignKey(Pen, to_field='number', on_delete=models.CASCADE)
    specieType = models.ForeignKey(Specie, to_field='specie', on_delete=models.CASCADE, default="AMO")
    dateTimeRecorded = models.DateTimeField(default=timezone.now)
    totalMortalities = models.IntegerField(default=0)
    newBreederStocks = models.IntegerField(default=0)
    newEggsCollected = models.IntegerField(default=0)
    newBabySnails = models.IntegerField(default=0)  # == hatchedEggsCount
    damagedEggsCount = models.IntegerField(default=0)
    snailReshuffle = models.IntegerField(default=0)
    feedConsumptionRate = models.FloatField(default=0, null=True)
    comments = models.TextField(null=True)

    def __str__(self):
        return f"Activity on pen {self.penNumber.number} @ {self.dateTimeRecorded.strftime('%H:%M:%S on %d %b %Y')}"

    # https://stackoverflow.com/questions/51392906/update-a-table-when-other-tables-changed-in-django-orm
    # https://stackoverflow.com/a/51393145

    class Meta:
        managed = True
        db_table = 'snails_activities'
        verbose_name_plural = 'Snails Activities'


class StocksTransfer(models.Model):
    CHOICES = [("Snail", "Snail"), ("Egg", "Egg")]
    dateTimeRecorded = models.DateTimeField(default=timezone.now)
    sourcePen = models.ForeignKey(Pen, to_field='number', on_delete=models.CASCADE, related_name="source_pen")
    destinationPen = models.ForeignKey(Pen, to_field='number', on_delete=models.CASCADE)
    type = models.CharField(max_length=100, null=True, choices=CHOICES)
    quantity = models.IntegerField(default=0)
    specieType = models.ForeignKey(Specie, to_field='specie', on_delete=models.CASCADE, default="AMO")
    comments = models.TextField(null=True)

    def __str__(self):
        return f"{self.type}"

    class Meta:
        managed = True
        db_table = 'stocks_transfers'
        verbose_name_plural = 'Stocks Transfers'


class EggsActivity(models.Model):
    penNumber = models.ForeignKey(Pen, to_field='number', on_delete=models.CASCADE)
    dateTimeRecorded = models.DateTimeField(default=timezone.now)
    newEggsCollected = models.IntegerField(default=0)
    hatchedEggsCount = models.IntegerField(default=0)  # == hatchedEggsCount
    damagedEggsCount = models.IntegerField(default=0)
    comments = models.TextField(null=True)

    def __str__(self):
        return f"Activity on pen {self.penNumber.number} @ {self.dateTimeRecorded.strftime('%H:%M:%S on %d %b %Y')}"

    # https://stackoverflow.com/questions/51392906/update-a-table-when-other-tables-changed-in-django-orm
    # https://stackoverflow.com/a/51393145

    class Meta:
        managed = True
        db_table = 'eggs_activities'
        verbose_name_plural = 'Eggs Activities'
