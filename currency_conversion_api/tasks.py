from .exchange_api import OpenExchange
# 
#can be configured to user periodic sve wit celery beat #TODO
def save_rates():
    '''
    Create tis task in admin Djano Q subtask ;
    :Fuc : "currency_conversion_api.task.save_rates"
    '''
    rate = OpenExchange() #Refactor to function call/not a good idea 
    rate.save_rates()
