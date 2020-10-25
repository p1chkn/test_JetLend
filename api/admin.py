from django.contrib import admin
from .models import Passport, Qualification, Document


class PassportAdmin(admin.ModelAdmin):

    list_display = ('name', 'surname', 'serial_number')
    search_fields = ('name', )
    empty_value_display = '-empty-'


class QualificationAdmin(admin.ModelAdmin):

    list_display = ('pk', 'status')


class DocumentAdmin(admin.ModelAdmin):

    list_display = ('title', 'qualification')


admin.site.register(Passport, PassportAdmin)
admin.site.register(Qualification, QualificationAdmin)
admin.site.register(Document, DocumentAdmin)
