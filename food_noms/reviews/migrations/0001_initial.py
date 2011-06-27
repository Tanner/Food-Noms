# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Rating'
        db.create_table('ratings_rating', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nom', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['noms.Nom'])),
        ))
        db.send_create_signal('ratings', ['Rating'])

        # Adding model 'Question'
        db.create_table('ratings_question', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('question', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('hasRate', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('hasFreeResponse', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('ratings', ['Question'])

        # Adding model 'Response'
        db.create_table('ratings_response', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('rating', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['reviews.Rating'])),
            ('question', self.gf('django.db.models.fields.related.ForeignKey')(related_name='+', to=orm['reviews.Question'])),
            ('rate', self.gf('django.db.models.fields.IntegerField')()),
            ('freeResponse', self.gf('django.db.models.fields.CharField')(max_length=1000)),
        ))
        db.send_create_signal('ratings', ['Response'])


    def backwards(self, orm):
        
        # Deleting model 'Rating'
        db.delete_table('ratings_rating')

        # Deleting model 'Question'
        db.delete_table('ratings_question')

        # Deleting model 'Response'
        db.delete_table('ratings_response')


    models = {
        'noms.nom': {
            'Meta': {'object_name': 'Nom'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'restaurant': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['noms.Restaurant']"})
        },
        'noms.restaurant': {
            'Meta': {'object_name': 'Restaurant'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '150'})
        },
        'reviews.question': {
            'Meta': {'object_name': 'Question'},
            'hasFreeResponse': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'hasRate': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'question': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'reviews.rating': {
            'Meta': {'object_name': 'Rating'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nom': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['noms.Nom']"})
        },
        'reviews.response': {
            'Meta': {'object_name': 'Response'},
            'freeResponse': ('django.db.models.fields.CharField', [], {'max_length': '1000'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'question': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'+'", 'to': "orm['reviews.Question']"}),
            'rate': ('django.db.models.fields.IntegerField', [], {}),
            'rating': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['reviews.Rating']"})
        }
    }

    complete_apps = ['ratings']
