import pandas as pd
from sqlalchemy import create_engine

DB_USER = "admin"
DB_PASSWORD = "admin123"
DB_HOST = "localhost"
DB_PORT = "5432"
DB_NAME = "salesdb"

CSV_FILE = "data/sales_data.csv"

def extract_data(file_path):
    print("Extracting data...")
    df = pd.read_csv(file_path)
    return df

def transform_data(df):
    print("Transforming data...")

    df.columns = df.columns.str.lower().str.strip()

    df["order_date"] = pd.to_datetime(df["order_date"])

    df["total_amount"] = df["quantity"] * df["price"]

    df["customer_name"] = df["customer_name"].str.title()
    df["city"] = df["city"].str.title()
    df["category"] = df["category"].str.title()

    df = df.drop_duplicates()
    df = df.dropna()

    return df

def load_data(df):
    print("Loading data into PostgreSQL...")

    engine = create_engine(
        f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
    )

    df.to_sql("sales_orders", engine, if_exists="replace", index=False)

    print("Data loaded successfully!")

def run_etl():
    raw_data = extract_data(CSV_FILE)
    clean_data = transform_data(raw_data)
    load_data(clean_data)

    print("ETL pipeline completed successfully.")

if __name__ == "__main__":
    run_etl()