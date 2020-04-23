import csv
import json
import boto3
from random import randint
def chunkit(l, n):
 for i in range(0, len(l), n):
    yield l[i:i + n]

kinesis = boto3.client("kinesis")
with open("C:\\Users\\revam\\Downloads\\tripdata_2019-01.csv") as f:
#Creating the ordered Dict
 reader = csv.DictReader(f)
#putting the json as per the number of chunk we will give in below function
#Create the list of json and push like a chunk. I am sending 100 rows together
 records = chunkit([{"PartitionKey": 'sau', "Data": json.dumps(row)} for row in reader], 100)
for chunk in records:
    kinesis.put_records(StreamName="kdg_datastream", Records=chunk)