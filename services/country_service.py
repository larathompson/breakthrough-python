import requests

# Can you practise using the https://restcountries.com/#api-endpoints-using-this-project to get the data on countries?
class CountryService:
    
    # @staticmethod
    # def get_all_countries():
    #     response = requests.get('https://restcountries.com/v3.1/all')
    #     return response.json()
    
    @staticmethod
    def get_country_by_name(name):
        response = requests.get(f'https://restcountries.com/v3.1/name/{name}?fullText=true')
        return response.json()
    
    @staticmethod
    def get_countries_for_region(region):
        response = requests.get(f'https://restcountries.com/v3.1/region/{region}')
        return response.json()

    #  can you write a function that gets the capital city of a country? 
    #  use the examples above and take a look at https://restcountries.com/#endpoints-capital-city to help 