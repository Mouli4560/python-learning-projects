from datetime import date
import sys
import inflect
p = inflect.engine()

def minutes(birthday, today):
    difference = today - birthday
    return difference.days * 24 * 60

def main():
    try:
        birthdate = input("Date of Birth: ")
        birthday = date.fromisoformat(birthdate)
        today = date.today()
        minutes_count = minutes(birthday, today)
        if minutes_count < 0:
            raise ValueError
        output = p.number_to_words(minutes_count, andword = "")
        print(f"{output.capitalize()} minutes")

    except ValueError:
        sys.exit(1)

if __name__ == "__main__":
    main()
