from django.db import models
from django.db.models import Sum, Count

# Create your models here.

SEASON_CHOICES = (
    ('Spring 2012', 'Spring 2012'),
    ('Summer 2012', 'Summer 2012'),
    ('Fall 2012', 'Fall 2012'),
)

GENDER_CHOICES = (
    ('M', 'Male'),
    ('F', "Female"),
)

HANDED_CHOICES = (
    ('L', 'Left'),
    ('R', 'Right'),
)

PITCHES_CHOICES = (
    ('Y', 'Y'),
    ('N', 'N'),
)

POSITION_CHOICES = (
    ('C', 'Catcher'),
    ('1B', 'First Base'),
    ('2B', 'Second Base'),
    ('3B', 'Third Base'),
    ('SS', 'Shortstop'),
    ('LF', 'Left Field'),
    ('CF', 'Center Field'),
    ('RF', 'Right Field'),
)

NUMBER_CHOICES = [(i,i) for i in range(11)]

class Player(models.Model):
    name = models.CharField(max_length=32)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    bats = models.CharField(max_length=1, choices=HANDED_CHOICES)
    throws = models.CharField(max_length=1, choices=HANDED_CHOICES)
    position = models.CharField(max_length=2, choices=POSITION_CHOICES)
    pitches = models.CharField(max_length=1, choices=PITCHES_CHOICES)
    hometown = models.CharField(max_length=32)
    
    def __unicode__(self):
        return self.name
    
    

class StatLine(models.Model):
    season_name = models.CharField(max_length=12, choices=SEASON_CHOICES)
    player = models.ForeignKey(Player)
    at_bats = models.IntegerField(max_length=2, choices=NUMBER_CHOICES, default=0)
    singles = models.IntegerField(max_length=2, choices=NUMBER_CHOICES, default=0)
    doubles = models.IntegerField(max_length=2, choices=NUMBER_CHOICES, default=0)
    triples = models.IntegerField(max_length=2, choices=NUMBER_CHOICES, default=0)
    homeruns = models.IntegerField(max_length=2, choices=NUMBER_CHOICES, default=0)
    runs = models.IntegerField(max_length=2, choices=NUMBER_CHOICES, default=0)
    rbis = models.IntegerField(max_length=2, choices=NUMBER_CHOICES, default=0)
    rboe = models.IntegerField(max_length=2, choices=NUMBER_CHOICES, default=0)
    hits = models.IntegerField(max_length=3, blank=True)
    
    
    def save(self):
        self.hits = self.singles + self.doubles + self.triples + self.homeruns
        super(StatLine, self).save()
    
    def __unicode__(self):
	    return self.player.name
    