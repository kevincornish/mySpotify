# Generated by Django 4.2.1 on 2023-06-07 21:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Album",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("album_name", models.CharField(max_length=100)),
                ("artist_name", models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name="Artist",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name="History",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("ts", models.DateTimeField(unique=True)),
                ("username", models.CharField(max_length=30)),
                ("platform", models.CharField(max_length=30)),
                ("ms_played", models.IntegerField()),
                ("conn_country", models.CharField(max_length=30)),
                ("ip_addr_decrypted", models.CharField(max_length=30)),
                ("user_agent_decrypted", models.CharField(max_length=30, null=True)),
                ("master_metadata_track_name", models.CharField(max_length=100)),
                ("master_metadata_album_artist_name", models.CharField(max_length=100)),
                ("master_metadata_album_album_name", models.CharField(max_length=100)),
                ("spotify_track_uri", models.CharField(max_length=30, null=True)),
                ("episode_name", models.CharField(max_length=30, null=True)),
                ("spotify_episode_uri", models.CharField(max_length=30, null=True)),
                ("reason_start", models.CharField(max_length=30)),
                ("reason_end", models.CharField(max_length=30)),
                ("shuffle", models.BooleanField(default=False)),
                ("skipped", models.CharField(max_length=30, null=True)),
                ("offline", models.BooleanField(default=False)),
                ("offline_timestamp", models.CharField(max_length=30)),
                ("incognito_mode", models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name="Track",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("track_name", models.CharField(max_length=100)),
                ("album_name", models.CharField(max_length=100)),
                ("artist_name", models.CharField(max_length=100)),
            ],
        ),
    ]