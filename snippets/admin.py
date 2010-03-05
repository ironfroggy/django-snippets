from django.contrib import admin

from snippets.models import Snippet

class SnippetAdmin(admin.ModelAdmin):
    pass
admin.site.register(Snippet, SnippetAdmin)
