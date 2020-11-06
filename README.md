# Mailing API built with Django Rest Framework
Api lets You send Email from Mailbox defined by You

# ENDPOINTS
Endpoint            |Method            |Result
-- | -- | --
`api/mailbox/`|***GET, POST***| GET all, POST new
`api/mailbox/:id/`|***GET, PUT, PATCH, DELETE***|GET one, UPDATE one, DELETE one
| |
`api/template/`|***GET, POST***| GET all, POST new
`api/template/:id/`|***GET, PUT, PATCH, DELETE*** |GET one, UPDATE one, DELETE one
 | |
`api/email/`|***GET, POST***|GET all, POST new and try to send it
# Post requests patterns
**Mailbox**
```
{
    "host": "<smtp host>",                   //string
    "port": <port number>,                   //int
    "login": "<login to smtp serwer>",       //string
    "password": "<password to smtp serwer>", //string
    "email_from": "<name of sender>",        //email string
    "use_ssl": <true/false>,                 //boolean
    "is_active": <true/false>                //boolean
}
```
**Template**
```
{
    "subject": "",                       //string
    "text": "",                          //string
    "attachment": <path to attachment>   //string
}
```
**EMAIL**
```
{
    "to": [<list of email adresses>],   //each element is email string
    "cc": [<list of email adresses>],   //each element is email string
    "bcc": [<list of email adresses>],  //each element is email string
    "reply_to": "(email_adress>",       //email string
    "mailbox": "<id>",                  //string
    "template": "<id>"                  //string
}
```
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
Django Girls has great tutorial [HERE](https://tutorial-extensions.djangogirls.org/en/optional_postgresql_installation)
#### 3. Install Redis
[For linux/mac](https://redis.io/download) - Download needed files, scroll downand follow instructions.\
[For windows](https://github.com/microsoftarchive/redis/releases/tag/win-3.0.504) - For windows You have to download ` Redis-x64-3.0.504.zip` file. Extract containing files, place of extraction does not matter.

You can of course use other Celery broker if You like, you can find them [HERE](https://docs.celeryproject.org/en/stable/getting-started/brokers/)
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
**I. `.env` file**\
Create `.env` file in the `root` folder.
**Note that there can't be any space between variable and value.**\
SECRET_KEY=supersecretvalue- - :heavy_check_mark:\
SECRET_KEY = supersecretvalue - :no_entry_sign:\
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

**II. Migrate models**
```bash
# Make migrations
python manage.py makemigrations
# Migrate
python manage.py migrate
```


# 4. Using
You need two consoles opened to run this project: first for Celery tasks, and second for Django itself. Make sure Virtual Environment is activated on both consoles.\
**I. Run Redis and Celery**\
To run Redis server run `redis-server` on Linux/Mac or `redis-server.exe` on Windows.\
To run Celery type in Your console:
```bash
celery -A root worker -l INFO
# Sometimes that does not work and instead you need to run:
python -m celery -A root worker -l INFO
```


**II. Run Django app**
Run Django server
```bash
python manage.py runserver
```
Open Django app in the browser, or send request through Postman or Curl to this adress:\
`localhost:8000/api`

**III. Sending emails**
To send email You first need to create Mailbox and Template. Follow post requests schemas to send email.
