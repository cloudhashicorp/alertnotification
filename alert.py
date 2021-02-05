       import boto3
              import collections
              from datetime import datetime
              import calendar

              SNS_TOPIC_ARN = '${SNSTopicArn}'
              client = boto3.client('cloudwatch')

              def get_instance_id(event):
                  return event['detail']['instance-id']
                            
              def lambda_handler(event, context):
                  instance_id = get_instance_id(event)
                  alarm = client.put_metric_alarm(
                      AlarmName='High CPU Alarm ' + instance_id ,
                      MetricName='CPUUtilization',
                      Namespace='AWS/EC2',
                      Statistic='Average',
                      ComparisonOperator='GreaterThanOrEqualToThreshold',
                      Threshold=80.0,
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
                      AlarmActions=[SNS_TOPIC_ARN])
                      
                  instance_id = get_instance_id(event)
                  alarm = client.put_metric_alarm(
                      AlarmName='OK CPU Alarm ' + instance_id ,
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
                      OKActions=[SNS_TOPIC_ARN])
