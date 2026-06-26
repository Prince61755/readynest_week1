import pandas as pd

RAW_PATH = "data/retail_sales.csv"
CLEAN_PATH = "data/retail_sales_clean.csv"


def load_data(path: str) -> pd.DataFrame:
    df = pd.read_csv(path)
    print(f"Loaded raw data: {df.shape[0]} rows, {df.shape[1]} columns")
    return df


def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    
    df.columns = (
        df.columns.str.strip()
        .str.lower()
        .str.replace(" ", "_")
    )

    df["date"] = pd.to_datetime(df["date"], format="%Y-%m-%d")

    dupes = df.duplicated().sum()
    id_dupes = df["transaction_id"].duplicated().sum()
    print(f"Exact duplicate rows: {dupes} | Duplicate transaction IDs: {id_dupes}")
    df = df.drop_duplicates()

    expected_total = df["quantity"] * df["price_per_unit"]
    mismatches = (expected_total != df["total_amount"]).sum()
    print(f"Rows where total_amount != quantity x price_per_unit: {mismatches}")


    print("Nulls per column:\n", df.isnull().sum().to_string())
    assert (df["age"] > 0).all(), "Found non-positive age"
    assert (df["quantity"] > 0).all(), "Found non-positive quantity"
    assert (df["price_per_unit"] > 0).all(), "Found non-positive price"


    df["month"] = df["date"].dt.month_name()
    df["month_num"] = df["date"].dt.month
    df["weekday"] = df["date"].dt.day_name()
    df["quarter"] = df["date"].dt.quarter

    df["age_group"] = pd.cut(
        df["age"],
        bins=[17, 25, 35, 45, 55, 65],
        labels=["18-25", "26-35", "36-45", "46-55", "56-64"],
    )

    df["spend_tier"] = pd.cut(
        df["total_amount"],
        bins=[0, 100, 500, 1000, 5000],
        labels=["Low (<=100)", "Medium (100-500)", "High (500-1000)", "Premium (>1000)"],
    )

    df = df.reset_index(drop=True)

    return df


def validate(df: pd.DataFrame):
    print("\n--- VALIDATION ---")
    print("Final shape:", df.shape)
    print("Date range:", df["date"].min().date(), "to", df["date"].max().date())
    print("Categories:", df["product_category"].unique().tolist())
    print("Remaining nulls:\n", df.isnull().sum()[df.isnull().sum() > 0])


def main():
    df = load_data(RAW_PATH)
    df_clean = clean_data(df)
    validate(df_clean)
    df_clean.to_csv(CLEAN_PATH, index=False)
    print(f"\nClean data saved to {CLEAN_PATH}")


if __name__ == "__main__":
    main()
