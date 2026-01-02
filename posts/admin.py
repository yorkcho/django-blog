from django.contrib import admin

# Register your models here.
from .models import Post

class PostAdmin(admin.ModelAdmin):
    # 確保所有可編輯的欄位都在 fields/fieldsets 裡
    fields = ('title', 'content', 'created_at')
    list_display = ['title', 'content', 'created_at']
    list_filter = ["created_at"]
    search_fields = ['title', 'content']
    # 將 created_at 設為只讀
    readonly_fields = ('created_at',)
    
admin.site.register(Post, PostAdmin)



# register multiple model classes
# @admin.register(Post) 
# class PostAdmin(admin.ModelAdmin):
#     pass


