# DjangoSSOClient

Execute the following commands in a directory of your choice.

```
git clone https://github.com/Harsh14901/DjangoSSOClient.git
cd DjangoSSOClient
python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt
cd project
python3 manage.py runserver

```

Also run the auth server at localhost:3000

Now open your browser and go to `localhost:8000/`
There is another endpoint you may wish to visit `localhost:8000/p1`

TO logout visit `localhost:8000/logout` 

For testing keep a look at the cookies that are being set in the browser.
