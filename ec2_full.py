import boto3
class Full_EC2:
   
   def __init__(self, region_name ="eu-north-1"):
       self.ec2_c =  boto3.client("ec2", region_name=[region])
       self.ec2_r = boto3.resource("ec2",region_name=[region])
   def create_instances(self):
       
       print("Instance is Creating ......")
       instances = self.ec2_r.create_instances(
          ImageId="ami-12345",
          InstanceType="t2.micro",
          MinCount=1,
          MaxCount=1,
          KeyName="None"
          SecurityGroupIds=[None]
       )
       ins=instances[0]
       ins.wait_until_exists()
       print("Instance is Created and  the ID of instance is :",ins.id)

   def list_instances(self):
       print("All the Instances list is given below")

       response=self.ec2_c.describe_instances()

       for r in response["Reservations"]:
           for i in r["Instances"]:
             print(
                 "Instances ID :",i["InstanceID"],
                 "Instace Type :",i["InstanceType"],
                 "Instance State :",i["State"]["Name"]
             ) 

   def start_instance(self,instance_id):
       print("Instance is Starting........")
       self.ec2_c.start_instances(
           InstanceIds=[instance_id]
       )
       waiter=self.ec2_c.get_waiter("instance_running")
       waiter.wait(InstanceIds=[instance_id])
       print("Instance is Started and Running now !")

   def stop_instance(self,instance_id):
        print("Instance is Stopping........")
        self.ec2_c.stop_instances(
           InstanceIds=[instance_id]
       )
        waiter=self.ec2_c.get_waiter("instance_stopped")
        waiter.wait(InstanceIds=[instance_id])
        print("Instance is  Stoped now !")

   def terminate_instance(self,instance_id):
        print("Instance is Terminating.......")
        self.ec2_c.terminate_instances(
           InstanceIds=[instance_id]
       )
        waiter=self.ec2_c.get_waiter("instance_terminated")
        waiter.wait(InstanceIds=[instance_id])
        print("Instance is  Terminated now !")
   def list_details(self,instance_id="ID"):
       print("All the Instances list is given below")

       response=self.ec2_c.describe_instances()

       for r in response["Reservations"]:
           for i in r["Instances"]:
             print(
                 "Instances ID :",i["InstanceID"],
                 "Instace Type :",i["InstanceType"],
                 "Instance State :",i["State"]["Name"]
                 "Public Ip Address:",i.get("PublicIpAddress")
                 "Private Ip Address:",i.get("PrivateIpAddress")
             )
   def filtering_state(self,state="running"):
        self.ec2_r.instances.filter(
            Filters=[
             {"Name":"Instance-state-name","Values":[state]}
            ]
        )
        for ins in instances:
            print("ID:",ins.id,"|State:",ins.state["Name"])

   def filtering_tags(self,key="key",value="value"):
        self.ec2_r.instances.filter(
            Filters=[
             {"Name":"tags":[key],"Values":[value]}
            ]
        )
        for ins in instances:
            print("ID:",ins.id,"|State:",ins.state["Name"])

if __name__ == "__main__":

    manager = Full_EC2()

    instance_id=manager.create_instances()

    manager.list_instances

    manager.list_details(instance_id)

    manager.start_instance(instance_id)

    manager.stop_instance(instance_id)

    manager.terminate_instance(instance_id)

    manager.filtering_state("running")

    manager.filtering_tags("kay","value")