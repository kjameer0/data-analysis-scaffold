# Data analysis scaffold

This project provides a basic and evolvable scaffold for analysis of `.csv` files.

## Get started

[Sample data about trees in NYC](https://data.cityofnewyork.us/Environment/2015-Street-Tree-Census-Tree-Data/uvpi-gqnh/about_data). You can click export on this webpage to get sample CSV data.

1. Create a folder called `data-files` by running `mkdir data-files` in the Terminal
2. Copy and paste the `.csv` file you want to work with into the `data-files/` folder
3. Open new VSCode Terminal
4. run `./setup.sh` in your terminal by copying and pasting `./setup.sh` into the terminal and pressing Enter.
5. run `./run.sh` to run the main program(make sure to open `main.py` and make sure the `csv_file` variable contains the correct path to your csv data file)

## Roles for different folders and files

1. `test` contains a files and configurations for testing
2. `.vscode` contains settings to customize VSCode, like auto-saving
3. add packages to `requirements.txt` if needed, and run `./setup.sh` again

## Testing

1. Add new test data to test suites in `test/conftest.py`
2. Group tests by behavior/logic you want to test together

## Snowflake

If you exported data with "Download results from stage" you can take the file path that Snowflake gives you and run:
`gunzip -c <snowflake-data-path> > <target-path>` to put the data where you need it.
