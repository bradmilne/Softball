from django.shortcuts import render_to_response
from django.db.models import Sum, Count
from softball.models import Player, StatLine
from decimal import Decimal

def stat_table(request):
    
    players = Player.objects.filter(statline__season_name="Spring 2012")
    return render_to_response('stat_table.html', {'players': players})
        
        