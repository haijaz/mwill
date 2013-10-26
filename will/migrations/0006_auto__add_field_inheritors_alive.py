# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Inheritors.alive'
        db.add_column(u'will_inheritors', 'alive',
                      self.gf('django.db.models.fields.NullBooleanField')(null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Inheritors.alive'
        db.delete_column(u'will_inheritors', 'alive')


    models = {
        u'will.inheritors': {
            'Meta': {'object_name': 'Inheritors'},
            'alive': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'gender': ('django.db.models.fields.CharField', [], {'max_length': '6'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'relationType': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['will.Relationships']"}),
            'relative': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['will.Inheritors']", 'null': 'True', 'blank': 'True'}),
            'testator': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['will.Testator']"})
        },
        u'will.relationships': {
            'Meta': {'object_name': 'Relationships'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '12'})
        },
        u'will.testator': {
            'Meta': {'object_name': 'Testator'},
            'gender': ('django.db.models.fields.CharField', [], {'max_length': '6'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        }
    }

    complete_apps = ['will']