import boto3 

#for accessing the db service 

db=boto3.client("rds",region_name="eu-north-1")

 # for listing db instances 

list_db = db.describe_db_instances()
for dbb in list_db["DBInstances"]:
    print(dbb["DBInstanceIdentifier"])
    print(dbb["DBInstanceStatus"])
    print(dbb["Engine"])


#for creating snapshot

db.create_db_snapshot(
    DBSnapshotIdentifier="my_first_snapshot"
    DBInstanceIdentifier="my_db"
)


#for lsiting snapshots

list_snapshots=db.describe_db_snapshots(
    DBInstanceIdentefier="my_db"
)

for ss in list_snapshots["DBSnapshots"]:
    print(ss["DBSnapshotIdentifier"])
