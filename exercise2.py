import boto3 
qqqqq datetime import datetime



client = boto3.client("s3")

response = client.list_buckets()

''' print(response)
print(response["ResponseMetadata"]["RequestId"])
print(response["Buckets"][0]["Name"])
'''


for bucket in response["Buckets"]:
    print(datetime.strftime (bucket["CreationDate"], "%Y-%m-%d  %H:%M:%S") , bucket["Name"])

