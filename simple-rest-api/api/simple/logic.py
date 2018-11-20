from datetime import datetime 
from pytz import timezone
tz = timezone('EST')

def hello():
    return {
        'message': 'Automation for the People',
        'timestamp': datetime.now(tz).timestamp()
        }