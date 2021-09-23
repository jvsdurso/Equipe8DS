# Generated by Django 3.2.6 on 2021-09-23 20:53

from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Jogador',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('nome', models.CharField(max_length=100)),
                ('is_active', models.BooleanField(default=True, editable=False)),
                ('email', models.CharField(max_length=100, unique=True)),
                ('username', models.CharField(max_length=15, unique=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'jogador',
                'verbose_name_plural': 'jogadores',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('preco_sugerido', models.FloatField(max_length=100)),
                ('qualidade', models.CharField(choices=[(None, '<selecione>'), ('ruim', 'Ruim'), ('pobre', 'Pobre'), ('medio', 'Médio'), ('bom', 'Bom'), ('excelente', 'Excelente')], max_length=100)),
                ('categoria', models.CharField(choices=[(None, '<selecione>'), ('alimentos', 'Alimentos'), ('transporte', 'Transporte'), ('academico', 'Acadêmico'), ('agricultura', 'Agricultura'), ('casa', 'Casa'), ('equipamento', 'Equipamento'), ('luxo', 'Luxo')], max_length=100)),
                ('descricao', models.CharField(max_length=100)),
                ('ativo', models.BooleanField(default=True, editable=False)),
            ],
            options={
                'verbose_name': 'item',
                'verbose_name_plural': 'itens',
            },
        ),
        migrations.CreateModel(
            name='Personagem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('raca', models.CharField(choices=[(None, '<selecione>'), ('humano', 'Humano'), ('anão', 'Anão'), ('dahllan', 'Dahllan'), ('elfo', 'Elfo'), ('goblin', 'Goblin'), ('lefou', 'Lefou'), ('minotauro', 'Minotauro'), ('qareen', 'Qareen'), ('golem', 'Golem'), ('hynne', 'Hynne'), ('kliren', 'Kliren'), ('medusa', 'Medusa'), ('osteon', 'Osteon'), ('sereia/tritão', 'Sereia/Tritão'), ('silfide', 'Silfide'), ('aggelos', 'Aggelos'), ('sufulre', 'Sufulre'), ('trog', 'Trog')], max_length=100, verbose_name='Raça')),
                ('classe', models.CharField(choices=[(None, '<selecione>'), ('mago', 'Mago'), ('bruxo', 'Bruxo'), ('feiticeiro', 'Feiticeiro'), ('bárbaro', 'Bárbaro'), ('bardo', 'Bardo'), ('caçador', 'Caçador'), ('cavaleiro', 'Cavaleiro'), ('clérigo', 'Clérigo'), ('druída', 'Druída'), ('guerreiro', 'Guerreiro'), ('inventor', 'Inventor'), ('ladino', 'Ladino'), ('lutador', 'Lutador'), ('nobre', 'Nobre'), ('paladino', 'Paladino')], max_length=100)),
                ('tipo', models.CharField(choices=[('jogador', 'Jogador'), ('npc', 'NPC')], default='Jogador', editable=False, max_length=100)),
                ('ativo', models.BooleanField(default=True, editable=False)),
                ('dono', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'personagem',
                'verbose_name_plural': 'personagens',
            },
        ),
        migrations.CreateModel(
            name='Cidade',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_cidade', models.CharField(max_length=100)),
                ('tesouro', models.FloatField(max_length=100)),
                ('ativo', models.BooleanField(default=True, editable=False)),
                ('governante', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bot.personagem')),
            ],
        ),
    ]