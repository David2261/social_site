# social_site
https://img.shields.io/github/last-commit/David2261/social_site
![GitHub Light](https://github.com/github-light.png#gh-dark-mode-only)

## What I did in the project
*The project is a light form of messenger (similar to reddit);
In which you can create an article and choose a topic, and leave a comment;
You can login or make new account;
A form for the api has been created;*

## When writing this manual, I used:
- windows ![Windows](https://img.shields.io/badge/Windows-0078D6?style=for-the-badge&logo=windows&logoColor=white) 10
- python ![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) 3.7
- django ![Django](https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white) 3.0
- drf ![DjangoREST](https://img.shields.io/badge/DJANGO-REST-ff1709?style=for-the-badge&logo=django&logoColor=white&color=ff1709&labelColor=gray) 3.11
- docker ![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white) 20.10.12
- docker compose 2.2.3

## Getting Started
- First you need to create an environment:
  - For that you need install virtualenv
    - `pip install virtualenv`
- After that you can create your new environment:
`virtualenv venv`
- Second you need activate env
- If you using windows, you can activate env like me:
`venv\Scripts\activate`
- Thirt you need install all pip's which contain in requirements.txt:
  - `pip install -r requirements`

## Nice your env created, right now we can work with project:
- First we make our migrations:
1. `python manage.py makemigrations`
2. `python manage.py migrate`
3. `python manage.py runserver`

## Main page:
![alt text](static/images/main_page.png "Main Page")