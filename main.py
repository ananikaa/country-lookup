import requests

API_URL = "https://countries.dev/countries"

def fetch_data():
    try:
        response = requests.get(API_URL)
        response.raise_for_status()
    except requests.RequestException:
        print("Could not connect to the API.")
        return None

    data = response.json()

    if not data:
        print("The API returned an empty list of countries.")
        return None

    return data

def find_country(data, country_name):
    country_name = country_name.lower()

    for country in data:
        name = country.get("name", "")
        cioc = country.get("cioc", "")

        if country_name in (name.lower(), cioc.lower()):
            return country

    return None

def display_country(country):
    print("Country:", country.get("name", "Unknown"))
    print("Capital:", country.get("capital") or "N/A")
    print("Population:", country.get("population") or "N/A")
    print("Region:", country.get("region", "N/A"))

    languages = country.get("languages")
    print("Languages:")
    if languages:
        for language in languages:
            print(" -", language.get("name", "Unknown"))
    else:
        print(" - N/A")

    currencies = country.get("currencies")
    print("Currencies:")
    if currencies:
        for currency in currencies:
            name = currency.get("name", "Unknown")
            symbol = currency.get("symbol", "")
            code = currency.get("code", "")
            print(f" - {name} {symbol} ({code})")
    else:
        print(" - N/A")
    print("_" * 40)

def prompt_country_name():
    user_input = input("\nEnter a country name or code (or 'q' to quit): ").strip()

    if user_input.lower() == "q":
        return None

    if not user_input:
        print("Please enter a country name.")
        return ""

    return user_input

def run_lookup_loop(data):
    while True:
        search_term = prompt_country_name()

        if search_term is None:
            print("Goodbye!")
            break

        if search_term == "":
            continue

        country = find_country(data, search_term)

        if country:
            display_country(country)
        else:
            print(f"Country '{search_term}' not found. Check the spelling and try again.")

def main():
    data = fetch_data()

    if data is None:
        return

    print(f"Loaded {len(data)} countries. You can look up as many as you like.")
    run_lookup_loop(data)

if __name__ == "__main__":
    main()
