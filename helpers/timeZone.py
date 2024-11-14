from datetime import timezone
from django.forms import ValidationError
import pytz

def change_timezone(self):    
        timezone_header = self.request.headers.get('Time-Zone', 'UTC')

        try:
            
            user_timezone = pytz.timezone(timezone_header)
            timezone.activate(user_timezone)
            
        except pytz.UnknownTimeZoneError:
            raise ValidationError("Invalid timezone provided in headers")

        today = timezone.now()