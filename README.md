# SIPAuthAPI
Some test work.

## [Installation]
1. `git clone https://github.com/ImranRahimov1995/SIPAuthAPI.git` 
2. `cd SIPAuthAPI`
3. `. ./smart-commands/install.sh`

## [Run]

#### After install - just input standart run cmd:

1. `python manage.py runserver`

###### NOTE: 

If you have some issue with run - don't forget run this cmd en each terminal session `export DJANGO_SETTINGS_MODULE=config.settings.local`

#### Or use my shell script. 

1. `cd SIPAuthAPI/`
2. `. smart-commands/run-server.sh `


## [Endpoints]

### Sign in API

http://127.0.0.1:8000/api/auth/sign-in    [POST]  AllowAny

{
  "username": "admin"
  "password": "admin"
}

______
### Sign up API

http://127.0.0.1:8000/api/auth/sign-up      [POST] AllowAny

{
  "username": 
    "This field is required.",
  
  "password": 
    "This field is required.",
  
  "email": "test@mail.com",
  "phone": "+994705556464"
}
______

### Token delete API

http://127.0.0.1:8000/api/auth/token       [DELETE]  OnlyWithBearerToken

______

### Measure latency API

http://127.0.0.1:8000/api/latency      [GET] OnlyWithBearerToken

_______

### Get User info API

http://127.0.0.1:8000/api/users/info      [GET] OnlyWithBearerToken

### Change User info API

http://127.0.0.1:8000/api/users/info      [PUT] OnlyWithBearerToken


{
    "email": "test@mail.com",
    "phone": "+994705556464"
}

#### NOTE: I was deployed this app in prod .  domain is api

(https://apitest.gopy.space/)

## [Docs]

http://127.0.0.1:8000/api/docs/

http://127.0.0.1:8000/api/docs/redoc/


