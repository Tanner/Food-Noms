# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Restaurant'
        db.create_table('noms_restaurant', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=150)),
        ))
        db.send_create_signal('noms', ['Restaurant'])

        # Adding model 'Nom'
        db.create_table('noms_nom', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('restaurant', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['noms.Restaurant'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=150)),
        ))
        db.send_create_signal('noms', ['Nom'])


    def backwards(self, orm):
        
        # Deleting model 'Restaurant'
        db.delete_table('noms_restaurant')

        # Deleting model 'Nom'
        db.delete_table('noms_nom')


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
        }
    }

    complete_apps = ['noms']
