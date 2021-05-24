from .models import Book, BookType
from .models import WebsiteLink, WebsiteLinkType
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
    pass


def does_diet_website_link_data_exist():
    pass


def does_hitting_video_link_data_exist():
    pass


def does_hitting_article_link_data_exist():
    pass


def get_all_diet_documents():
    pass


def get_all_diet_website_links():
    pass


def get_all_books_grouped_by_type():
    pass


def get_all_hitting_video_links():
    pass


def get_all_hitting_articles():
    pass