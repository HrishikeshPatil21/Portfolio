from django.db import migrations

G1 = "https://drive.google.com/file/d/1oIWi4CF2seA2qtDFdRtmRKcpBDvBaSw1/view?usp=sharing"
G2 = "https://drive.google.com/file/d/1bPqFzkhiOlowFEkkZlkmOQJ9eT-IOLFO/view?usp=sharing"
REPO = "https://github.com/HrishikeshPatil21/"


def load(apps, schema_editor):
    g = apps.get_model
    Cert, Edu, Exp, Proj = g("core", "Certificate"), g("core", "Education"), g("core", "Experience"), g("core", "Project")
    Cert.objects.filter(title="B.Tech, Computer Engineering").delete()
    icons = {"Tableau data visualization": ("📊", 1), "Ethical hacking": ("🛡️", 2), "C programming": ("💻", 3)}
    for t, (ic, o) in icons.items():
        Cert.objects.filter(title=t).update(icon=ic, order=o)
    if not Cert.objects.filter(title="Python developer internship").exists():
        Cert.objects.create(title="Python developer internship", issuer="Completion certificate, GoldenBird Education", icon="🐍", link=G1, order=0)
    Exp.objects.filter(company="GoldenBird Education").update(link=G1)
    Exp.objects.filter(company="AIar Innovations").update(link=G2)
    Proj.objects.filter(title="Realtime face attendance system").update(link=REPO + "Real-Time-Face-Attendace-System-Using-AI-")
    Proj.objects.filter(title="Banking management system").update(link=REPO + "Bank-Mangement-System")
    if not Edu.objects.exists():
        rows = [
            ("B.Tech, Computer Engineering", "D.Y. Patil University, Pune (Ambi)", "", "2022 to 2026", "CGPA 7.52"),
            ("HSC (Class XII)", "S.M. Dr. D.Y. Patil Junior College, Pune", "Maharashtra State Board of Secondary and Higher Secondary Education", "2022", ""),
            ("Secondary (Class X)", "Saraswasti Vishwa Vidyalaya National School, Pune", "Central Board of Secondary Education (CBSE)", "2020", ""),
        ]
        for i, (t, inst, d, p, s) in enumerate(rows):
            Edu.objects.create(title=t, institute=inst, detail=d, period=p, score=s, order=i)


class Migration(migrations.Migration):
    dependencies = [("core", "0003_education_certificate")]
    operations = [migrations.RunPython(load, migrations.RunPython.noop)]
