# Automated-Mass-Email-Notification-System-using-AWS-Lambda-SES-EventBridge-
This project demonstrates a fully serverless automated email notification system built using AWS Lambda, Amazon SES, and Amazon EventBridge. It automatically sends scheduled and event-based emails without requiring any servers.


Features  : 

100% Serverless (no EC2, no servers)

Scheduled automatic emails using EventBridge

HTML formatted professional emails

Uses AWS SES for reliable email delivery

IAM Role–based secure execution

Daily notification automation


Project Architecture :

The system sends scheduled email notifications every day at a predefined time.
EventBridge triggers the Lambda function → Lambda executes email logic → SES delivers the email.


Tech Stack : 
AWS Lambda, Amazon SES, Amazon EventBridge, IAM role and python (3.10)


Workflow Steps
1. SES Setup

Verify Sender & Receiver emails

SES → Verified Identities

Required to remove “Email address not verified” errors

(See: assets/ses-setup.png)

2. IAM Role Creation

IAM → Create Role → Lambda

Attach:

AmazonSESFullAccess

CloudWatchFullAccess

(See: assets/iam-role.png)

3. Create Lambda Function (Python 3.10)

Runtime: Python 3.10

Execution Role: LambdaEmailRole

Paste the code from lambda_function.py

Test the function manually

(See: assets/lambda-config.png)

4. EventBridge Schedule

EventBridge → Create Schedule

Type: Recurring

Cron time set to daily at 10:00 AM

Target: Lambda Function
(See: assets/eventbridge-schedule.png)

 Result  :
The system automatically sends email at the scheduled time.

 Test Case : 
Test Case Name: EmailTest

Expected Output:

Lambda executes successfully

SES sends email

Receiver mailbox receives professional HTML email

Architecture : 

<img width="576" height="288" alt="image" src="https://github.com/user-attachments/assets/a531c344-7a8a-4e15-9c90-d36c7f90d90f" />




Conclusion : 

This project successfully demonstrates a serverless and automated email notification system using AWS Lambda, Amazon SES, and EventBridge.
It is reliable, fast, cost-efficient, and scalable for real-world automation including reminders, alerts, reports, and OTP delivery.

