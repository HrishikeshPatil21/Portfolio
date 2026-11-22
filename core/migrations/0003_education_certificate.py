from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [("core", "0002_seed")]
    operations = [
        migrations.RenameModel("Credential", "Certificate"),
        migrations.AlterModelOptions("certificate", options={"ordering": ["order", "id"]}),
        migrations.AddField("certificate", "icon", models.CharField(default="🏅", max_length=8)),
        migrations.AddField("certificate", "link", models.URLField(blank=True)),
        migrations.AddField("experience", "link", models.URLField(blank=True)),
        migrations.CreateModel(
            name="Education",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("title", models.CharField(help_text="e.g. B.Tech, Computer Engineering", max_length=120)),
                ("institute", models.CharField(max_length=160)),
                ("detail", models.CharField(blank=True, help_text="e.g. the board", max_length=200)),
                ("period", models.CharField(help_text="e.g. 2022 to 2026", max_length=40)),
                ("score", models.CharField(blank=True, help_text="e.g. CGPA 7.52", max_length=40)),
                ("order", models.PositiveIntegerField(default=0)),
            ],
            options={"verbose_name_plural": "education", "ordering": ["order", "id"]},
        ),
    ]
