from django.shortcuts import redirect
import jwt
import requests
import json
import time

SSO_TOKEN = 'token'
REFRESH_TOKEN = 'rememberme'
AUTH_URL = 'http://localhost:3000/user/login'
REFRESH_URL = 'http://localhost:3000/auth/refresh-token'
PUBLIC_KEY = 'project/public.pem'
MAX_TTL_ALLOWED = 60 * 5

class SSOMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        self.public_key = open(PUBLIC_KEY,'rb').read()
        self.cookies = None

    def __call__(self, request):
        try:
            token = request.COOKIES[SSO_TOKEN]
        except :
            token = None

        try:
            rememberme = request.COOKIES[REFRESH_TOKEN]
        except:
            rememberme = None
            
            

        if(not token and not rememberme):
            return redirect(AUTH_URL+f"/?service_url={request.build_absolute_uri()}")
        
        if(token is not None):
            try:
                decoded = jwt.decode(token,self.public_key,algorithms='RS256')
                
                if(float(decoded['exp']) - time.time() < MAX_TTL_ALLOWED):
                    decoded['user'] = self.refresh(request=request,token={SSO_TOKEN:token})

                self.assign_user(request, decoded['user'])
            except:
                return redirect(AUTH_URL+f"/?service_url={request.build_absolute_uri()}")
        else:
            try:
                decoded = jwt.decode(rememberme,self.public_key,algorithms='RS256')
                user = self.refresh(request,{REFRESH_TOKEN:rememberme})
                self.assign_user(request,user_payload=user)
            except:
                return redirect(AUTH_URL+f"/?service_url={request.build_absolute_uri()}")

        response = self.get_response(request)

        if(self.cookies is not None):
            response._headers['set-cookie'] = ('Set-Cookie',self.cookies)

        return response


    # TO implement after db is ready
    def assign_user(self,request,user_payload):
        print(f"Assigning {user_payload} to request.user")

    def refresh(self,request,token):
        r=requests.post(REFRESH_URL,data=token)
        self.cookies = r.headers['Set-Cookie'].replace('Lax,','Lax,\nSet-Cookie:')
        return json.loads(r.text)['user']
