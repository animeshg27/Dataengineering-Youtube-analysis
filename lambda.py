import awswrangler as wr
import pandas as pd
import urllib.parse
import os

# Environment variables
S3_CLEANSED_LAYER = os.environ['s3_cleansed_layer']
GLUE_CATALOG_DB_NAME = os.environ['glue_catalog_db_name']
GLUE_CATALOG_TABLE_NAME = os.environ['glue_catalog_table_name']
WRITE_DATA_OPERATION = os.environ['write_data_operation']

def handle_s3_event(event):
    """
    Extract bucket name and object key from the event.
    """
    record = event['Records'][0]['s3']
    bucket = record['bucket']['name']
    key = urllib.parse.unquote_plus(record['object']['key'], encoding='utf-8')
    return bucket, key

def read_json_from_s3(bucket, key):
    """
    Read JSON content from the specified S3 bucket and key.
    """
    return wr.s3.read_json(f's3://{bucket}/{key}')

def normalize_json_data(df_raw):
    """
    Normalize JSON data to extract required columns.
    """
    return pd.json_normalize(df_raw['items'])

def write_to_s3_as_parquet(df):
    """
    Write the DataFrame to S3 in Parquet format.
    """
    return wr.s3.to_parquet(
        df=df,
        path=S3_CLEANSED_LAYER,
        dataset=True,
        database=GLUE_CATALOG_DB_NAME,
        table=GLUE_CATALOG_TABLE_NAME,
        mode=WRITE_DATA_OPERATION
    )

def lambda_handler(event, context):
    # Handle the S3 event
    bucket, key = handle_s3_event(event)
    
    try:
        # Read and process the JSON data from S3
        df_raw = read_json_from_s3(bucket, key)
        df_normalized = normalize_json_data(df_raw)
        
        # Write the processed data to S3 in Parquet format
        response = write_to_s3_as_parquet(df_normalized)
        
        return response
    
    except Exception as e:
        error_message = f"Failed to process object {key} from bucket {bucket}. Ensure the object exists and the bucket is in the same region as this function."
        print(error_message)
        raise e
