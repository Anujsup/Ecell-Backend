from django.contrib import admin
from .models import PastEvent, PostImage, TeamMember, Department,UpcomingEvent
# , Pdf,Article,Video

# Register your models here.

class PropertyImageInline(admin.TabularInline):
    model = PostImage
    extra = 0

class PropertyAdmin(admin.ModelAdmin):
    inlines = [ PropertyImageInline, ]
admin.site.register(PastEvent, PropertyAdmin)
admin.site.register(Department)
admin.site.register(TeamMember)
admin.site.register(UpcomingEvent)
# admin.site.register(PastEvent)