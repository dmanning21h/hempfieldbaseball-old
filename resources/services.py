from .models import BookType, LinkType, DocumentType
from .enums import ResourceTypes

def get_all_diet_documents():
    return DocumentType.objects.get(name=ResourceTypes.DIET).documents.all()


def get_all_diet_articles():
    return LinkType.objects.get(name=ResourceTypes.DIET).articles.all()


def get_all_books_grouped_by_type():
    books_grouped = {}
    for book_type in BookType.objects.exclude(name=ResourceTypes.LIFTING):
        books_grouped[book_type.name] = book_type.books.all()

    return books_grouped


def get_all_hitting_videos():
    return LinkType.objects.get(name=ResourceTypes.HITTING).videos.all()


def get_all_hitting_articles():
    return LinkType.objects.get(name=ResourceTypes.HITTING).articles.all()