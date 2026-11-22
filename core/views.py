from django.contrib import messages
from django.shortcuts import redirect, render

from .forms import ContactForm
from .models import Certificate, Education, Experience, Profile, Project, SkillGroup, Stat

FALLBACK = Profile(name="Your Name", roles="Python developer", intro="Add your details in /admin.", email="you@example.com")


def home(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Message sent. Thank you!")
            return redirect("/#contact")
    else:
        form = ContactForm()
    return render(request, "core/home.html", {
        "profile": Profile.objects.first() or FALLBACK,
        "stats": Stat.objects.all(),
        "groups": SkillGroup.objects.prefetch_related("skills"),
        "projects": Project.objects.all(),
        "jobs": Experience.objects.all(),
        "educations": Education.objects.all(),
        "certificates": Certificate.objects.all(),
        "form": form,
    })
