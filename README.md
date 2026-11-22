# Django Portfolio

## Run locally
```bash
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate        # also loads your resume details
python manage.py createsuperuser
python manage.py runserver
```
Site: http://127.0.0.1:8000/  Admin: http://127.0.0.1:8000/admin/

## Editing (admin only)
Only the superuser can log in at /admin/ and change anything: Profile (photo, resume PDF, links),
Stats, Skill groups (add skills inline), Projects, Experience (with certificate link), Education, Certificates (each with an optional link).
Contact form messages appear under Contact messages (read-only).

## Deploy on PythonAnywhere
1. Create a free PythonAnywhere account and open a Bash console.
2. Clone the GitHub repository:
   ```bash
   git clone https://github.com/HrishikeshPatil21/Portfolio.git
   cd Portfolio
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   python manage.py migrate
   python manage.py collectstatic --noinput
   ```
3. Create a Django web app in the PythonAnywhere Web tab. Set the source code directory,
   virtualenv, and WSGI application to this project.
4. Replace the generated WSGI file with:
```python
import os
import sys

project_home = "/home/HrishikeshPatil21/Portfolio"
if project_home not in sys.path:
    sys.path.insert(0, project_home)

os.environ["DJANGO_SETTINGS_MODULE"] = "portfolio_site.settings"
os.environ["DJANGO_DEBUG"] = "0"
os.environ["DJANGO_SECRET_KEY"] = "generate-a-long-random-secret"
os.environ["DJANGO_ALLOWED_HOSTS"] = "HrishikeshPatil21.pythonanywhere.com"
os.environ["DJANGO_CSRF_TRUSTED_ORIGINS"] = "https://HrishikeshPatil21.pythonanywhere.com"

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
```
5. Map `/static/` to the project's `staticfiles` directory and `/media/` to the project's
   `media` directory in the PythonAnywhere Web tab.
6. Reload the web app, then create the admin user if needed:
   ```bash
   python manage.py createsuperuser
   ```
