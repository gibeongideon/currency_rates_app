# currency_rates_app

#Sin up as user and access te end points 
#Rates are periodially saved by a worker/TODO do to it in settin

#END POINT1
http://127.0.0.1:8000/api 

Examples

#POST
{
    "base_currency": USD,
    "target_currency": KES,
    "amount": 1
}

#GET/Response

{
    "created_at": "2021-03-09T06:08:40.183299Z",
    "base_currency": 2,
    "target_currency": 1,
    "amount": "1.0000000",
    "rate": "109.70000000"
}




#END POINT2



http://127.0.0.1:8000/user/create/
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