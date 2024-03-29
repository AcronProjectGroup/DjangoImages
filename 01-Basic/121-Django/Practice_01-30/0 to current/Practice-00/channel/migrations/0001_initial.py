# Generated by Django 4.2.2 on 2023-07-22 11:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('userauth', '0004_alter_user_last_login'),
    ]

    operations = [
        migrations.CreateModel(
            name='Channel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='Media',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('size', models.IntegerField()),
                ('format', models.CharField(max_length=60)),
                ('type', models.CharField(max_length=60)),
                ('duration', models.IntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.IntegerField(null=True)),
                ('title', models.CharField(max_length=200, null=True)),
                ('summary', models.CharField(max_length=400, null=True)),
                ('content', models.CharField(max_length=1000)),
                ('is_vip', models.BooleanField(default=False)),
                ('channel_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='channel.channel')),
                ('media', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='channel.media')),
            ],
        ),
        migrations.CreateModel(
            name='Membership',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.CharField(choices=[('admin', 'Admin'), ('normal', 'Normal'), ('vip', 'Vip')], default='normal', max_length=10)),
                ('channel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='channel.channel')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='userauth.user')),
            ],
        ),
        migrations.AddField(
            model_name='channel',
            name='members',
            field=models.ManyToManyField(related_name='followings', through='channel.Membership', to='userauth.user'),
        ),
        migrations.AddField(
            model_name='channel',
            name='owner_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='userauth.user'),
        ),
    ]
