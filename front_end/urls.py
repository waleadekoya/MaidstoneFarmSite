from django.urls import path

from . import views

app_name = 'frontend'
urlpatterns = [
    path('snails/activity/detail/', views.activity_detail, name='activity-detail'),
    path('snails/activity/detail/<int:year>/<int:month>/<int:day>', views.activity_detail_by_date,
         name='activity-by-date'),
    path('snails/activity/detail/<pen>', views.activity_detail_by_pen, name='activity-detail-by-pen'),
    path('snails/activity/summary/', views.activity_summary, name='activity-summary'),
    path('snails/inventory/detail/', views.inventory_detail, name='inventory-detail'),
    path('snails/inventory/detail/<pen>', views.inventory_detail_by_pen, name='inventory-detail-by-pen'),
    path('snails/inventory/snapshot/', views.inventory_snapshot, name='inventory-snapshot'),
    path('snails/inventory/snapshot/all', views.inventory_snapshot_all, name='inventory-snapshot-all'),
    path('snails/inventory/specie/', views.inventory_by_specie, name='inventory-specie'),
    path('eggs/inventory/activities', views.eggs_inventory_activities, name='eggs-inventory-activities'),
    path('eggs/inventory/activities/<pen>', views.eggs_inventory_by_pen, name='eggs-inventory-by-pen'),
    path('eggs/inventory/snapshot', views.eggs_inventory_snapshot, name='eggs-inventory-snapshot'),
    path('pens/view/', views.pen_data, name='pens'),
    path('graphs/', views.activity_graph, name='graphs')
]
# /inventory
