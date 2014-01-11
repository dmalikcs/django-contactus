# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'ContactUs.status'
        db.add_column(u'contactus_contactus', 'status',
                      self.gf('django.db.models.fields.CharField')(default='N', max_length=2),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'ContactUs.status'
        db.delete_column(u'contactus_contactus', 'status')


    models = {
        u'contactus.contactus': {
            'Meta': {'object_name': 'ContactUs'},
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'message': ('django.db.models.fields.TextField', [], {'max_length': '200'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'status': ('django.db.models.fields.CharField', [], {'default': "'N'", 'max_length': '2'})
        }
    }

    complete_apps = ['contactus']