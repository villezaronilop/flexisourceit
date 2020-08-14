### Cheat code on Docker

```
$ django-admin startproject config .
$ django-admin startapp <module>
```

For making migration file whenever there a new models
```
$ python manage.py makemigrations
$ python manage.py migrate
```

Create superadmin
```
$ python manage.py createsuperuser --email test@example.com --username admin
```


SQL script to run using root crendential
```
CREATE DATABASE db_flexisourceit;
CREATE USER user_flexisourceit WITH ENCRYPTED PASSWORD 'password_flexisourceit';
GRANT ALL PRIVILEGES ON DATABASE db_flexisourceit TO user_flexisourceit;
```


### Get Users Stock list
`api/users/{usuer_id}/stock`

### Buy and Sell Stock
POST: `api/order/stock`
payload: `{"user":1, "stock": 2, "quantity":3, "action": "sell"}`
*action* [sell, buy]
