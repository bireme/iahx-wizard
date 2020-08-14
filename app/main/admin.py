from django.contrib import admin

from main.models import *

class StepLocalAdmin(admin.TabularInline):
    model = StepLocal
    extra = 0

@admin.register(Step)
class StepAdmin(admin.ModelAdmin):
    list_filter = ('wizard__name', 'step_number',)
    inlines = [StepLocalAdmin,]


class OptionLocalAdmin(admin.TabularInline):
    model = OptionLocal
    extra = 0

@admin.register(Option)
class OptionAdmin(admin.ModelAdmin):
    list_filter = ('step__wizard__name', 'step__step_number', 'group', )
    inlines = [OptionLocalAdmin,]


admin.site.register(Wizard)
