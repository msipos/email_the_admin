# email_the_admin
Short and portable script for shooting an email via Mailgun. Useful for crons, reports, etc.

Use it like this:

    some command here | email_the_admin.py "My subject line here"

Or write into a file first:

    some command here > EMAIL_TEXT
    some other command >> EMAIL_TEXT
    cat EMAIL_TEXT | email_the_admin.py "My subject"

**Note:** You can edit the file email_the_admin.py to enter your Mailgun credentials and admin email address.  Alternatively you can use the script like this:

    some command here | ADMIN_EMAIL="example@example.com" MG_API_TOKEN="..." MG_DOMAIN="..." email_the_admin.py "My subject line here"
