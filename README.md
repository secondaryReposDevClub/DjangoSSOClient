# DjangoSSOClient

Execute the following commands in a directory of your choice.

```
git clone https://github.com/Harsh14901/DjangoSSOClient.git
cd DjangoSSOClient
python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt
cd project
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py runserver 3000

```

Also run the auth server at `localhost:8000`

Now open your browser and go to `localhost:3000/`
Everything should be up and running by now. Create some good old notes and have fun!

For testing keep a look at the cookies that are being set in the browser.
