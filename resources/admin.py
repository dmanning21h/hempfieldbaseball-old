from django.contrib import admin

from .models import Book, BookType
from .models import WebsiteLink, WebsiteLinkType
from .models import Document, DocumentType


admin.site.register(Book)
admin.site.register(BookType)
admin.site.register(WebsiteLink)
admin.site.register(WebsiteLinkType)
admin.site.register(Document)
admin.site.register(DocumentType)
