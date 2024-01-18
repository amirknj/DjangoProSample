# This is Django professional sample projecet

## project was setuped with cookicutter

1- compelete cookiecutter workflow (recommendation: leave project_slug empty) and go inside the project
```
cd projcet
```

2- SetUp venv
```
virtualenv -p python3.10 venv
source venv/bin/activate
```

3- install Dependencies
```
pip install -r requirements_dev.txt
pip install -r requirements.txt
```

4- spin off docker compose
```
docker compose -f docker-compose.dev.yml up -d
```

5- create your env
```
cp .env.example .env
```

6- Create tables
```
python manage.py migrate
```

7- run the project
```
python manage.py runserver
```