### McDermott Network

---

Base app for authentication and API requests

To run this app do:

```
virtualenv venv
source venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

After someone pushes, you may need to run:

```
# If a dependency is added:
pip install -r requirements.txt
# If a model is changed:
python manage.py makemigrations
python manage.py migrate
```
