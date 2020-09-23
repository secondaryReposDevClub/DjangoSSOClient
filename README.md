# DjangoSSOClient
This is a sample Django Application to illustrate the use of the Django middleware for integrating DevClub apps with CASI.

[Link to SSO Server](https://github.com/devclub-iitd/SingleSignOn) 

## Prerequisites to use the SSO Middleware:
- Registration of client with SSO server.
  - Register your client with CASI at [https://auth.devclub.in/client/register](https://auth.devclub.in/client/register)
  - Specify any custom roles you may want during registration. (These can be updated/deleted at any time)
  - After registration download the public key and the configuration file for your client.
- A Django based client server into which this middleware can be integrated.

## Setup 
- Clone this repo using `git clone https://github.com/secondaryReposDevClub/DjangoSSOClient.git`
- Copy the middleware file in `DjangoSSOClient/project/project/middleware.py` into the directory that contains `settings.py` file in your Django server.
- Also copy the downloaded files `public.pem` and `config` into the same directory in which `settings.py` is located.

## Options
- **Server Config Options**: These options will be provided in the `config` file that you download from SSO. Copy Paste these options exactly from `config` into `settings.py` to avoid any configuration problems.
  1. `SSO_TOKEN`
  2. `REFRESH_TOKEN`
  3. `AUTH_URL`
  4. `REFRESH_URL`
  5. `MAX_TTL_ALLOWED`
  6. `QUERY_PARAM`
- **Client Config Options**: These options are customizable as per the client needs. Specify these in the `settings.py` file
  1. `PUBLIC_KEY` : This is the path of the public key in your server. If the public key is in the same directory as your `settings.py` file then this parameter must be equal to `'<project_name>/public.pem'`
  2. `LOGOUT_PATH`: This is the route that the user will access to logout from your client. To logout from CASI as well, specify the route in this parameter. e.g. `/logout/`. **Note**: This parameter must exaclty match `request.path` for logout action at CASI to be triggered.
  3. `USER_MODEL` : This is the model that the middleware uses to update basic authentication fields of a user. By default it is `django.contrib.auth.models.User`. However if you have implemented a model that subclasses `AbstractUser` or a custom model, then ensure that the model has the following fields `username, email, first_name, last_name`.
  4. `PUBLIC_PATHS` : This is an array of path regexes that will be matched against `request.path`. If there is a match then the path will not be processed by the middleware. In essence, if the user visiting a path matches any of the regex in this array then it will be a public path.
  5. `UNAUTHORIZED_HANDLER` : This is a view that should be called if the user is unauthorized to access a given path. It is a normal Django view function as you specify in `views.py`
  6. `DEFAULT_ROLES` : An array of roles that all authorized users should have when accessing non-public paths.
  7. `ROLES` : A dictionary mapping route regexes to corresponding role arrays. If the path accessed (`request.path`) regex-matches with any of the keys in this dictionary then the user is authorized only if he has all the roles specified in the corresponding value of the key (a role array). See `ROLES` in `middleware.py` for an example.
  

For any issues/doubts raise an issue here [Issues](https://github.com/secondaryReposDevClub/DjangoSSOClient/issues)
