import boto3
 
#for s3 client 

s3=boto3.client("s3")

#for  creating bucket

s3.create_bucket(
    Bucket="My_Bucket",
    CreateBucketConfiguration={
        "LocationConstraint":"eu-north-1"
    }
)

#for listing bucket

bucket_list = s3.list_buckets()
for bucket in bucket_list:
    print(f"Bucket : {bucket["Name"]}")


#for uploading objects in bucket

s3.upload_file(
    "file.txt",
    "My_Bucket",
    "First_Object"
)

#for downloading object file from s3

s3.download_file(
    "First_Object",
    "My_Bucket",
    "Desktop"
)

#for deleting file

s3.delete_object(
    Bucket="My_Bucket",
    Key="First_Object"
)

#for listing object
list_Objects=s3.list_objects_v2(Bucket="My_Bucket")
if "Contents" in list_Objects:
    for Object in list_Objects["Contents"]:
        print("Object Key :",Object["Key"],"|Object Size:",Object["Size"])

