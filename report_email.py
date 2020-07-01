#!/usr/bin/env python3

# 5. processes supplier-data/descriptions/,
# creates a list of name & weight of each item
# saves that information in /tmp/processed.pdf
# send /tmp/processed.pdf to automation@example.com

import os
from datetime import date
import reports
import emails


def create_summary(input_folder):
    out = []
    for root, _, files in os.walk(input_folder):
        for filename in files:
            # print(root, filename)
            with open(root+filename, 'r') as description:
                for line_nr, content in enumerate(description):
                    if line_nr == 0:
                        out.append(["name: " + content.replace('\n', '')])
                    if line_nr == 1:
                        out.append(["weight: " + content.replace('\n', '')])
                out.append([])
    return out


if __name__ == "__main__":
    input_folder = 'supplier-data/descriptions/'
    paragraph = create_summary(input_folder)
    attachment = '/tmp/processed.pdf'
    today = date.today()
    title = "Processed Update on " + str(today)
    reports.generate_report(attachment, title, paragraph)

    sender = "automation@example.com"
    receiver = "{}@example.com".format(os.environ.get('USER'))
    subject = "Upload Completed - Online Fruit Store"
    body = """
        All fruits are uploaded to our website successfully.
        A detailed list is attached to this email."""
    message = emails.generate_email(sender,
                                    receiver,
                                    subject,
                                    body,
                                    "/tmp/processed.pdf")
    emails.send_email(message)
