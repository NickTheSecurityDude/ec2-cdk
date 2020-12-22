from aws_cdk import (
  aws_ec2 as ec2,
  core
)

class EC2Stack(core.Stack):
  def __init__(self, scope: core.Construct, construct_id: str, **kwargs) -> None:
    super().__init__(scope, construct_id, **kwargs)
   
    my_ec2=ec2.Instance(self, "ec2-instance",
      instance_type=ec2.InstanceType("t3.nano"),
      machine_image=ec2.LookupMachineImage(name="my-test-ami"),
      vpc=ec2.Vpc.from_lookup(self,"VPC",is_default=True)
    )

    # allow SSH
    my_ec2.connections.allow_from_any_ipv4(ec2.Port.tcp(22),"Internet access SSH")

    # add userdata
    my_ec2.user_data.add_commands("wget https://inspector-agent.amazonaws.com/linux/latest/install","bash install")

    # add inspector tag
    core.Tags.of(my_ec2).add("inspector","True")