from django.db import migrations

OLD = "I’m looking for a software engineering role in backend or data-driven development. Send me a message."
NEW = ("I’m looking for a software engineering role in backend or data-driven development, "
       "or a role as a Python developer, AI ML developer or data analyst. Send me a message.")


def update(apps, schema_editor):
    apps.get_model("core", "Profile").objects.filter(contact_text=OLD).update(contact_text=NEW)


class Migration(migrations.Migration):
    dependencies = [("core", "0005_update_profile")]
    operations = [migrations.RunPython(update, migrations.RunPython.noop)]
