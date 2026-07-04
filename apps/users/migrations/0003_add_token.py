from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_user_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='token',
            field=models.CharField(
                max_length=256,
                unique=True,
                null=True,
                blank=True
            ),
        ),
    ]