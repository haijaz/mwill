# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Testator'
        db.create_table(u'will_testator', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('gender', self.gf('django.db.models.fields.CharField')(max_length=6)),
        ))
        db.send_create_signal(u'will', ['Testator'])

        # Adding model 'Inheritors'
        db.create_table(u'will_inheritors', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('gender', self.gf('django.db.models.fields.CharField')(max_length=6)),
            ('relative', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['will.Inheritors'])),
            ('testator', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['will.Testator'])),
        ))
        db.send_create_signal(u'will', ['Inheritors'])


    def backwards(self, orm):
        # Deleting model 'Testator'
        db.delete_table(u'will_testator')

        # Deleting model 'Inheritors'
        db.delete_table(u'will_inheritors')


    models = {
        u'will.inheritors': {
            'Meta': {'object_name': 'Inheritors'},
            'gender': ('django.db.models.fields.CharField', [], {'max_length': '6'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'relative': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['will.Inheritors']"}),
            'testator': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['will.Testator']"})
        },
        u'will.testator': {
            'Meta': {'object_name': 'Testator'},
            'gender': ('django.db.models.fields.CharField', [], {'max_length': '6'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        }
    }

    complete_apps = ['will']