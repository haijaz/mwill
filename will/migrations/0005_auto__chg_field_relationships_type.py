# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Relationships.type'
        db.alter_column(u'will_relationships', 'type', self.gf('django.db.models.fields.CharField')(max_length=12))

    def backwards(self, orm):

        # Changing field 'Relationships.type'
        db.alter_column(u'will_relationships', 'type', self.gf('django.db.models.fields.IntegerField')())

    models = {
        u'will.inheritors': {
            'Meta': {'object_name': 'Inheritors'},
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