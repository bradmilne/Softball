# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Player'
        db.create_table('softball_player', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=32)),
            ('gender', self.gf('django.db.models.fields.CharField')(max_length=1)),
            ('bats', self.gf('django.db.models.fields.CharField')(max_length=1)),
            ('throws', self.gf('django.db.models.fields.CharField')(max_length=1)),
            ('position', self.gf('django.db.models.fields.CharField')(max_length=2)),
            ('pitches', self.gf('django.db.models.fields.CharField')(max_length=1)),
            ('hometown', self.gf('django.db.models.fields.CharField')(max_length=32)),
        ))
        db.send_create_signal('softball', ['Player'])

        # Adding model 'StatLine'
        db.create_table('softball_statline', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('season_name', self.gf('django.db.models.fields.CharField')(max_length=12)),
            ('player', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['softball.Player'])),
            ('at_bats', self.gf('django.db.models.fields.IntegerField')(default=0, max_length=2)),
            ('singles', self.gf('django.db.models.fields.IntegerField')(default=0, max_length=2)),
            ('doubles', self.gf('django.db.models.fields.IntegerField')(default=0, max_length=2)),
            ('triples', self.gf('django.db.models.fields.IntegerField')(default=0, max_length=2)),
            ('homeruns', self.gf('django.db.models.fields.IntegerField')(default=0, max_length=2)),
            ('runs', self.gf('django.db.models.fields.IntegerField')(default=0, max_length=2)),
            ('rbis', self.gf('django.db.models.fields.IntegerField')(default=0, max_length=2)),
            ('rboe', self.gf('django.db.models.fields.IntegerField')(default=0, max_length=2)),
            ('hits', self.gf('django.db.models.fields.IntegerField')(max_length=3, blank=True)),
            ('avg', self.gf('django.db.models.fields.DecimalField')(max_digits=4, decimal_places=3, blank=True)),
        ))
        db.send_create_signal('softball', ['StatLine'])

    def backwards(self, orm):
        # Deleting model 'Player'
        db.delete_table('softball_player')

        # Deleting model 'StatLine'
        db.delete_table('softball_statline')

    models = {
        'softball.player': {
            'Meta': {'object_name': 'Player'},
            'bats': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'gender': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'hometown': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            'pitches': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'position': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'throws': ('django.db.models.fields.CharField', [], {'max_length': '1'})
        },
        'softball.statline': {
            'Meta': {'object_name': 'StatLine'},
            'at_bats': ('django.db.models.fields.IntegerField', [], {'default': '0', 'max_length': '2'}),
            'avg': ('django.db.models.fields.DecimalField', [], {'max_digits': '4', 'decimal_places': '3', 'blank': 'True'}),
            'doubles': ('django.db.models.fields.IntegerField', [], {'default': '0', 'max_length': '2'}),
            'hits': ('django.db.models.fields.IntegerField', [], {'max_length': '3', 'blank': 'True'}),
            'homeruns': ('django.db.models.fields.IntegerField', [], {'default': '0', 'max_length': '2'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'player': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['softball.Player']"}),
            'rbis': ('django.db.models.fields.IntegerField', [], {'default': '0', 'max_length': '2'}),
            'rboe': ('django.db.models.fields.IntegerField', [], {'default': '0', 'max_length': '2'}),
            'runs': ('django.db.models.fields.IntegerField', [], {'default': '0', 'max_length': '2'}),
            'season_name': ('django.db.models.fields.CharField', [], {'max_length': '12'}),
            'singles': ('django.db.models.fields.IntegerField', [], {'default': '0', 'max_length': '2'}),
            'triples': ('django.db.models.fields.IntegerField', [], {'default': '0', 'max_length': '2'})
        }
    }

    complete_apps = ['softball']