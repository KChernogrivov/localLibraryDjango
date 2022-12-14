# Generated by Django 3.2.15 on 2022-10-04 05:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0008_alter_book_cover'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='preview',
            field=models.TextField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='cover',
            field=models.ImageField(null=True, upload_to='covers/'),
        ),
    ]
