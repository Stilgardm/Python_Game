from google.cloud import bigquery
from google.oauth2 import service_account

# Path to your downloaded JSON file
KEY_PATH = "D:/PythonProject/firm-structure-378501-5b90beb1e7fd.json"

def get_table_data():
    # Initialize the BigQuery client
    # If running locally, ensure you have set your GOOGLE_APPLICATION_CREDENTIALS
    credentials = service_account.Credentials.from_service_account_file(KEY_PATH)
    client = bigquery.Client(credentials=credentials, project=credentials.project_id)
    #client = bigquery.Client()

    # Define your table reference
    table_id = "firm-structure-378501.Finance.Finance_Test"
    #`firm - structure - 378501.Finance.Finance_Test`
    #nth-mantra-411407.Test.TestTable

    # SQL query to grab all data
    query = f"SELECT * FROM `{table_id}`"

    try:
        # Run the query
        query_job = client.query(query)
        results = query_job.result()  # Waits for the job to complete

        print(f"Displaying data from {table_id}:\n" + "-"*30)

        # Iterate through the rows (there should be only one)
        for row in results:
            # Dynamically grab column names and values
            columns = row.keys()
            for col in columns:
                print(f"{col}: {row[col]}")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    get_table_data()