#!/usr/bin/env python
from mailtosms import MailToSms
from cherrysms import SMSSender
import sys
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("username", help="Cherry SMS username (your phone number with country prefix e.g. 49 instead of +49)")
parser.add_argument("password", help="Cherry SMS password")
parser.add_argument("phoneno", help="Phone number to send SMS to (including country prefix e.g. 49 instead of +49)")
args = parser.parse_args()

sms = SMSSender(args.username, args.password)
mts = MailToSms(sms, args.phoneno)

mts.parse_msg_from_file(sys.stdin)
