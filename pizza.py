import csv
import sys
from tabulate import tabulate

if len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")
if len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")
if not sys.argv[1].endswith(".csv"):
    sys.exit("Not a CSV file")


def display_menu():
    menu_data = []
    try:
        with open(sys.argv[1]) as file:
            reader = csv.reader(file)
            for row in reader:
                menu_data += [row]
        print(tabulate(menu_data, headers="firstrow", tablefmt="grid"))
    except FileNotFoundError:
        sys.exit("File does not exist")


if __name__ == "__main__":
    display_menu()
