from rest_framework import serializers

from .models import Pen, SnailsInventory, SnailsActivity, EggsInventory, StocksTransfer


class PenSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Pen
        fields = ['number', 'size', 'created_date', 'modified_date']


class SnailsInventorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = SnailsInventory
        fields = '__all__'
        # fields = ['penNumber', 'species', 'dateRecorded', 'totalCount']


class EggsInventorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = EggsInventory
        fields = '__all__'


class SnailsActivitySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = SnailsActivity
        fields = '__all__'
        # fields = ['penNumber', 'species', 'dateRecorded', 'totalMortalities', 'newBreederStocks',
        #           'newEggsCollected', 'newBabySnails', 'damagedEggsCount', 'snailReshuffle']

    def create(self, validated_data):
        return SnailsActivity.objects.create(**validated_data)


# https://stackoverflow.com/questions/68767041/how-to-post-multiple-objects-in-one-json-request


class StocksTransferSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = StocksTransfer
        fields = '__all__'
