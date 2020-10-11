from django.contrib import admin
from .models import Articles
from ckeditor_uploader.widgets import CKEditorUploadingWidget

@admin.register(Articles)
class ArticlesAdmin(admin.ModelAdmin):
    # text
    list_display = ("name", "create_date", "update_date", "text")
    
    def text(self, obj):
       return obj.text[0:70:] 

# Register your models here.
    