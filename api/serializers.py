from rest_framework import serializers
from .models import Battle

# this is used to serialize whole list of json data stored in db
class BattleSerial(serializers.ModelSerializer):
    class Meta:
        model = Battle
        fields = '__all__' #('name', 'year')


