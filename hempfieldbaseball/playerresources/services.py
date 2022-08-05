from .models import BookType, LinkType, DocumentType
from .enums import ResourceTypes


def get_all_diet_documents():
    return DocumentType.objects.get(name=ResourceTypes.DIET).documents.all()


def get_all_diet_articles():
    return LinkType.objects.get(name=ResourceTypes.DIET).articles.all()


def get_mental_baseball_books():
    return BookType.objects.get(name=ResourceTypes.MENTAL_BASEBALL).books.all()


def get_all_hitting_videos():
    return LinkType.objects.get(name=ResourceTypes.HITTING).videos.all()


def get_all_hitting_articles():
    return LinkType.objects.get(name=ResourceTypes.HITTING).articles.all()
