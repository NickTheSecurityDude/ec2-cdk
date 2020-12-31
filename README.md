# ec2-cdk

## Create an EC2 Instance using AWS CDK

```
git clone https://github.com/NickTheSecurityDude/ec2-cdk.git
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install -r requirements.txt
export AWS_PROFILE="your-profile"
cdk bootstrap aws://acct-id/region
cdk ls
cdk synth
cdk deploy
```

(c) Copyright 2020 - NickTheSecurityDude

Disclaimer:
For informational/educational purposes only. Bugs are likely and can be reported on github.
Using this will incur AWS charges.
