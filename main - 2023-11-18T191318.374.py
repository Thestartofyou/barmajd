import requests
from bs4 import BeautifulSoup
import datetime

def get_cheapest_drinks():
    url = "YOUR_BAR_WEBSITE_URL"
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        # Parse the HTML to find information about drink prices and locations
        # Update this part based on the structure of the website

        cheapest_drinks = {
            "drink_name": "example_drink",
            "price": "$5.00",
            "location": "Bar XYZ",
            "time": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }

        return cheapest_drinks
    else:
        print(f"Failed to retrieve data. Status code: {response.status_code}")
        return None

if __name__ == "__main__":
    cheapest_drink = get_cheapest_drinks()

    if cheapest_drink:
        print(f"At {cheapest_drink['time']}, {cheapest_drink['drink_name']} is cheapest at {cheapest_drink['location']} for {cheapest_drink['price']}.")
