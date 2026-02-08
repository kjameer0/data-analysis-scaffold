# Data analysis scaffold

This project provides a basic and evolvable scaffold for analysis of `.csv` files.

## Get started

[Sample data about trees in NYC](https://data.cityofnewyork.us/Environment/2015-Street-Tree-Census-Tree-Data/uvpi-gqnh/about_data)

1. Copy and paste `.csv` file into `data-files/` folder
2. Open new VSCode Terminal
3. run `./setup.sh`
4. run `./run.sh` to run the main program

## Roles for different folders and files

1. `test` contains a files and configurations for testing
2. `.vscode` contains settings to customize VSCode, like auto-saving
3. add packages to `requirements.txt` if needed, and run `./setup.sh` again

## Testing

1. Add new test data to test suites in `test/conftest.py`
2. Group tests by behavior/logic you want to test together
