from bs4 import BeautifulSoup
from win10toast import ToastNotifier
import requests

# Function to fetch data from URL
def get_weather_data(url):
    try:
        r = requests.get(url)
        r.raise_for_status()  # Raise an HTTPError for bad responses
        return r.text
    except requests.exceptions.RequestException as e:
        print(f"Error fetching URL: {e}")
        return None

# Function to parse HTML and extract weather information
def parse_weather(html):
    if html:
        soup = BeautifulSoup(html, 'html.parser')
        current_temp = soup.find("span", class_="_-_-components-src-organism-CurrentConditions-CurrentConditions--tempValue--MHmYY")
        chances_rain = soup.find("div", class_="_-_-components-src-organism-CurrentConditions-CurrentConditions--precipValue--2aJSf")

        if current_temp and chances_rain:
            temp = current_temp.get_text(strip=True)
            rain = chances_rain.get_text(strip=True)
            return temp, rain
        else:
            print("Unable to find weather information on the page.")
            return None, None
    else:
        print("No HTML content to parse.")
        return None, None

# Main function to display toast notification
def display_notification(temp, rain):
    if temp and rain:
        result = f"Current temperature: {temp} in Patna, Bihar\nChance of rain: {rain}"
        n = ToastNotifier()
        n.show_toast("Live Weather Update", result, duration=10)
    else:
        print("Unable to display notification. Missing weather information.")

# Example usage
if __name__ == "__main__":
    url = "https://weather.com/en-IN/weather/today/l/25.59,85.14?par=google&temp=c/"
    html_data = get_weather_data(url)
    if html_data:
        temp, rain = parse_weather(html_data)
        display_notification(temp, rain)
