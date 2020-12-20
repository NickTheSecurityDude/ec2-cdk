from aws_cdk import (
  aws_ec2 as ec2,
  core
)

class EC2Stack(core.Stack):
  def __init__(self, scope: core.Construct, construct_id: str, **kwargs) -> None:
    super().__init__(scope, construct_id, **kwargs)
   
    ec2.Instance(self, "ec2-instance",
      instance_type=ec2.InstanceType("t3.nano"),
      machine_image=ec2.LookupMachineImage(name="my-test-ami"),
      vpc=ec2.Vpc.from_lookup(self,"VPC",is_default=True)
    )