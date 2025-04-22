import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text      import MIMEText


SENDER   = "analystcopilot@gmail.com"
PASSWORD = "cqca rgzr vxtf rhij"
SMTP_HOST = "smtp.gmail.com"
SMTP_PORT = 465

def make_digest():
    headlines = [
        "• Q1 earnings for ACME Corp.",
        "• 10‑K summary for Globex Inc.",
        "• RSS: 5 new TechCrunch posts"
    ]
    return "<br>".join(headlines)

def compose_email(to_addr, subject, html_body):
    msg = MIMEMultipart("alternative")
    msg["From"]    = SENDER
    msg["To"]      = to_addr
    msg["Subject"] = subject

    # plain‑text fallback
    text = html_body.replace("<br>", "\n").replace("•", "-")
    msg.attach(MIMEText(text, "plain"))
    msg.attach(MIMEText(html_body, "html"))
    return msg

def send_email(msg):
    with smtplib.SMTP_SSL(SMTP_HOST, SMTP_PORT) as server:
        server.login(SENDER, PASSWORD)
        server.send_message(msg)
    print("Digest sent!")

if __name__ == "__main__":
    html = f"<h2>Today’s Digest</h2><p>{make_digest()}</p>"
    email_msg = compose_email(
        to_addr="sridhanvi07@gmail.com",
        subject="Your Copilot Digest",
        html_body=html
    )
    send_email(email_msg)
