from will.models import Testator, Inheritors, Relationships
from django.contrib import admin

class InheritorsInline(admin.StackedInline):
    model = Inheritors
    extra = 5
    
class TestatorAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,          {'fields':  ['name']}),
        (None,          {'fields':  ['gender']}),
    ]
    inlines = [InheritorsInline]
    
class RelationshipsAdmin(admin.ModelAdmin):
    list_display = ('type', 'id')    
    
admin.site.register(Testator, TestatorAdmin)
admin.site.register(Relationships, RelationshipsAdmin)