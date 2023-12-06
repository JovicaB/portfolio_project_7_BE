from datetime import datetime, date, timedelta


class DateUtilities:

    def todays_date_str(self) -> str: 
        """ Returns the today's date.

        Returns:
            Today's date: (str)
        """
        todays_date = date.today()
        todays_date_str = todays_date.strftime("%Y-%m-%d")
        return todays_date_str
    
    def year_ago_date_str(self, date_str: str) -> str:
        """ Calculates and returns the next working date.

        Args:
            date_str (str): e.g.'29-11-2023'

        Returns:
            Next working date: (str)
        """
        date_object = datetime.strptime(date_str, "%Y-%m-%d")
        todays_date = date_object.date()

        year_ago = todays_date - timedelta(days=365)

        year_ago_str = year_ago.strftime("%Y-%m-%d")
        return year_ago_str

## USAGE
# class_instance = DateUtilities()
# print(class_instance.year_ago_date_str('06-12-2023'))