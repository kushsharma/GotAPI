from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Battle
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import BattleSerial


# Returns number of battles
class BattleCount(APIView):
    def get(self, request):
        all_battles = Battle.objects.all()
        return Response({'count': len(all_battles)})

# Returns list of all battles
class BattleList(APIView):
    def get(self, request):
        list = Battle.objects.all()
        serial = BattleSerial(list, many=True)
        return Response(serial.data)

    def post(self):
        pass


# Generates stats from database
class BattleStats(APIView):
    def get(self, request):
        winlist = Battle.objects.filter(attacker_outcome="win")
        wincount = 0
        for rec in winlist:
            wincount += 1;

        losslist = Battle.objects.filter(attacker_outcome="loss")
        losscount = 0
        for rec in losslist:
            losscount += 1;

        battelist = Battle.objects.all()
        battletype = []
        attackerList = []
        defenderList = []
        regionList = []
        defenderSizeList = []

        average = 0
        for rec in battelist:
            if battletype.count(str(rec.battle_type)) == 0 and str(rec.battle_type) != "":
                battletype.append(rec.battle_type)

            if str(rec.attacker_king) != "":
                attackerList.append(rec.attacker_king)
            if str(rec.defender_king) != "":
                defenderList.append(rec.defender_king)
            if str(rec.region) != "":
                regionList.append(rec.region)
            if str(rec.defender_size) != "":
                defenderSizeList.append(rec.defender_size)
                average += int(rec.defender_size)

        # baking stats for json
        jsn = {'most_active': {'attacker_king': most_common(attackerList),
                               'defender_king' : most_common(defenderList),
                               'region' : most_common(regionList)},
               'attacker_outcome': {'win': wincount, 'loss': losscount},
               'battle_type': battletype,
               'defender_size':{'average':average/len(defenderSizeList),
                                'min':min(defenderSizeList),
                                'max':max(defenderSizeList)}
               };
        # serial = BattleSerial(winlist, many=True)
        return Response(jsn)

    def post(self):
        pass


def most_common(lst):
    return max(set(lst), key=lst.count)

# Searches based on query
# /search/name=<name>
# /search/king=<attacker_king>
# /search/type=<battle_type>
# /search/location=<location>
class SearchQuery(APIView):
    def get(self, request):
        jsn = ""
        qname = request.GET.get('name', 'null')
        qking = request.GET.get('king', 'null')
        qtype = request.GET.get('type', 'null')
        qlocation = request.GET.get('location', 'null')

        html = ""

        if qname != "null":
            all_battles = Battle.objects.filter(name=qname)
            serial = BattleSerial(all_battles, many=True)
            return Response(serial.data)
        elif qking != "null":
            all_battles = Battle.objects.filter(attacker_king=qking)
            serial = BattleSerial(all_battles, many=True)
            return Response(serial.data)
        elif qtype != "null":
            all_battles = Battle.objects.filter(battle_type=qtype)
            serial = BattleSerial(all_battles, many=True)
            return Response(serial.data)
        elif qlocation != "null":
            all_battles = Battle.objects.filter(location=qlocation)
            serial = BattleSerial(all_battles, many=True)
            return Response(serial.data)
        else:
            return Response("{}")
