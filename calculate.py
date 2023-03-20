#!/usr/bin/env python3
"""
This python-script uses the D'Hondt method.
This algorithm is used in the Netherlands and other countries
to divide seats in parliaments.
"""

import argparse
import pandas as pd

PARTY = "Partij"
WHOLESEATS = "Hele zetels"
SEATS = "Zetels"
VOTES = "Stemmen"
PERCENTAGE = "Percentage"
SUM = "Totaal"
QUOTIENT = "Quotient"


def main(file_name: str, number_of_seats: int) -> None:
    """
    Print the number of seats per party for the given number of
    seats, using vote counts from the specified file.
    """
    # Read the CSV file into a pandas DataFrame
    data = pd.read_csv(file_name,
                       index_col=0,
                       dtype={PARTY: str, VOTES: int})
    data = data.sort_values(by=[VOTES], ascending=False)

    # Add a column "Percentage" with the percentage of the total votes
    data[PERCENTAGE] = data[VOTES] / data[VOTES].sum() * 100

    # Calculate the number of whole seats for each party
    data[WHOLESEATS] = (data[VOTES] //
                        (data[VOTES].sum() / number_of_seats)
                        ).astype(int)

    # Use the D'Hondt method to calculate the total
    # number of seats for each party
    data[SEATS] = data[WHOLESEATS]
    while data[SEATS].sum() < number_of_seats:
        data[QUOTIENT] = data[VOTES] / (data[SEATS] + 1)
        data.at[data[QUOTIENT].idxmax(), SEATS] += 1
    data.drop(columns=[QUOTIENT], inplace=True)

    # Get dtypes
    dtypes = data.dtypes
    # Add a row "Total" with the sum of all columns
    data.loc[SUM] = data.sum()
    # Set dtypes correctly again
    data = data.astype(dtypes)

    # Print the DataFrame
    print(data)


if __name__ == '__main__':
    # Create a parser object to handle command line arguments
    parser = argparse.ArgumentParser(
        description=__doc__)
    # Add arguments to the parser
    parser.add_argument("--file",
                        type=str,
                        help="The name of the data file (e.g., example.csv)",
                        default="example.csv",
                        required=False)
    parser.add_argument("--seats",
                        type=int,
                        help="The number of seats to divide (e.g., 47)",
                        default=47,
                        required=False)
    # Parse the command line arguments
    args = parser.parse_args()
    main(args.file, args.seats)
