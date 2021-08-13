from django.contrib import admin

from .models import Book, BookType
from .models import LinkType, ArticleLink, VideoLink
from .models import Document, DocumentType


class BookTypeAdmin(admin.ModelAdmin):
    list_display = ['name', 'order']


class BookAdmin(admin.ModelAdmin):
    list_display = ['name', 'order', 'book_type_id']


class LinkTypeAdmin(admin.ModelAdmin):
    list_display = ['name']


class ArticleLinkAdmin(admin.ModelAdmin):
    list_display = ['name', 'order', 'link_type_id']


class VideoLinkAdmin(admin.ModelAdmin):
    list_display = ['name', 'order', 'link_type_id']


class DocumentTypeAdmin(admin.ModelAdmin):
    list_display = ['name']


class DocumentAdmin(admin.ModelAdmin):
    list_display = ['name', 'order', 'document_type_id']


admin.site.register(BookType, BookTypeAdmin)
admin.site.register(Book, BookAdmin)

admin.site.register(LinkType, LinkTypeAdmin)
admin.site.register(ArticleLink, ArticleLinkAdmin)
admin.site.register(VideoLink, VideoLinkAdmin)

admin.site.register(DocumentType, DocumentTypeAdmin)
admin.site.register(Document, DocumentAdmin)
