from datetime import datetime

from django.db.models import Max, Q, Sum, DateField, QuerySet, Avg
from django.db.models.functions import Cast
from django.http import JsonResponse, Http404, HttpResponseRedirect
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser

from front_end.forms import SnailActivityForm
from rest_api.models import SnailsActivity, SnailsInventory, EggsInventory, Pen
from rest_api.serializers import SnailsActivitySerializer


def getMaxDate():
    return SnailsActivity.objects.latest('dateTimeRecorded').dateTimeRecorded


def activitySnapshot() -> QuerySet:
    return SnailsActivity.objects.annotate(date=Cast('dateTimeRecorded', DateField())) \
        .values('date') \
        .annotate(totalMortalities=Sum('totalMortalities'),
                  totalEggsCollected=Sum('newEggsCollected'),
                  totalBabySnails=Sum('newBabySnails'),
                  totalDamagedEggsCount=Sum('damagedEggsCount'),
                  totalNewBreederStocks=Sum('newBreederStocks'),
                  avgFeedConsumptionRate=Avg('feedConsumptionRate'),
                  totalCountRebase=Sum('snailReshuffle')) \
        .order_by('date')


def create_new_activity(request):
    """
    Create a new activity.
    """
    if request.method == "POST":
        form = SnailActivityForm(request.POST or None)
        if form.is_valid():
            data = SnailsActivity(**form.cleaned_data)
            data.save()
            return JsonResponse(SnailsActivitySerializer(data).data, safe=False)
        else:
            return HttpResponseRedirect(redirect_to="frontend:activity")

    # elif request.method == "GET":
    #     snails_activity = SnailsActivity.objects.all().order_by('-dateTimeRecorded')
    #     serializer = SnailsActivitySerializer(snails_activity, many=True)
    #     return JsonResponse(serializer.data, safe=False)

    # elif request.method == "POST":
    #     data = JSONParser().parse(request)
    #     serializer = SnailsActivitySerializer(data=data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return JsonResponse(serializer.data, status=201)
    #     return JsonResponse(serializer.errors, status=400)
    else:
        form = SnailActivityForm()  # An unbound form
        return render(request, 'activity-form.html', {"form": form})


def activity_summary(request):
    query = activitySnapshot()
    totals = SnailsActivity.objects.aggregate(Sum('totalMortalities'), Sum('newEggsCollected'),
                                              Sum('newBabySnails'), Sum('newBreederStocks'),
                                              Sum('snailReshuffle'), Sum('damagedEggsCount'),
                                              Max('feedConsumptionRate'),
                                              )
    latestTime = SnailsActivity.objects.latest('dateTimeRecorded').dateTimeRecorded
    return render(request, 'activity-summary.html', context=dict(data=query, max_date=latestTime, grandTotals=totals))


def activity_detail_by_date(request, year: int, month: int, day: int):
    query = SnailsActivity.objects.filter(dateTimeRecorded__day=day,
                                          dateTimeRecorded__month=month,
                                          dateTimeRecorded__year=year)
    latestTime = SnailsActivity.objects.latest('dateTimeRecorded').dateTimeRecorded
    try:
        aggregates = activitySnapshot().filter(date__year=year, date__month=month, date__day=day)[0]
    except IndexError as e:
        raise Http404(f"No record exist for {datetime(year, month, day)}")
    return render(request, 'activity-detail.html', context=dict(data=query, max_date=latestTime,
                                                                grandTotals=aggregates, is_date_filtered=True))


def activity_detail(request):
    # https://docs.djangoproject.com/en/4.0/intro/overview/#write-your-views
    # https://stackoverflow.com/a/59605867
    # https://django-tables2.readthedocs.io/en/latest/pages/tutorial.html
    query = SnailsActivity.objects.all().order_by('dateTimeRecorded')
    latestTime = SnailsActivity.objects.latest('dateTimeRecorded').dateTimeRecorded
    return render(request, 'activity-detail.html', context=dict(data=query, max_date=latestTime,
                                                                is_date_filtered=False))


def activity_detail_by_pen(request, pen):
    query = SnailsActivity.objects.all().filter(penNumber__number=pen).order_by('dateTimeRecorded')
    latestTime = SnailsActivity.objects.latest('dateTimeRecorded').dateTimeRecorded
    return render(request, 'activity-detail.html', context=dict(data=query, max_date=latestTime,
                                                                is_date_filtered=False))


def inventory_detail(request):
    query = SnailsInventory.objects.all().order_by('penNumber', 'dateTimeRecorded')
    return render(request, 'inventory.html', context=dict(data=query, max_date=datetime.now()))


def inventory_detail_by_pen(request, pen):
    query = SnailsInventory.objects.all().filter(penNumber__number=pen).order_by('penNumber', 'dateTimeRecorded')
    return render(request, 'inventory.html', context=dict(data=query, max_date=datetime.now()))


def inventory_snapshot_all(request):
    query = getInventorySnapshot()
    totals = query.aggregate(Sum('totalCount'))['totalCount__sum']
    return render(request, 'inventory.html', context=dict(data=query, max_date=datetime.now(),
                                                          grandTotals=totals, isSnapshot=True))


def inventory_snapshot(request):
    query = getInventorySnapshot().filter(totalCount__gt=0)
    totals = query.aggregate(Sum('totalCount'))['totalCount__sum']
    eggsCount = getEggsSnapshot().aggregate(Sum('totalCount'))['totalCount__sum']
    return render(request, 'inventory.html', context=dict(data=query, max_date=datetime.now(),
                                                          eggsCount=eggsCount,
                                                          grandTotals=totals, isSnapshot=True))


def inventory_by_specie(request):
    data = getInventorySnapshot().filter(totalCount__gt=0)
    dataAggregatesBySpecie = data.values('specieType').annotate(specieSum=Sum('totalCount')).order_by()
    totals = data.aggregate(Sum('totalCount'))['totalCount__sum']
    return render(request, 'inventory-by-specie.html',
                  context=dict(data=dataAggregatesBySpecie, max_date=datetime.now(),
                               grandTotals=totals, isSnapshot=True))


def getInventorySnapshot():
    model_mx_set = SnailsInventory.objects.values('penNumber_id') \
        .annotate(maxDateRecorded=Max('dateTimeRecorded')).order_by()
    q_statement = Q()
    for pair in model_mx_set:
        q_statement |= (Q(penNumber_id=pair['penNumber_id']) & Q(dateTimeRecorded=pair['maxDateRecorded']))
    model_set = SnailsInventory.objects.filter(q_statement)
    return model_set.order_by('penNumber')


def getEggsSnapshot():
    model_mx_set = EggsInventory.objects.values('penNumber_id') \
        .annotate(maxDateRecorded=Max('dateTimeRecorded')).order_by()
    q_statement = Q()
    for pair in model_mx_set:
        q_statement |= (Q(penNumber_id=pair['penNumber_id']) & Q(dateTimeRecorded=pair['maxDateRecorded']))
    model_set = EggsInventory.objects.filter(q_statement)
    return model_set.order_by('penNumber')


def eggs_inventory_activities(request):
    query = EggsInventory.objects.all().order_by('dateTimeRecorded')
    return render(request, 'eggs-inventory-activities.html', context=dict(data=query, max_date=datetime.now()))


def eggs_inventory_by_pen(request, pen):
    query = EggsInventory.objects.all().filter(penNumber__number=pen).order_by('dateTimeRecorded')
    return render(request, 'eggs-inventory-activities.html', context=dict(data=query, max_date=datetime.now()))


def eggs_inventory_snapshot(request):
    data = getEggsSnapshot()
    totals = data.aggregate(Sum('totalCount'))['totalCount__sum']
    return render(request, 'eggs-inventory-snapshot.html',
                  context=dict(data=data, totals=totals, max_date=datetime.now()))


def pen_data(request):
    query = Pen.objects.all().order_by('number')
    print(f"{request.scheme}://{request.get_host()}")
    return render(request, 'pen-data.html', context=dict(data=query, max_date=datetime.now()))


def activity_graph(request):
    querySet = activitySnapshot()  # .values('date', 'totalMortalities', 'newEggsCollected')
    data = [[record.get('date'), record.get('totalMortalities')] for record in querySet]
    labels = ['Date', 'totalMortalities']
    return render(request, 'snails_charts.html', context=dict(labels=labels, data=data))
