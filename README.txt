# Django Rest Application

_Using Sqlite for serving data_

##Run following commands to setup
``` 
    pip install -r requirements.txt
    python manage.py runserver
```
##Access API
*Open your browser and go to 127.0.0.1:8000

##Admin control panel at /admin**
```
    Username: kush
    Password: kushpassword
```
##Commands
```
    127.0.0.1:8000/count
    127.0.0.1:8000/stats
    127.0.0.1:8000/list
    127.0.0.1:8000/admin
```
##Search

Examples
```
    127.0.0.1:8000/search/?name=Siege of Winterfell
    127.0.0.1:8000/search/?king=Stannis Baratheon
    127.0.0.1:8000/search/?location=Winterfell
    127.0.0.1:8000/search/?type=siege
```
Syntax
```
    127.0.0.1:8000/search/?name=<name>
    127.0.0.1:8000/search/?king=<attacker_king>
    127.0.0.1:8000/search/?location=<location>
    127.0.0.1:8000/search/?type=<battle_type>
```