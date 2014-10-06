# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Contest_Problem.max_score'
        db.add_column('compile_contest_problem', 'max_score',
                      self.gf('django.db.models.fields.IntegerField')(default=100),
                      keep_default=False)


        # Changing field 'Contest_Problem.category'
        db.alter_column('compile_contest_problem', 'category', self.gf('django.db.models.fields.TextField')(max_length=20))

    def backwards(self, orm):
        # Deleting field 'Contest_Problem.max_score'
        db.delete_column('compile_contest_problem', 'max_score')


        # Changing field 'Contest_Problem.category'
        db.alter_column('compile_contest_problem', 'category', self.gf('django.db.models.fields.TextField')())

    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['auth.Permission']", 'blank': 'True'})
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
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['auth.Group']", 'related_name': "'user_set'", 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['auth.Permission']", 'related_name': "'user_set'", 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'compile.contest': {
            'Meta': {'object_name': 'Contest'},
            'contestor': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"}),
            'description': ('django.db.models.fields.TextField', [], {'max_length': '500'}),
            'endtime': ('django.db.models.fields.DateTimeField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'starttime': ('django.db.models.fields.DateTimeField', [], {}),
            'title': ('django.db.models.fields.TextField', [], {})
        },
        'compile.contest_problem': {
            'Meta': {'object_name': 'Contest_Problem'},
            'category': ('django.db.models.fields.TextField', [], {'max_length': '20', 'blank': 'True'}),
            'contest': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['compile.Contest']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'max_score': ('django.db.models.fields.IntegerField', [], {}),
            'problem': ('django.db.models.fields.TextField', [], {}),
            'testcase_in_1': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'testcase_in_2': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'testcase_in_3': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'testcase_out_1': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'testcase_out_2': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'testcase_out_3': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'title': ('django.db.models.fields.TextField', [], {})
        },
        'compile.contest_submission': {
            'Meta': {'ordering': "['-created']", 'object_name': 'Contest_Submission'},
            'contest_problem': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['compile.Contest_Problem']"}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'fname': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"})
        },
        'compile.submission_result': {
            'Meta': {'object_name': 'Submission_Result'},
            'average_time': ('django.db.models.fields.FloatField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'result_type': ('django.db.models.fields.IntegerField', [], {}),
            'submission': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['compile.Contest_Submission']", 'unique': 'True'}),
            'testcase_passed': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        'compile.submission_try': {
            'Meta': {'object_name': 'Submission_Try'},
            'finput': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'blank': 'True'}),
            'fname': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['compile']