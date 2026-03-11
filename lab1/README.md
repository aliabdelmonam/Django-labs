# Lab 1 — Lol's Kitchen 🍴
> Django Course | First Django App

A simple menu listing page built with Django and dummy data. No database.
---

## What it does

- Displays a list of menu items (name, category, price, availability)
- Search by name
- Filter by category

## Stack

- Python / Django
- HTML + CSS (no frameworks)
- Dummy data (list of dictionaries — no models/DB)

## Run it

```bash
pip install django
python manage.py runserver
```

Then visit `http://127.0.0.1:8000/`

## Structure

```
lab/
├── meals/
│   ├── views.py       # logic + dummy data
│   ├── urls.py        # routing
│   └── templates/
        └── meals/
│           └── index.html # the page
            └── style.css 
└── lab/
    └── urls.py        # project urls
```

## Concepts practiced

- Django app structure
- URL routing
- Views & context
- Django template tags (`{{ }}`, `{% for %}`, `{% if %}`)
- GET requests & query parameters
