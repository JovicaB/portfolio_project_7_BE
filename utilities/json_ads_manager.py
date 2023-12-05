from json_manager import JSONDataManager


ADS_DATA = 'data/ads.json'


class JSONAdsDataExtractor:
    def __init__(self) -> None:
        self.ads_data = JSONDataManager(ADS_DATA)
        self.main_json_key = 'job_ads_websites'

    def get_ads_website(self, country):
        ads_data = self.ads_data.read_json(self.main_json_key)
        if country not in ads_data:
            return f"Country '{country}' not found in the ads data."
        else:
            return ads_data[country]


# class_instance = JSONAdsDataExtractor()
# print(class_instance.get_ads_website("Serbia"))