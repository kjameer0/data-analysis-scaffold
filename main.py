import pandas as pd

# Put the csv file path you want to work with
# between the double quotes
csv_file = "data-files/trees.csv"


def load_dataframe():
    df = pd.read_csv(csv_file, nrows=1000)
    return df


def count_boroughs(df: pd.DataFrame):
    all_boroughs = df.loc[:, "borough"].unique()
    return len(all_boroughs)


if __name__ == "__main__":
    print("Starting analysis")
    trees_df = load_dataframe()
    print("Total boroughs in NYC: ", count_boroughs(trees_df))
