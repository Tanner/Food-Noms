# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Deleting field 'Question.hasRate'
        db.delete_column('ratings_question', 'hasRate')

        # Deleting field 'Question.hasFreeResponse'
        db.delete_column('ratings_question', 'hasFreeResponse')

        # Adding field 'Question.type'
        db.add_column('ratings_question', 'type', self.gf('django.db.models.fields.CharField')(default='RATING', max_length=200), keep_default=False)

        # Changing field 'Response.rate'
        db.alter_column('ratings_response', 'rate', self.gf('django.db.models.fields.IntegerField')(null=True))

        # Changing field 'Response.freeResponse'
        db.alter_column('ratings_response', 'freeResponse', self.gf('django.db.models.fields.CharField')(max_length=1000, null=True))


    def backwards(self, orm):
        
        # Adding field 'Question.hasRate'
        db.add_column('ratings_question', 'hasRate', self.gf('django.db.models.fields.BooleanField')(default=False), keep_default=False)

        # Adding field 'Question.hasFreeResponse'
        db.add_column('ratings_question', 'hasFreeResponse', self.gf('django.db.models.fields.BooleanField')(default=False), keep_default=False)

        # Deleting field 'Question.type'
        db.delete_column('ratings_question', 'type')

        # User chose to not deal with backwards NULL issues for 'Response.rate'
        raise RuntimeError("Cannot reverse this migration. 'Response.rate' and its values cannot be restored.")

        # User chose to not deal with backwards NULL issues for 'Response.freeResponse'
        raise RuntimeError("Cannot reverse this migration. 'Response.freeResponse' and its values cannot be restored.")


    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
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
        'ratings.question': {
            'Meta': {'object_name': 'Question'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'question': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'ratings.rating': {
            'Meta': {'object_name': 'Rating'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nom': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['noms.Nom']"}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']", 'null': 'True'})
        },
        'ratings.response': {
            'Meta': {'object_name': 'Response'},
            'freeResponse': ('django.db.models.fields.CharField', [], {'max_length': '1000', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'question': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'+'", 'to': "orm['ratings.Question']"}),
            'rate': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'rating': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['ratings.Rating']"})
        }
    }

    complete_apps = ['ratings']
