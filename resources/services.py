from .models import Book, BookType
from .models import ArticleLink, VideoLink, LinkType
from .models import Document, DocumentType


def _model_records_exist(model):
    if len(model.objects.all()) > 0:
        return True
    else:
        return False


def does_book_data_exist():
    return _model_records_exist(Book)


def does_diet_data_exist():
    diet_document_data = does_diet_document_data_exist()
    diet_website_links = does_diet_website_link_data_exist()
    return diet_document_data or diet_website_links


def does_diet_document_data_exist():
    if len(Document.objects.filter(document_type__name="Diet")) > 0:
        return True
    else:
        return False


def does_diet_website_link_data_exist():
    if len(ArticleLink.objects.filter(link_type__name="Diet")) > 0:
        return True
    else:
        return False


def does_hitting_video_link_data_exist():
    if len(VideoLink.objects.filter(link_type__name="Hitting Video")) > 0:
        return True
    else:
        return False


def does_hitting_article_link_data_exist():
    if len(ArticleLink.objects.filter(link_type__name="Hitting Article")) > 0:
        return True
    else:
        return False


def get_all_diet_documents():
    return DocumentType.objects.get(name="Diet").documents.all()


def get_all_diet_articles():
    return LinkType.objects.get(name="Diet").articles.all()


def get_all_books_grouped_by_type():
    books_grouped = {}
    for book_type in BookType.objects.exclude(name="lifting"):
        books_grouped[book_type.name] = book_type.books.all()

    return books_grouped


def get_all_hitting_videos():
    return LinkType.objects.get(name="Hitting").videos.all()


def get_all_hitting_articles():
    return LinkType.objects.get(name="Hitting").articles.all()