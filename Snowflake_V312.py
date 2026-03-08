import json
import snowflake.connector

# connection parameters
KEY_PATH = "D:/PythonProject/snowflake_creds.json"

with open(KEY_PATH, 'r') as f:
    config = json.load(f)

def get_snowflake_data():
    # Load credentials from the JSON file

    # Connect using the dictionary loaded from JSON
    ctx = snowflake.connector.connect(
        user=config['user'],
        password=config['password'],
        account=config['account'],
        warehouse=config['warehouse'],
        database=config['database'],
        schema=config['schema'],
        role=config['role']
    )

    return ctx

try:
    print("Connecting to Snowflake...")
    ctx = snowflake.connector.connect(**config)
    cs = ctx.cursor()

    # Querying the table you mentioned
    sql = "SELECT * FROM DATALOADTEST"
    cs.execute(sql)

    # Fetching results
    results = cs.fetchall()

    if not results:
        print("Connection successful, but the table is empty.")
    else:
        print(f"Successfully recovered {len(results)} rows:")
        for row in results:
            print(row)

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    # Safely closing the connection
    if 'cs' in locals(): cs.close()
    if 'ctx' in locals(): ctx.close()
    print("Connection closed.")