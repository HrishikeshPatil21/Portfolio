from django.db import models


def split(value):
    return [v.strip() for v in value.split(",") if v.strip()]


class Profile(models.Model):
    """Your personal details. Keep just one."""
    name = models.CharField(max_length=100)
    roles = models.CharField(max_length=300, default="Python developer",
                             help_text="Comma-separated. Shown in the typing effect.")
    badges = models.CharField(max_length=200, blank=True,
                              help_text="Up to 4 comma-separated tags floating around your photo.")
    intro = models.TextField(help_text="Short paragraph under your name.")
    contact_text = models.TextField(blank=True, help_text="Short text above the contact form.")
    photo = models.ImageField(upload_to="profile/", blank=True)
    resume = models.FileField(upload_to="resume/", blank=True, help_text="PDF opened by the View resume button.")
    email = models.EmailField()
    github = models.URLField(blank=True)
    linkedin = models.URLField(blank=True)

    @property
    def first_role(self):
        return (split(self.roles) or [""])[0]

    @property
    def initials(self):
        return "".join(w[0] for w in self.name.split()[:2]).upper()

    def badge_list(self):
        return split(self.badges)[:4]

    def __str__(self):
        return self.name


class Stat(models.Model):
    label = models.CharField(max_length=40, help_text="e.g. CGPA")
    value = models.CharField(max_length=10, help_text="A number, e.g. 7.52 or 2")
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["order", "id"]

    def __str__(self):
        return f"{self.value} {self.label}"


class SkillGroup(models.Model):
    title = models.CharField(max_length=60)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["order", "id"]

    def __str__(self):
        return self.title


class Skill(models.Model):
    group = models.ForeignKey(SkillGroup, related_name="skills", on_delete=models.CASCADE)
    name = models.CharField(max_length=60)
    highlight = models.BooleanField(default=False, help_text="Show with the colourful gradient.")

    class Meta:
        ordering = ["id"]

    def __str__(self):
        return self.name


class Project(models.Model):
    title = models.CharField(max_length=120)
    icon = models.CharField(max_length=8, default="💻", help_text="One emoji.")
    description = models.TextField()
    tech = models.CharField(max_length=200, blank=True, help_text="Comma-separated.")
    link = models.URLField(blank=True)
    link_label = models.CharField(max_length=40, default="View on GitHub")
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["order", "id"]

    def tech_list(self):
        return split(self.tech)

    def __str__(self):
        return self.title


class Experience(models.Model):
    role = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    period = models.CharField(max_length=60, help_text="e.g. Oct 2025 to Mar 2026")
    link = models.URLField(blank=True)
    description = models.TextField()
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["order", "id"]

    def __str__(self):
        return f"{self.role}, {self.company}"


class Education(models.Model):
    title = models.CharField(max_length=120, help_text="e.g. B.Tech, Computer Engineering")
    institute = models.CharField(max_length=160)
    detail = models.CharField(max_length=200, blank=True, help_text="e.g. the board")
    period = models.CharField(max_length=40, help_text="e.g. 2022 to 2026")
    score = models.CharField(max_length=40, blank=True, help_text="e.g. CGPA 7.52")
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["order", "id"]
        verbose_name_plural = "education"

    def __str__(self):
        return self.title


class Certificate(models.Model):
    title = models.CharField(max_length=120)
    issuer = models.CharField(max_length=120)
    icon = models.CharField(max_length=8, default="🏅")
    link = models.URLField(blank=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["order", "id"]

    def __str__(self):
        return self.title


class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created"]

    def __str__(self):
        return f"{self.name} ({self.created:%d %b %Y})"
