import boto3
import collections
from datetime import datetime
import calendar

client = boto3.client('cloudwatch')
ec = boto3.client('ec2')

def lambda_handler(event, context):
    reservations = ec.describe_instances()
        for r in reservations['Reservations']:
            for i in r['Instances']:
                instance_id = i['InstanceId']
                for t in i['Tags']:
                    if t['Key'] == 'Name':
                        iname = t['Value']
                        alarm = client.put_metric_alarm(
                        AlarmName='CPU Alarm ' + iname ,
                        MetricName='CPUUtilization',
                        Namespace='AWS/EC2',
                        Statistic='Average',
                        ComparisonOperator='GreaterThanOrEqualToThreshold',
                        Threshold=70.0,
                        Period=300,
                        EvaluationPeriods=1,
                        Dimensions=[
                            {
                                'Name': 'InstanceId',
                                'Value': instance_id
                            }
                        ],
                        Unit='Percent',
                        ActionsEnabled=True,
                        AlarmActions=['arn:aws:sns:us-east-1:012345678912:CloudWatch'])
