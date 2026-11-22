from django.db import migrations


def seed(apps, schema_editor):
    g = apps.get_model
    g("core", "Profile").objects.create(
        name="Hrishikesh Patil",
        roles="Python developer, Django developer, ML and LangChain builder",
        badges="Python, Django, LangChain, ML",
        intro="Final-year Computer Engineering student in Pune. I build Django web apps, machine learning projects and AI tools, from the database to the dashboard.",
        contact_text="I’m looking for a software engineering role in backend or data-driven development. Send me a message.",
        resume="resume/Hrishikesh_Patil_Resume.pdf",
        email="hrishpatil21304@gmail.com",
        github="https://github.com/HrishikeshPatil21",
        linkedin="https://linkedin.com/in/hrishikesh-patil21",
    )
    for i, (v, l) in enumerate([("7.52", "CGPA"), ("2", "Internships"), ("2", "Full projects"), ("4", "Certifications")]):
        g("core", "Stat").objects.create(value=v, label=l, order=i)
    groups = [
        ("Languages and tools", [("Python", 1), ("Django", 1), ("C", 0), ("HTML", 0), ("CSS", 0), ("MySQL", 0), ("Git", 0)]),
        ("AI and data", [("Machine learning", 1), ("LangChain", 1), ("Prompt engineering", 0), ("Supervised learning", 0), ("Unsupervised learning", 0), ("Pandas", 0), ("NumPy", 0)]),
        ("Analytics and people", [("Excel", 0), ("Tableau", 0), ("Communication", 0), ("Leadership", 0), ("Critical thinking", 0), ("Quick learner", 0)]),
    ]
    for i, (title, skills) in enumerate(groups):
        grp = g("core", "SkillGroup").objects.create(title=title, order=i)
        for n, h in skills:
            g("core", "Skill").objects.create(group=grp, name=n, highlight=bool(h))
    gh = "https://github.com/HrishikeshPatil21"
    g("core", "Project").objects.create(order=0, icon="📷", title="Realtime face attendance system", link=gh,
        tech="Python, Django, LBPH, LLM tools",
        description="My final-year project. It recognises faces in real time, with a desktop app and a web dashboard for search, filters and CSV export. It flags low attendance, builds monthly Excel reports and has an AI chatbot for staff questions.")
    g("core", "Project").objects.create(order=1, icon="🏦", title="Banking management system", link=gh,
        tech="Python, OOP, File handling",
        description="A console banking app with accounts, deposits, withdrawals and transfers. It is built in layers (models, services, file handler) with file-based storage and a full transaction log.")
    g("core", "Experience").objects.create(order=0, role="AI & ML developer intern", company="AIar Innovations", period="Oct 2025 to Mar 2026",
        description="Built and optimised Python and Django backend modules for AI-powered workflows, added basic machine learning logic for automated decisions, and tested, debugged and documented backend scripts with the team.")
    g("core", "Experience").objects.create(order=1, role="Python developer intern", company="GoldenBird Education", period="Jun 2025 to Sep 2025",
        description="Shipped several Python projects with modular OOP code, and cut latency by optimising legacy code, indexing the database and writing efficient MySQL queries.")
    for i, (t, s) in enumerate([("B.Tech, Computer Engineering", "D.Y. Patil University, Pune, 2022 to 2026"),
                                ("Tableau data visualization", "Spartificial Pvt. Ltd."),
                                ("Ethical hacking", "Eduskill Academy"),
                                ("C programming", "SevenMentors Training Institute")]):
        g("core", "Credential").objects.create(order=i, title=t, issuer=s)


class Migration(migrations.Migration):
    dependencies = [("core", "0001_initial")]
    operations = [migrations.RunPython(seed, migrations.RunPython.noop)]
