from django.db import models


class Book(models.Model):
    book_id = models.AutoField(primary_key=True)
    book_type_id = models.ForeignKey('BookType', db_column='book_type_id',
                                     verbose_name='Book Type',
                                     related_name='books',
                                     on_delete=models.PROTECT)
    name = models.CharField(max_length=50)
    author = models.CharField(max_length=30)
    amazon_url = models.URLField(max_length=125)
    image = models.ImageField(upload_to='resources-book-images')
    order = models.PositiveSmallIntegerField(unique=True)

    class Meta:
        db_table = "Book"
        verbose_name = "Book"
        verbose_name_plural = "Books"
        ordering = ['order']

    def __str__(self):
        return self.name


class BookType(models.Model):
    book_type_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    order = models.PositiveSmallIntegerField(unique=True)

    class Meta:
        db_table = "BookType"
        verbose_name = "Book Type"
        verbose_name_plural = "Book Types"
        ordering = ['order']

    def __str__(self):
        return self.name


class WebsiteLink(models.Model):
    website_link_id = models.AutoField(primary_key=True)
    website_link_type_id = models.ForeignKey('WebsiteLinkType', db_column='website_link_type_id',
                                     verbose_name='Website Link Type',
                                     related_name='website_links',
                                     on_delete=models.PROTECT)
    name = models.CharField(max_length=100)
    url = models.URLField(max_length=150)
    order = models.PositiveSmallIntegerField(unique=True)
    image = models.ImageField(upload_to='resources-website-link-images', blank=True, null=True)
    order = models.PositiveSmallIntegerField(unique=True)

    class Meta:
        db_table = "WebsiteLink"
        verbose_name = "Website Link"
        verbose_name_plural = "Website Links"
        ordering = ['order']

    def __str__(self):
        return self.name


class WebsiteLinkType(models.Model):
    website_link_type_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    is_video = models.BooleanField(default=False)

    class Meta:
        db_table = "WebsiteLinkType"
        verbose_name = "Website Link Type"
        verbose_name_plural = "Website Link Types"

    def __str__(self):
        return self.name


class Document(models.Model):
    document_id = models.AutoField(primary_key=True)
    document_type_id = models.ForeignKey('DocumentType', db_column='document_type_id',
                                         verbose_name='Document Type',
                                         related_name='documents',
                                         on_delete=models.PROTECT)
    name = models.CharField(max_length=50)
    file = models.FileField(upload_to='resources-documents')
    image = models.ImageField(upload_to='resources-documents-images')
    order = models.PositiveSmallIntegerField(unique=True)

    class Meta:
        db_table = "Document"
        verbose_name = "Document"
        verbose_name_plural = "Documents"
        ordering = ['order']

    def __str__(self):
        return self.name


class DocumentType(models.Model):
    document_type_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length = 30)

    class Meta:
        db_table = "DocumentType"
        verbose_name = "Document Type"
        verbose_name_plural = "Document Types"

    def __str__(self):
        return self.name
