# Country Lookup CLI

A command-line tool for looking up country information: capital, population,
region, languages, and currencies. Supports checking multiple countries in a
single session.

## API used

[countries.dev](https://countries.dev) — a free, keyless REST API. This tool uses the endpoint:

```
GET https://countries.dev/countries
```

Fields used from the response: `name`, `capital`, `population`, `region`,
`languages`, `currencies`, and `cioc` (for lookups by IOC code).

## Setup

```bash
git clone <repository-url>
cd <project-folder>
pip install -r requirements.txt
```

## Usage

```bash
python main.py
```

The program fetches the full list of countries once, then lets you search in
a loop — by name (`Russia`, `Germany`) or IOC code (`RUS`, `GER`). Search is
case-insensitive. Type `q` to quit.

Example session:

```
Loaded 250 countries. You can look up as many as you like.

Enter a country name or code (or 'q' to quit): rus
Country: Russian Federation
Capital: Moscow
Population: 144000000
Region: Europe
Languages:
 - Russian
Currencies:
 - Russian ruble ₽ (RUB)
________________________________________

Enter a country name or code (or 'q' to quit): q
Goodbye!
```

## Error handling

- Network failures when calling the API are caught and reported without
  crashing the program.
- Empty input prompts the user to try again.
- A country not found produces a clear message and the loop continues.
- Missing fields in the API response (e.g. countries without an official
  capital) are handled with `.get()` and default values, avoiding `KeyError`.

## Project structure

```
.
├── main.py            # fetch / find / display / CLI loop logic
├── requirements.txt   # dependencies
└── README.md
```
