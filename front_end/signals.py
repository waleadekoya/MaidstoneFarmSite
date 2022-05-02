# from django.db.models.signals import post_save, pre_save
# from django.dispatch import receiver
# from django.utils import timezone
# from datetime import timedelta
#
# # from .models import SnailsActivity, SnailsInventory, Pen, EggsInventory, Specie, StocksTransfer
# from rest_api.models import SnailsActivity, SnailsInventory, Pen, EggsInventory, Specie, StocksTransfer
#
#
# def get_time_stamp(instance_object, instance):
#     return instance_object.dateTimeRecorded + timedelta(minutes=1) \
#         if instance.dateTimeRecorded <= instance_object.dateTimeRecorded else instance.dateTimeRecorded
#
#
# def create_egg_instance(pen_no: int, instance, instance_object):
#     EggsInventory.objects.create(penNumber=Pen.objects.get(number=pen_no),
#                                  dateTimeRecorded=get_time_stamp(instance_object, instance),
#                                  specieType=Specie.objects.get(specie="AMO"),
#                                  totalCount=instance_object.totalCount,
#                                  comments=instance.comments)
#
#
# def create_snail_instance(instance, instance_object, is_transfer=False, pen_no: int = None):
#     SnailsInventory.objects.create(penNumber=Pen.objects.get(number=pen_no) if is_transfer else instance.penNumber,
#                                    specieType=instance.specieType,
#                                    dateTimeRecorded=get_time_stamp(instance_object, instance),
#                                    totalCount=instance_object.totalCount,
#                                    comments=instance.comments)
#
#
# @receiver(post_save, sender=SnailsActivity)
# def update_inventory_record(sender, instance=None, created=False, **kwargs):
#     # when a new record is persisted, do the following:
#     # 1. update SnailsInventory table totalCount with newBreederStocks, totalMortalities, newBabySnails.
#     # 2. update the dateRecorded, and specieType in SnailsInventory table.
#     # 3. update the EggsInventory table with newEggsCollected, newBabySnails, and the dateRecorded
#     # Get the latest record for the pen number by dateTimeRecorded
#     if kwargs.get('created', True):
#         adjustmentSign = "+" if instance.snailReshuffle >= 0 else "-"
#         try:
#
#             latestRecordByPen = SnailsInventory.objects \
#                 .filter(penNumber=Pen.objects.get(number=instance.penNumber_id)) \
#                 .order_by("-id")[0]
#             latestTimestamp = latestRecordByPen.dateTimeRecorded.strftime("%Y-%m-%d %H:%M:%S")
#             instance.comments = f"{latestRecordByPen.totalCount} snails b/f @ {latestTimestamp} " \
#                                 f"+ {instance.newBreederStocks} newBreederStocks " \
#                                 f"- {instance.totalMortalities} totalMortalities " \
#                                 f"+ {instance.newBabySnails} newBabySnails " \
#                                 f"{adjustmentSign} {abs(instance.snailReshuffle)} stockAdjustments = "
#             latestRecordByPen.totalCount += instance.newBreederStocks
#             latestRecordByPen.totalCount -= instance.totalMortalities
#             latestRecordByPen.totalCount += instance.newBabySnails
#             latestRecordByPen.totalCount += instance.snailReshuffle
#
#             instance.comments += str(latestRecordByPen.totalCount)
#             if created:
#                 create_snail_instance(instance, latestRecordByPen)
#                 instance.comments = ""
#         except IndexError as e:
#             # No record exist for this pen - New entry
#             instance.totalCount = instance.newBreederStocks - instance.totalMortalities + instance.newBabySnails + instance.snailReshuffle
#             instance.comments = f"{instance.newBreederStocks} newBreederStocks " \
#                                 f"- {instance.totalMortalities} totalMortalities " \
#                                 f"+ {instance.newBabySnails} newBabySnails " \
#                                 f"{adjustmentSign} {abs(instance.snailReshuffle)} stockAdjustments = {instance.totalCount}"
#             if created:
#                 SnailsInventory.objects.create(penNumber=instance.penNumber,
#                                                specieType=instance.specieType,
#                                                dateTimeRecorded=instance.dateTimeRecorded,
#                                                totalCount=instance.totalCount,
#                                                comments=instance.comments)
#                 instance.comments = ""
#
#         if instance.newEggsCollected or instance.newBabySnails or instance.damagedEggsCount:
#             pen_id = instance.penNumber.number
#             staff = instance.penNumber.responsible.name
#             staffDict = dict(Doowis=102, Victor=103, Grace=104, Afeez=105, TBC=108)
#             incubationPen = staffDict.get(staff)
#
#             try:
#                 latestRecord = \
#                     EggsInventory.objects.filter(penNumber=Pen.objects.get(number=incubationPen)).order_by("-id")[0]
#                 eggsComments = f"{latestRecord.totalCount} b/f @ {latestRecord.dateTimeRecorded} " \
#                                f"+ {instance.newEggsCollected} newEggsCollected from Pen No: {pen_id} " \
#                                f"- {instance.newBabySnails} newEggsHatched - {instance.damagedEggsCount} damagedEggsCount = "
#
#                 latestRecord.totalCount += instance.newEggsCollected
#                 latestRecord.totalCount -= instance.newBabySnails
#                 latestRecord.totalCount -= instance.damagedEggsCount
#                 eggsComments += str(latestRecord.totalCount)
#                 # if instance.comments:
#                 #     eggsComments += "\n" + instance.comments
#                 instance.comments = eggsComments
#                 create_egg_instance(incubationPen, instance, latestRecord)
#                 instance.comments = ""
#             except IndexError:
#                 # No record exist for this incubation pen - New entry
#                 instance.totalCount = instance.newEggsCollected - instance.newBabySnails - instance.damagedEggsCount
#                 eggsComments = f"{instance.newEggsCollected} newEggsCollected from Pen No: {pen_id} " \
#                                f"- {instance.newBabySnails} newEggsHatched - {instance.damagedEggsCount} damagedEggsCount"
#                 instance.comments = eggsComments
#                 EggsInventory.objects.create(penNumber=Pen.objects.get(number=incubationPen),
#                                              dateTimeRecorded=instance.dateTimeRecorded or timezone.now(),
#                                              specieType=Specie.objects.get(specie="AMO"),
#                                              totalCount=instance.totalCount,
#                                              comments=eggsComments)
#                 instance.comments = ""
#
#
# @receiver(post_save, sender=StocksTransfer)
# def update_stocks_transfers(sender, instance=None, created=False, **kwargs):
#     # when a new record is persisted, do the following:
#     # 1. update SnailsActivity Reshuffle for the Pen (for Snails) or EggsInventory totalCount table (for Eggs).
#     # Get the latest record for the pen number by dateTimeRecorded
#     if instance.quantity > 0:
#         source_pen_id = instance.sourcePen.number
#         destination_pen_id = instance.destinationPen.number
#         if instance.type == "Egg":
#             latestRecordSource = \
#                 EggsInventory.objects.filter(penNumber=Pen.objects.get(number=source_pen_id)).order_by("-id")[0]
#             latestRecordDestination = \
#                 EggsInventory.objects.filter(penNumber=Pen.objects.get(number=destination_pen_id)).order_by("-id")[0]
#             latestRecordSource.totalCount -= instance.quantity
#             latestRecordDestination.totalCount += instance.quantity
#
#             create_egg_instance(source_pen_id, instance, latestRecordSource)
#             create_egg_instance(destination_pen_id, instance, latestRecordDestination)
#
#         if instance.type == "Snail":
#             latestRecordSource = \
#                 SnailsInventory.objects.filter(penNumber=Pen.objects.get(number=source_pen_id)).order_by("-id")[0]
#             latestRecordDestination = \
#                 SnailsInventory.objects.filter(penNumber=Pen.objects.get(number=destination_pen_id)).order_by("-id")[0]
#             latestRecordSource.totalCount -= instance.quantity
#             latestRecordDestination.totalCount += instance.quantity
#             create_snail_instance(instance, latestRecordSource, True, pen_no=source_pen_id)
#             create_snail_instance(instance, latestRecordDestination, True, pen_no=destination_pen_id)
#
#         instance.comments = ""
