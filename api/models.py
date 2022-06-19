# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Camion(models.Model):
    noimmatric = models.CharField(db_column='NoImmatric', primary_key=True, max_length=10)  # Field name made lowercase.
    dateachat = models.DateField(db_column='DateAchat', blank=True, null=True)  # Field name made lowercase.
    nomodele = models.ForeignKey('Modele', models.DO_NOTHING, db_column='NoModele')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'camion'


class Centretraitement(models.Model):
    nocentre = models.AutoField(db_column='NoCentre', primary_key=True)  # Field name made lowercase.
    nomcentre = models.CharField(db_column='NomCentre', max_length=100, blank=True, null=True)  # Field name made lowercase.
    noruecentre = models.IntegerField(db_column='NoRueCentre', blank=True, null=True)  # Field name made lowercase.
    ruecentre = models.CharField(db_column='RueCentre', max_length=200, blank=True, null=True)  # Field name made lowercase.
    cpostalcentre = models.IntegerField(db_column='CpostalCentre', blank=True, null=True)  # Field name made lowercase.
    villecentre = models.CharField(db_column='VilleCentre', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'centretraitement'


class Demande(models.Model):
    nodemande = models.AutoField(db_column='NoDemande', primary_key=True)  # Field name made lowercase.
    datedemande = models.DateField(db_column='DateDemande', blank=True, null=True)  # Field name made lowercase.
    dateenlevement = models.DateField(db_column='DateEnlevement', blank=True, null=True)  # Field name made lowercase.
    web_o_n = models.CharField(db_column='Web_O_N', max_length=1, blank=True, null=True)  # Field name made lowercase.
    siret = models.ForeignKey('Entreprise', models.DO_NOTHING, db_column='Siret')  # Field name made lowercase.
    notournee = models.ForeignKey('Tournee', models.DO_NOTHING, db_column='NoTournee', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'demande'


class Detaildemande(models.Model):
    quantiteenlevee = models.IntegerField(db_column='QuantiteEnlevee')  # Field name made lowercase.
    remarque = models.CharField(db_column='Remarque', max_length=100, blank=True, null=True)  # Field name made lowercase.
    nodemande = models.OneToOneField(Demande, models.DO_NOTHING, db_column='NoDemande', primary_key=True)  # Field name made lowercase.
    notypedechet = models.ForeignKey('Typedechet', models.DO_NOTHING, db_column='NoTypeDechet')  # Field name made lowercase.
    noville = models.ForeignKey('Ville', models.DO_NOTHING, db_column='NoVille')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'detaildemande'
        unique_together = (('nodemande', 'notypedechet', 'noville'),)


class Detaildepot(models.Model):
    quantitedeposee = models.IntegerField(db_column='QuantiteDeposee')  # Field name made lowercase.
    notournee = models.OneToOneField('Tournee', models.DO_NOTHING, db_column='NoTournee', primary_key=True)  # Field name made lowercase.
    notypedechet = models.ForeignKey('Typedechet', models.DO_NOTHING, db_column='NoTypeDechet')  # Field name made lowercase.
    nocentre = models.ForeignKey(Centretraitement, models.DO_NOTHING, db_column='NoCentre')  # Field name made lowercase.
    noville = models.ForeignKey('Ville', models.DO_NOTHING, db_column='NoVille')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'detaildepot'
        unique_together = (('notournee', 'notypedechet', 'nocentre', 'noville'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Employe(models.Model):
    noemploye = models.AutoField(db_column='NoEmploye', primary_key=True)  # Field name made lowercase.
    nom = models.CharField(db_column='Nom', max_length=50, blank=True, null=True)  # Field name made lowercase.
    prenom = models.CharField(db_column='Prenom', max_length=50, blank=True, null=True)  # Field name made lowercase.
    datenaiss = models.DateField(db_column='dateNaiss', blank=True, null=True)  # Field name made lowercase.
    dateembauche = models.DateField(db_column='dateEmbauche', blank=True, null=True)  # Field name made lowercase.
    salaire = models.DecimalField(db_column='Salaire', max_digits=8, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    nofonction = models.ForeignKey('Fonction', models.DO_NOTHING, db_column='NoFonction', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'employe'


class Entreprise(models.Model):
    siret = models.BigIntegerField(db_column='Siret', primary_key=True)  # Field name made lowercase.
    raisonsociale = models.CharField(db_column='RaisonSociale', max_length=50)  # Field name made lowercase.
    norueentr = models.IntegerField(db_column='NoRueEntr', blank=True, null=True)  # Field name made lowercase.
    rueentr = models.CharField(db_column='RueEntr', max_length=200, blank=True, null=True)  # Field name made lowercase.
    cpostalentr = models.IntegerField(db_column='CpostalEntr', blank=True, null=True)  # Field name made lowercase.
    villeentr = models.CharField(db_column='VilleEntr', max_length=50, blank=True, null=True)  # Field name made lowercase.
    notel = models.CharField(db_column='NoTel', max_length=10, blank=True, null=True)  # Field name made lowercase.
    contact = models.CharField(db_column='Contact', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'entreprise'


class Fonction(models.Model):
    nofonction = models.AutoField(db_column='NoFonction', primary_key=True)  # Field name made lowercase.
    nomfonction = models.CharField(db_column='NomFonction', max_length=50)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'fonction'


class Marque(models.Model):
    nomarque = models.AutoField(db_column='NoMarque', primary_key=True)  # Field name made lowercase.
    nommarque = models.CharField(db_column='NomMarque', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'marque'


class Modele(models.Model):
    nomodele = models.AutoField(db_column='NoModele', primary_key=True)  # Field name made lowercase.
    nommodele = models.CharField(db_column='NomModele', max_length=100, blank=True, null=True)  # Field name made lowercase.
    nomarque = models.ForeignKey(Marque, models.DO_NOTHING, db_column='NoMarque', blank=True, null=True)  # Field name made lowercase.
    maxenlevement = models.IntegerField(db_column='MaxEnlevement', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'modele'


class Tournee(models.Model):
    notournee = models.AutoField(db_column='NoTournee', primary_key=True)  # Field name made lowercase.
    datetournee = models.DateField(db_column='DateTournee', blank=True, null=True)  # Field name made lowercase.
    noimmatric = models.ForeignKey(Camion, models.DO_NOTHING, db_column='NoImmatric')  # Field name made lowercase.
    noemploye = models.ForeignKey(Employe, models.DO_NOTHING, db_column='NoEmploye')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tournee'


class Typedechet(models.Model):
    notypedechet = models.AutoField(db_column='NoTypeDechet', primary_key=True)  # Field name made lowercase.
    nomtypedechet = models.CharField(db_column='NomTypeDechet', max_length=50, blank=True, null=True)  # Field name made lowercase.
    niv_danger = models.IntegerField(db_column='Niv_danger', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'typedechet'


class Ville(models.Model):
    noville = models.AutoField(db_column='NoVille', primary_key=True)  # Field name made lowercase.
    nomville = models.CharField(db_column='NomVille', max_length=100)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ville'
