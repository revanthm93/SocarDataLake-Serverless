# SocarDataLake-Serverless
Corporate Datalake for Socar - Build completely on AWS Cloud with Serverless Architecture using S3, Glue (catalog and crawler), Lambda, SNS, (Kinesis- optional)

I have build a serverless data lake with Amazon Simple Storage Service (Amazon S3) as the primary data store as it provides us with high scalability and high availability.

Components of AWS whic I used in the current Dalalake setup are:

* Amazon s3 for storage.
* Lambda
* SQS
* Glue
* Cloudwatch
* SNS
* Athena 
* QuickSight (Account not available)
* Kinesis Data Stream and Firehose (optional - for realtime streaming data processing)

How it works:

1. Data gets ingested to raw s3 bucket (socardl-raws3bucket-12zp2irhigzvx).

(Using any one of the scripts - uploadtos3.py uploadcsvtos3asstream.py, generatedatastreamforKinesis.py)

https://s3.console.aws.amazon.com/s3/buckets/socardl-raws3bucket-12zp2irhigzvx?region=ap-south-1
https://s3.console.aws.amazon.com/s3/buckets/socardl-processeds3bucket-aoutxjqiuaik?region=ap-south-1

2. Once the data is uploaded, an event which we configured invokes the GlueTriggerLambdafunction. This function creates an AWS Glue Data Catalog that stores metadata information inferred from the data that was crawled from s3 raw bucket.

(The data catalog helps us to keep track what data we have in datalake and determine the schema of the data along with other metadata information such as location, format and size. It helps us to run ETL jobs or ad hoc queries on data thats lying in data lake)

3. Simple Queue Service (Amazon SQS) queue with a topic for maintaining the retry logic to ensure the data gets processed.

4. Have created an AWS Glue ETL job with a basic python code with a spark instance data type change transformation. (We can customize as much as we want, we can also do the same with scala). Processed data will be stored in seperate processed s3 bucket and bookmark etl job, it will ensure you won't reprocess the same data again and again.

(AWS Glue provides a managed Apache Spark environment to run your ETL job without maintaining any infrastructure with pay as you go model.)

5. Created seperate lambda function to automate the ETL job to transform and process the data. When the lambda function's CloudWatch Events rule receives a success status, it triggers the ETLJobLambda Lambda function.

6. Configured the cloudWatch Events rule - OpsEventRule to send an email notification to us using an Amazon SNS topic to inform us that our data has been successfully processedby our ETL gluejob.

7. On top of the Processed data in processed bucket, Athena tables can be created for querying and using quicksight we can vizualise the data.

Account provided wasn't provisioned with quicksight. So couldn't touch up on visualization part. And its just simple since we already have the processed data in place.


Additional items done:

Handled realtime streaming data using kinesis data stream and firehose.

The streaming source can be trigger using either of the scripts given or you can use kinesis data generator with credentials:

link - https://awslabs.github.io/amazon-kinesis-data-generator/web/producer.html?upid=ap-south-1_0Z2Xlf9O8&ipid=ap-south-1:d04ecc1d-7161-46cb-8433-0c3ec0316d0b&cid=3fmlk9p4gr8992v4qbn2h2jj1k&r=ap-south-1

username - Candidate-10001-ap-south-1
password - Socar123
