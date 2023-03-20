## Zetelverdeling rekentool

This python-script uses the **[D'Hondt method](https://en.wikipedia.org/wiki/D%27Hondt_method)**. This algorithm is used in the Netherlands and other countries to divide seats in parliaments.

## Setup

```bash
python3 -m pip install -r requirements.txt
```

## Usage

To run the script, you will need to provide a datafile and the number of seats to divide. The datafile should follow the [data format](#data-format) described below.

```
usage: calculate.py [-h] [--file FILE] [--seats SEATS]

This python-script uses the D'Hondt method. This algorithm is used in the Netherlands and other countries to divide seats in parliaments.

options:
  -h, --help     show this help message and exit
  --file FILE    The name of the data file (e.g., example.csv)
  --seats SEATS  The number of seats to divide (e.g., 47)
```
If no arguments are given, the script will use the [example data file](example.csv) and 47 seats.

## Data format
Data should be provided as a comma separated file (CSV) with the following columns. Headers should be present on the first row.
- `Partij` - the name of the party.
- `Stemmen` - the number of votes for the party.

For example:
```csv
"Partij","Stemmen"
"Partij voor de Open Source",12357
"ASM",9487
"Progressieven",3945
"CPP",3894
"PythonPartij",1394
"C.P. Computerpartij",384
"DotNet",380
```