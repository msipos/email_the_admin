#!/usr/bin/env python

"""

  Easy script to send emails to the admin through Mailgun.  Useful for crons, reports, etc.

  Use it like this:

    some command here | email_the_admin.py "My subject line here"

  Or write into a file first:

    some command here > EMAIL_TEXT
    some other command >> EMAIL_TEXT
    cat EMAIL_TEXT | email_the_admin.py "My subject"

"""

import base64
import os
import sys
import urllib
import urllib2

# NOTE: Fill in your details below to make script easier to use.
ADMIN_EMAIL = os.environ.get('ADMIN_EMAIL', 'example@example.com')
MG_API_TOKEN = os.environ.get('MG_API_TOKEN', 'key-################################')
MG_DOMAIN = os.environ.get('MG_DOMAIN', 'mg.example.com')

def send_email(subject, text):
    data = {
        "from": "Robot <mailgun@%s>" % MG_DOMAIN,
        "to": ADMIN_EMAIL,
        "subject": subject,
        "text": text,
        "html": '<html><body><pre>\n' + text + '\n</pre></body></html>'
    }

    url = "https://api.mailgun.net/v3/%s/messages" % MG_DOMAIN
    req = urllib2.Request(url, urllib.urlencode(data))
    base64string = base64.encodestring('api:%s' % MG_API_TOKEN).replace('\n', '')
    req.add_header("Authorization", "Basic %s" % base64string)
    result = urllib2.urlopen(req)

    code = result.getcode()
    if code != 200:
        raise RuntimeError('Request failed with HTTP code=%d and info=%r' % (code, result.info()))

def main():
    subject = 'Admin Email'
    if len(sys.argv) == 2:
        subject = sys.argv[1]

    contents = sys.stdin.read()

    print('Sending email to admin with subject "%s" and content length %d...' % (subject, len(contents)))

    send_email(subject, contents)

    print('Email successfully sent')

if __name__=='__main__':
    main()
