# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Relationships'
        db.create_table(u'will_relationships', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('type', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'will', ['Relationships'])

        # Adding field 'Inheritors.relationType'
        db.add_column(u'will_inheritors', 'relationType',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['will.Relationships']),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting model 'Relationships'
        db.delete_table(u'will_relationships')

        # Deleting field 'Inheritors.relationType'
        db.delete_column(u'will_inheritors', 'relationType_id')


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
            'type': ('django.db.models.fields.IntegerField', [], {})
        },
        u'will.testator': {
            'Meta': {'object_name': 'Testator'},
            'gender': ('django.db.models.fields.CharField', [], {'max_length': '6'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        }
    }

    complete_apps = ['will']