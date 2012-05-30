Softball
========

Still having issues using Django to calculate batting averages, slugging percentages and weighted on base percentages.

The model has two tables - Players and Statlines. Each Statline entry represents a players performance for an individual game. What I want to output on the homepage are the cumulative stats for each player so that they resemble the back of a baseball card. 

Where I'm currently stuck is that a batting average for an individual player is:
(sum of singles + sum of doubles + sum of triples + sum of homeruns) / sum of at bats

I can get these values and hardcode them but I want to make a query so I can iterate through it on the template. I was thinking of using a model method to calculate these so I could make a query like: 

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
    
And then when I iterate through it I could call a Player method like that would calculate the average of the player.

Am I on the right track here?

