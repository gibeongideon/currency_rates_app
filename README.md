# currency_rates_app


#Sign up as user and access te end points 

DEMO
https://pbpcurrencyratesapi.herokuapp.com

ADMIN
https://pbpcurrencyratesapi.herokuapp.com/admin/
Login Admin to set periodic rates save  

username: admin
password :qqqqq11111

#END POINT1
https://pbpcurrencyratesapi.herokuapp.com/exchange_rate 

Examples

# POST
{
    "base_currency": USD,
    "target_currency": KES,
    "amount": 1
}

# GET/Response

{
    "created_at": "2021-03-09T06:08:40.183299Z",
    "base_currency": 2,
    "target_currency": 1,
    "amount": "1.0000000",
    "rate": "109.70000000"
}




#END POINT2



https://pbpcurrencyratesapi.herokuapp.com/exchange_rate/user/create/
#POST /CREATE user

{
    "username": "admin",
    "first_name": "",
    "last_name": "",
    "email": "admin@convertcurency.com",
    "password": "fKLLtaxzbzvY$T"
}


# for periodic tasks/Save rates to db

use admi to create task

Enter "currency_conversion_api.tasks.save_rates" in FUC & save
_rates can be set to be saved per minute ,ourly etc

ENDPOINDS
admin/
create_user/ [name='users']
user_page [name='user_page']
[name='login']
logout [name='logout']
register [name='register']
password_change/ [name='password_change']
password_change/done/ [name='password_change_done']
password_reset/ [name='password_reset']
password_reset/done [name='password_reset_done']
reset/<uidb64>/<token>/ [name='password_reset_confirm']
reset/done/ [name='password_reset_complete']
exchange_rate
