# Generated by Django 3.2.3 on 2021-05-30 19:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BookType',
            fields=[
                ('book_type_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30)),
                ('order', models.PositiveSmallIntegerField(unique=True)),
            ],
            options={
                'verbose_name': 'Book Type',
                'verbose_name_plural': 'Book Types',
                'db_table': 'BookType',
                'ordering': ['order'],
            },
        ),
        migrations.CreateModel(
            name='DocumentType',
            fields=[
                ('document_type_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30)),
            ],
            options={
                'verbose_name': 'Document Type',
                'verbose_name_plural': 'Document Types',
                'db_table': 'DocumentType',
            },
        ),
        migrations.CreateModel(
            name='WebsiteLinkType',
            fields=[
                ('website_link_type_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30)),
                ('is_video', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'Website Link Type',
                'verbose_name_plural': 'Website Link Types',
                'db_table': 'WebsiteLinkType',
            },
        ),
        migrations.CreateModel(
            name='WebsiteLink',
            fields=[
                ('website_link_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=75)),
                ('url', models.URLField(max_length=100)),
                ('image', models.ImageField(blank=True, null=True, upload_to='resources-website-link-images')),
                ('order', models.PositiveSmallIntegerField(unique=True)),
                ('website_link_type_id', models.ForeignKey(db_column='website_link_type_id', on_delete=django.db.models.deletion.PROTECT, related_name='website_links', to='resources.websitelinktype', verbose_name='Website Link Type')),
            ],
            options={
                'verbose_name': 'Website Link',
                'verbose_name_plural': 'Website Links',
                'db_table': 'WebsiteLink',
                'ordering': ['order'],
            },
        ),
        migrations.CreateModel(
            name='Document',
            fields=[
                ('document_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('file', models.FileField(upload_to='resources-documents')),
                ('image', models.ImageField(upload_to='resources-documents-images')),
                ('order', models.PositiveSmallIntegerField(unique=True)),
                ('document_type_id', models.ForeignKey(db_column='document_type_id', on_delete=django.db.models.deletion.PROTECT, related_name='documents', to='resources.documenttype', verbose_name='Document Type')),
            ],
            options={
                'verbose_name': 'Document',
                'verbose_name_plural': 'Documents',
                'db_table': 'Document',
                'ordering': ['order'],
            },
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('book_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('author', models.CharField(max_length=30)),
                ('amazon_url', models.URLField(max_length=125)),
                ('image', models.ImageField(upload_to='resources-book-images')),
                ('order', models.PositiveSmallIntegerField(unique=True)),
                ('book_type_id', models.ForeignKey(db_column='book_type_id', on_delete=django.db.models.deletion.PROTECT, related_name='books', to='resources.booktype', verbose_name='Book Type')),
            ],
            options={
                'verbose_name': 'Book',
                'verbose_name_plural': 'Books',
                'db_table': 'Book',
                'ordering': ['order'],
            },
        ),
    ]
