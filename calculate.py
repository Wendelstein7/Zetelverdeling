#!/usr/bin/env/python3

import sys
import pandas as pd
import argparse

PARTY = "Partij"
WHOLESEATS = "Hele zetels"
SEATS = "Zetels"
VOTES = "Stemmen"
PERCENTAGE = "Percentage"
SUM = "Totaal"
QUOTIENT = "Quotient"

# Create a parser object to handle command line arguments
parser = argparse.ArgumentParser(
    description="This python-script uses the D'Hondt method. This algorithm is used in the Netherlands and other countries to divide seats in parliaments.")
# Add arguments to the parser
parser.add_argument("--file", type=str, help="The name of the data file (e.g., example.csv)",
                    default="example.csv", required=False)
parser.add_argument("--seats", type=int,
                    help="The number of seats to divide (e.g., 47)", default=47, required=False)
# Parse the command line arguments
args = parser.parse_args()
# Get the values from the arguments
file_name = args.data
number_of_seats = args.seats


# Read the CSV file into a pandas DataFrame
df = pd.read_csv(file_name, index_col=0,
                 dtype={PARTY: str, VOTES: int})
df = df.sort_values(by=[VOTES], ascending=False)

# Add a column "Percentage" with the percentage of the total votes
df[PERCENTAGE] = df[VOTES] / df[VOTES].sum() * 100

# Calculate the number of whole seats for each party
df[WHOLESEATS] = df[VOTES] // (df[VOTES].sum() / number_of_seats)

# Use the D'Hondt method to calculate the total number of seats for each party
df[SEATS] = df[WHOLESEATS]
while df[SEATS].sum() < number_of_seats:
    df[QUOTIENT] = df[VOTES] / (df[SEATS] + 1)
    df.at[df[QUOTIENT].idxmax(), SEATS] += 1
df.drop(columns=[QUOTIENT], inplace=True)

# Add a row "Total" with the sum of all columns
df.loc[SUM] = df.sum()

# Print the DataFrame
print(df)
