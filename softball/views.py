from django.shortcuts import render_to_response
from django.db.models import Sum, Count
from softball.models import Player, StatLine

def stat_table(request):
    
    
    stats = Player.objects.filter(statline__season_name="Spring 2012"
    ).annotate(
        sum_atbats=Sum('statline__at_bats'),
        sum_singles=Sum('statline__singles'),
        sum_doubles=Sum('statline__doubles'),
        sum_triples=Sum('statline__triples'),
        sum_homeruns=Sum('statline__homeruns'),
        sum_rbis=Sum('statline__rbis'),
        sum_rboe=Sum('statline__rboe'),
        sum_hits=Sum('statline__hits'),
    )

    

  
   
    return render_to_response('stat_table.html', {
        'stats': stats,
       
    })