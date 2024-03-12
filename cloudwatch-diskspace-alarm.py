import boto3

# Grab your SSO profile from ~/.aws and cat config to view or open in text editor to view your profile name

my_profile = "sso-profile-name" 

# If you need to create a profile make sure aws cli is isntalled and just run 'aws sso configure'

sess = boto3.Session(profile_name=my_profile, region_name ='eu-west-1')



sns_client = sess.client("sns")
cw = sess.client("cloudwatch")



# Set up alarm parameters (unchanged from the previous example)
alarm_name = 'MyEC2DiskSpaceAlarm'
namespace = 'AWS/EC2'
metric_name = 'DiskSpaceUtilization'
dimensions = [
    {
        'Name': 'InstanceId',
        'Value': 'i-XXXXXXXXXXXXXXXXX' # remove this comment and replace with actual instance ID
    }
]
comparison_operator = 'LessThanThreshold'
threshold = 20.0
evaluation_periods = 1
period = 1800 # remove this comment, currently set to every 30 mins but you can change to whatever you want
alarm_actions = ['arn:aws:sns:eu-west-1:XXXXXXXXX805:EC2ParserDiskSpaceAlert'] # remove this comment and replace arn with your actual sns arn

# Create the alarm
cw.put_metric_alarm(
    AlarmName=alarm_name,
    AlarmDescription='Alarm when disk space utilization is low',
    ActionsEnabled=True,
    MetricName=metric_name,
    Namespace=namespace,
    Dimensions=dimensions,
    Statistic='Average',
    ComparisonOperator=comparison_operator,
    Threshold=threshold,
    EvaluationPeriods=evaluation_periods,
    Period=period,
    AlarmActions=alarm_actions
)

print("Alarm created successfully!")
