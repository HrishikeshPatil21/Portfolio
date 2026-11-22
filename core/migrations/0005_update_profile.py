from django.db import migrations


def update(apps, schema_editor):
    p = apps.get_model("core", "Profile").objects.first()
    if not p:
        return
    old = "Final-year Computer Engineering student in Pune."
    if p.intro.startswith(old):
        p.intro = p.intro.replace(old, "Computer Engineering graduate from Pune.", 1)
    if "ML and LangChain builder" in p.roles:
        p.roles = "Python developer, Django developer, AI ML developer, Data Scientist, Data Analyst"
    if not p.photo:
        p.photo = "profile/hrishikesh.jpg"
    p.save()


class Migration(migrations.Migration):
    dependencies = [("core", "0004_load_education_links")]
    operations = [migrations.RunPython(update, migrations.RunPython.noop)]
