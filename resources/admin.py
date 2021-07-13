from django.contrib import admin

from .models import Book, BookType
from .models import WebsiteLink, WebsiteLinkType
from .models import Document, DocumentType


class BookAdmin(admin.ModelAdmin):
    list_display = ['name', 'order', 'book_type_id']


class BookTypeAdmin(admin.ModelAdmin):
    list_display = ['name', 'order']


class WebsiteLinkAdmin(admin.ModelAdmin):
    list_display = ['name', 'order', 'website_link_type_id']


class WebsiteLinkTypeAdmin(admin.ModelAdmin):
    list_display = ['name']


class DocumentAdmin(admin.ModelAdmin):
    list_display = ['name', 'order', 'document_type_id']


class DocumentTypeAdmin(admin.ModelAdmin):
    list_display = ['name']


admin.site.register(Book, BookAdmin)
admin.site.register(BookType, BookTypeAdmin)
admin.site.register(WebsiteLink, WebsiteLinkAdmin)
admin.site.register(WebsiteLinkType, WebsiteLinkTypeAdmin)
admin.site.register(Document, DocumentAdmin)
admin.site.register(DocumentType, DocumentTypeAdmin)
