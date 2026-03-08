import snowflake.connector

# connection parameters
config = {
    "user": "STILGARDM",  # Replace with your Snowflake login name
    "password": "4e9SikfxVu44wyg",  # Replace with your password
    "account": "oywpqqi-qm00385",  # Your specific account identifier
    "warehouse": "COMPUTE_WH",  # Default trial warehouse
    "database": "LEARNING_DB",
    "schema": "PYTHON_TEST"
}

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