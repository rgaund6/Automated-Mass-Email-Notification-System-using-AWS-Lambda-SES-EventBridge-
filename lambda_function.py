import boto3
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

ses = boto3.client('ses')

def lambda_handler(event, context):

    sender = "your-verified-sender@gmail.com"
    recipient = "your-verified-receiver@gmail.com"
    subject = "Your Daily AWS Automation Update"

    # Text Body
    text_body = """
    Hello,
    This is your daily automation update from AWS.

    Status Summary:
    - Task executed successfully
    - Status: Success

    Regards,
    Raj
    """

    # HTML Body
    html_body = """
    <html>
    <body style="font-family: Arial; padding: 20px; background:#f8f8f8;">
    <div style="background:#fff; padding:20px; border-radius:10px;">
        <h2 style="color:#0066cc;">Hello,</h2>
        <p>This is your daily automation update sent using AWS Lambda & SES.</p>

        <h3>Status Summary:</h3>
        <ul>
            <li>Task executed successfully</li>
            <li>Status: <b style="color:green;">Success</b></li>
        </ul>

        <br>
        Regards,<br>
        Raj
    </div>
    </body>
    </html>
    """

    msg = MIMEMultipart('alternative')
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = recipient

    msg.attach(MIMEText(text_body, 'plain'))
    msg.attach(MIMEText(html_body, 'html'))

    response = ses.send_raw_email(
        Source=sender,
        Destinations=[recipient],
        RawMessage={"Data": msg.as_string()}
    )

    return {"status": "Email sent successfully", "response": response}

