from utilities.date_utilities import DateManager
import schedule


class GetData:
    def get_stocks_data(self):
        pass

    def get_ads_data(self):
        pass


class CountActivation:
    def __init__(self) -> None:
        self.date_manager_instance = DateManager()
        self.get_data_instance = GetData()

    def countdown(self):
        schedule.every(24).hours.do(self.activate_data_acquisition)

        while True:
            schedule.run_pending()

    def get_data(self):
        self.get_data_instance.get_stocks_data()
        self.get_data_instance.get_ads_data()
        return 'Data acquired'

    def activate_data_acquisition(self) -> bool:
        todays_date = self.date_manager_instance.todays_date_str()

        if self.date_manager_instance.is_workday(todays_date):
            self.get_data()


## USAGE
# count_activation_class_instance = CountActivation()
# print(count_activation_class_instance.activate_data_acquisition())


