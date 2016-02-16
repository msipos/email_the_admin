# email_the_admin
Short and portable script for shooting an email via Mailgun. Useful for crons, reports, etc.

Use it like this:

    some command here | email_the_admin.py "My subject line here"

Or write into a file first:

    some command here > EMAIL_TEXT
    some other command >> EMAIL_TEXT
    cat EMAIL_TEXT | email_the_admin.py "My subject"
