import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_style("whitegrid")
plt.rcParams["figure.dpi"] = 110

CLEAN_PATH = "data/retail_sales_clean.csv"
OUT_DIR = "outputs"


def load_clean(path: str) -> pd.DataFrame:
    df = pd.read_csv(path)
    df["date"] = pd.to_datetime(df["date"])
    return df

def descriptive_stats(df: pd.DataFrame):
    numeric_cols = ["age", "quantity", "price_per_unit", "total_amount"]
    stats = df[numeric_cols].describe().round(2)

    with open(f"{OUT_DIR}/descriptive_stats.txt", "w") as f:
        f.write("DESCRIPTIVE STATISTICS — Numeric Columns\n")
        f.write("=" * 50 + "\n")
        f.write(stats.to_string())
        f.write("\n\n")
        f.write("Transactions by category:\n")
        f.write(df["product_category"].value_counts().to_string())
        f.write("\n\nTransactions by gender:\n")
        f.write(df["gender"].value_counts().to_string())
        f.write("\n\nRevenue by category:\n")
        f.write(df.groupby("product_category")["total_amount"].sum().sort_values(ascending=False).to_string())

    print(stats)
    return stats

def univariate_analysis(df: pd.DataFrame):
    fig, axes = plt.subplots(2, 2, figsize=(12, 9))

    sns.histplot(df["age"], bins=20, kde=True, ax=axes[0, 0], color="#2c7a7b")
    axes[0, 0].set_title("Distribution of Customer Age")

    sns.boxplot(x=df["total_amount"], ax=axes[0, 1], color="#2c7a7b")
    axes[0, 1].set_title("Box Plot — Total Amount (₹)")

    sns.histplot(df["total_amount"], bins=30, kde=True, ax=axes[1, 0], color="#c05621")
    axes[1, 0].set_title("Distribution of Total Amount")

    sns.boxplot(x=df["quantity"], ax=axes[1, 1], color="#c05621")
    axes[1, 1].set_title("Box Plot — Quantity per Transaction")

    plt.tight_layout()
    plt.savefig(f"{OUT_DIR}/01_univariate_analysis.png")
    plt.close()
    print("Saved: 01_univariate_analysis.png")


def bivariate_analysis(df: pd.DataFrame):
    fig, axes = plt.subplots(1, 2, figsize=(13, 5.5))

    sns.scatterplot(
        data=df, x="age", y="total_amount", hue="product_category",
        alpha=0.6, ax=axes[0]
    )
    axes[0].set_title("Age vs Total Amount Spent (by Category)")

    numeric_cols = ["age", "quantity", "price_per_unit", "total_amount"]
    corr = df[numeric_cols].corr()
    sns.heatmap(corr, annot=True, fmt=".2f", cmap="RdYlGn", center=0, ax=axes[1])
    axes[1].set_title("Correlation Heatmap")

    plt.tight_layout()
    plt.savefig(f"{OUT_DIR}/02_bivariate_analysis.png")
    plt.close()
    print("Saved: 02_bivariate_analysis.png")
    return corr

def category_gender_analysis(df: pd.DataFrame):
    fig, axes = plt.subplots(1, 2, figsize=(13, 5.5))

    cat_revenue = df.groupby("product_category")["total_amount"].sum().sort_values(ascending=False)
    sns.barplot(x=cat_revenue.values, y=cat_revenue.index, hue=cat_revenue.index,
                ax=axes[0], palette="viridis", legend=False)
    axes[0].set_title("Total Revenue by Category")
    axes[0].set_xlabel("Revenue (₹)")

    gender_cat = df.groupby(["product_category", "gender"])["total_amount"].sum().unstack()
    gender_cat.plot(kind="bar", ax=axes[1], color=["#e07a5f", "#3d5a80"])
    axes[1].set_title("Revenue by Category & Gender")
    axes[1].set_ylabel("Revenue (₹)")
    axes[1].tick_params(axis="x", rotation=0)

    plt.tight_layout()
    plt.savefig(f"{OUT_DIR}/03_category_gender_analysis.png")
    plt.close()
    print("Saved: 03_category_gender_analysis.png")


def time_trend_analysis(df: pd.DataFrame):
    monthly = df.set_index("date").resample("ME")["total_amount"].sum()

    plt.figure(figsize=(10, 5.5))
    monthly.plot(marker="o", color="#2c7a7b")
    plt.title("Monthly Revenue Trend (2023)")
    plt.ylabel("Revenue (₹)")
    plt.xlabel("Month")
    plt.tight_layout()
    plt.savefig(f"{OUT_DIR}/04_monthly_revenue_trend.png")
    plt.close()
    print("Saved: 04_monthly_revenue_trend.png")


def age_group_analysis(df: pd.DataFrame):
    plt.figure(figsize=(9, 5.5))
    age_spend = df.groupby("age_group")["total_amount"].mean().sort_index()
    sns.barplot(x=age_spend.index.astype(str), y=age_spend.values,
                hue=age_spend.index.astype(str), palette="crest", legend=False)
    plt.title("Average Spend by Age Group")
    plt.ylabel("Average Total Amount (₹)")
    plt.xlabel("Age Group")
    plt.tight_layout()
    plt.savefig(f"{OUT_DIR}/05_age_group_spend.png")
    plt.close()
    print("Saved: 05_age_group_spend.png")


def main():
    df = load_clean(CLEAN_PATH)
    descriptive_stats(df)
    univariate_analysis(df)
    bivariate_analysis(df)
    category_gender_analysis(df)
    time_trend_analysis(df)
    age_group_analysis(df)
    print("\nEDA complete. Check the outputs/ folder for charts + stats.")


if __name__ == "__main__":
    main()
