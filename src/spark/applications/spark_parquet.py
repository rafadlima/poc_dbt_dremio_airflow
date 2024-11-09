import pyspark
from pyspark.sql import SparkSession


def transform_parquet(device_file, zone_landing) -> None:
    
    # Connect to a remote Spark cluster (e.g., AWS EMR, Databricks)
    spark = SparkSession.builder \
                .appName("DataIngestion") \
                .getOrCreate()
    
    
    # Read data from an external source (e.g., S3 bucket)
    get_device_file = device_file #"s3a://raw/*.json"

    raw_data = spark.read \
                .format("json") \
                .option("inferSchema", "true") \
                .option("header", "true") \
                .json(get_device_file)
    
    # Write the data to the "bronze" layer of the data lake in Parquet format
    parquet_bronze_zone = zone_landing #"s3a://bronze"

    raw_data.write.format("parquet").save(parquet_bronze_zone)

    # Stop the Spark session
    spark.stop()