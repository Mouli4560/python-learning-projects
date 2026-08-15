# CS50P - Seasons

A Python program that calculates how many minutes a person has been alive based on their date of birth.

This project was completed as part of CS50's Introduction to Programming with Python (CS50P).

## What it does

The program:

- Takes a date of birth in `YYYY-MM-DD` format.
- Calculates the number of minutes between the date of birth and the current date.
- Converts the resulting number of minutes into words.
- Handles invalid dates and future dates.

## Technologies

- Python
- `datetime`
- `inflect`
- `pytest`

## How to run

Install the required libraries if they are not already installed:

```bash
pip install inflect pytest
```
Then run:
```
python seasons.py
```
Enter your date of birth when prompted in YYYY-MM-DD format.

## Testing

The project includes tests for valid and invalid inputs.

Run the tests with:
```
pytest test_seasons.py
```

## What I practiced

This project helped me practice:

* Working with datetime.date
* Parsing dates with date.fromisoformat()
* Calculating differences between dates
* Converting numerical values into words
* Writing functions
* Handling invalid input
* Writing tests with pytest
