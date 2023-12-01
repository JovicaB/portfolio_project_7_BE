### FINISHED
from datetime import datetime, date, timedelta


class DateManager:

    def todays_date_str(self) -> str: 
        """ Returns the today's date.

        Returns:
            Today's date: (str)
        """
        todays_date = date.today()
        todays_date_str = todays_date.strftime("%d-%m-%Y")
        return todays_date_str
    
    def tomorrow_date_str(self, date_str: str) -> str:
        """ Calculates and returns the next working date.

        Args:
            date_str (str): e.g.'29-11-2023'

        Returns:
            Next working date: (str)
        """
        date_object = datetime.strptime(date_str, "%d-%m-%Y")
        todays_date = date_object.date()

        next_working_day = todays_date + timedelta(days=1)
        while next_working_day.weekday() >= 5:
            next_working_day += timedelta(days=1)

        todays_date_str = next_working_day.strftime("%d-%m-%Y")
        return todays_date_str
  
    def format_to_date_objet(self, input_str_date: str) -> date:
        """Converts date string to date object

        Args:
            input_str_date (str): _description_

        Returns:
            date object
        """
        try:
            datetime_object = datetime.strptime(input_str_date, "%d-%m-%Y")
            date_result = datetime_object.date()
            return date_result
        except ValueError as e:
            print(f"Error: {e}")
            return None
        
    def is_workday(self, date: str) -> bool:
        """Checks if provided date is workday

        Args:
            date (str): date (e.g 01-12-2023)

        Returns:
            bool: if arg date string workday True, if not False
        """
        date_object = datetime.strptime(date, "%d-%m-%Y")
        if 0 <= date_object.weekday() <= 4:
            return True
        else:
            return False

## USAGE
# class_instance = DateManager()

# print(class_instance.todays_date_str())
# data = '25-11-2023'
# print(class_instance.tomorrow_date_str(data))
# print(class_instance.format_to_date_objet(data))
# print(class_instance.is_date_workday(data))





