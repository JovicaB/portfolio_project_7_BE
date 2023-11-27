from datetime import datetime, date

class DateManager:

    def todays_date_str(self):
        todays_date = date.today()
        todays_date_str = todays_date.strftime("%d-%m-%Y")
        return todays_date_str
  
    def format_str_date(self, input_str_date):
        try:
            datetime_object = datetime.strptime(input_str_date, "%d-%m-%Y")
            date_result = datetime_object.date()
            return date_result
        except ValueError as e:
            print(f"Error: {e}")
            return None
