import os
import psycopg2
from config import DB_CONFIG, DATA_PATH, CSV_TABLE_MAPPING


def get_connection():
    return psycopg2.connect(**DB_CONFIG)


def load_csv_to_table(table_name, csv_file):
    full_path = os.path.join(DATA_PATH, csv_file)

    print(f"\nLoading table: bronze.{table_name}")
    print(f"Source file : {full_path}")

    if not os.path.exists(full_path):
        print("File NOT found. Skipping.")
        return

    try:
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(f"TRUNCATE TABLE bronze.{table_name};")

        with open(full_path, "r", encoding="utf-8") as file:
            cursor.copy_expert(
                f"""
                COPY bronze.{table_name}
                FROM STDIN
                WITH CSV HEADER DELIMITER ','
                """,
                file
            )

        conn.commit()

        cursor.execute(f"SELECT COUNT(*) FROM bronze.{table_name};")
        row_count = cursor.fetchone()[0]

        print(f"Loaded successfully: {row_count} rows")

        cursor.close()
        conn.close()

    except Exception as error:
        print(f"Failed loading bronze.{table_name}")
        print(error)


if __name__ == "__main__":
    for table_name, csv_file in CSV_TABLE_MAPPING.items():
        load_csv_to_table(table_name, csv_file)