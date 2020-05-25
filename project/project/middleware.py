from django.shortcuts import redirect
from django.urls import reverse_lazy
import jwt
import requests
import json
import time


from django.contrib.auth.models import User
from django.contrib.auth import login,logout

SSO_TOKEN = 'token'
REFRESH_TOKEN = 'rememberme'
AUTH_URL = 'http://localhost:3000/user/login'
REFRESH_URL = 'http://localhost:3000/auth/refresh-token'
PUBLIC_KEY = 'project/public.pem'
MAX_TTL_ALLOWED = 60 * 5
QUERY_PARAM = 'serviceURL'
LOGOUT_PATH = '/logout/'
USER_MODEL = User

PUBLIC_PATHS = list(map(reverse_lazy, ['public', 'index'])) # An array of paths that will not be processed by the middleware 

class SSOMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        self.public_key = open(PUBLIC_KEY,'rb').read()
        self.cookies = None

    def __call__(self, request):
        if (request.path in PUBLIC_PATHS):
            return self.get_response(request)

        if (request.path == LOGOUT_PATH):
            return self.logout(request)

        try:
            token = request.COOKIES[SSO_TOKEN]
        except :
            token = None

        try:
            rememberme = request.COOKIES[REFRESH_TOKEN]
        except:
            rememberme = None
            

        if(not token and not rememberme):
            return redirect(AUTH_URL+f"/?{QUERY_PARAM}={request.build_absolute_uri()}")
        
        if(token is not None):
            try:
                decoded = jwt.decode(token,self.public_key,algorithms='RS256')
                
                if(float(decoded['exp']) - time.time() < MAX_TTL_ALLOWED):
                    decoded['user'] = self.refresh(request=request,token={SSO_TOKEN:token})

                self.assign_user(request, decoded['user'])
            except Exception as err:
                print(err)
                return redirect(AUTH_URL+f"/?{QUERY_PARAM}={request.build_absolute_uri()}")
        else:
            try:
                decoded = jwt.decode(rememberme,self.public_key,algorithms='RS256')
                user = self.refresh(request,{REFRESH_TOKEN:rememberme})
                self.assign_user(request,user_payload=user)
            except Exception as err:
                print(err)
                return redirect(AUTH_URL+f"/?{QUERY_PARAM}={request.build_absolute_uri()}")

        response = self.get_response(request)

        if(self.cookies is not None):
            response._headers['set-cookie'] = ('Set-Cookie',self.cookies)

        return response


    def assign_user(self,request,user_payload):
        if(request.user.is_authenticated):
            return
        try:
            user = USER_MODEL.objects.get(email=user_payload['email'])
        except:
            user = USER_MODEL.objects.create_user(username=user_payload['username'], email=user_payload['email'],first_name=user_payload['firstname'],last_name=user_payload['lastname'])
        login(request, user)
        
    
    def refresh(self,request,token):
        r=requests.post(REFRESH_URL,data=token)
        self.cookies = r.headers['Set-Cookie'].replace('Lax,','Lax,\nSet-Cookie:')
        return json.loads(r.text)['user']

    def logout(self,request):
        logout(request)
        response = self.get_response(request)
        response.delete_cookie(SSO_TOKEN)
        response.delete_cookie(REFRESH_TOKEN)
        return response