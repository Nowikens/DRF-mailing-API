# Mailing API build with Django Rest Framework
Api lets You define Mailbox from which email will be sent, Template which is the content of you email and Email which sets adresees.

# Used components:
- [Python](https://www.python.org/) 3.8.3
- [Django](https://www.djangoproject.com/) 3.1.2
- [Django Rest Framework](https://www.django-rest-framework.org/) 3.12.1
- [Celery](https://docs.celeryproject.org/en/stable/#) 5.0.1
- [Redis](https://redis.io/)
- [PostgreSQL](https://www.postgresql.org/)
- [psycopg2](https://www.psycopg.org/) 2.8.6
- [Django Environ](https://django-environ.readthedocs.io/en/latest) 0.4.5
- [Django Filter](https://django-filter.readthedocs.io/en/stable) 2.4.0

# Check it out
#### 1. Create virtual environment
```bash
# Install virtualenv
pip install virtualenv
# Create virtualenv
virtualenv virtualenv_name
# Activate
./virtualenv_name/scripts/activate
# Or
./virtualenv_name/scripts/activate.bat
```
#### 2. Install and configure PostgreSQL
Django girls has great tutorial [HERE](https://tutorial-extensions.djangogirls.org/en/optional_postgresql_installation)
#### 3. Install Redis
[For linux/mac](https://redis.io/download) - Download needed files, scroll downand follow instructions.
[For windows](https://github.com/microsoftarchive/redis/releases/tag/win-3.0.504) - For windows You have to download ` Redis-x64-3.0.504.zip` file. Extract containing files and run `redis-server.exe`.
#### 4. Clone repository and install requirements
```bash
# Clone repository
git clone https://github.com/Nowikens/DRF-mailing-API
# Go to project folder
cd DRF-mailing-API
# Install required packages
pip install -r requirements.txt
```
#### 3. Configurations
1. .env file
**Note that there can't be any space between variable and value.**
SECRET_KEY=supersecretvalue     :white-check-mark:
SECRET_KEY = supersecretvalue   :x:
**To get You new secret key use [This site](https://djecrety.ir/), or create in any other way 50 characters random string**
```
SECRET_KEY=Your_Secret_Key
DEBUG=TRUE                  # For testing and development purposes

DB_NAME=Your_DB_NAME
DB_USER=Your_DB_USER
DB_PASSWORD=Your_DB_Password
DB_HOST=Your_DB_Host        # Default: localhost or 127.0.0.1
DB_PORT=Your_DB_Port        # Default: 5432
```

2. Migrate models 
```bash
# Make migrations
python manage.py makemigrations
# Migrate
python manage.py migrate
```
# 4. Using 









