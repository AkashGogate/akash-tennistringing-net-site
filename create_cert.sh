openssl req -x509 -nodes -newkey rsa:2048 \
  -subj '/C=US/ST=New Jersey/L=Princeton/O=Akash Stringing/OU=/CN=akash.tennistringing.net/emailAddress=akash.gogate@gmail.com' \
  -addext 'subjectAltName = DNS:*.tennistringing.net.com, DNS:d33uelcxk1rqho.cloudfront.net' \
  -keyout akashstringing.key \
  -out .akashstringing.pem
