from django.shortcuts import render

from . import services as rs


def index(request):
    diet_data_exists = rs.does_diet_data_exist()
    book_data_exists = rs.does_book_data_exist()
    hitting_videos_exist = rs.does_hitting_video_link_data_exist()
    hitting_articles_exist = rs.does_hitting_article_link_data_exist()

    context = {
        'diet_data_exists':
            diet_data_exists,
        'book_data_exists':
            book_data_exists,
        'hitting_videos_exist':
            hitting_videos_exist,
        'hitting_articles_exist':
            hitting_articles_exist
    }

    return render(request, 'resources/resources.html', context)


def diet(request):
    diet_documents = rs.get_all_diet_documents()
    diet_website_links = rs.get_all_diet_articles()

    context = {
        'diet_documents':
            diet_documents,
        'diet_website_links':
            diet_website_links
    }

    return render(request, 'resources/diet.html', context)


def books(request):
    books = rs.get_all_books_grouped_by_type()

    context = {
        'books_by_type': books,
    }

    return render(request, 'resources/books.html', context)


def hitting_videos(request):
    hitting_videos = rs.get_all_hitting_videos()

    context = {
        'hitting_video_links': hitting_videos
    }

    return render(request, 'resources/hitting-videos.html', context)


def hitting_articles(request):
    hitting_articles = rs.get_all_hitting_articles()

    context = {
        'hitting_article_links': hitting_articles
    }

    return render(request, 'resources/hitting-articles.html', context)