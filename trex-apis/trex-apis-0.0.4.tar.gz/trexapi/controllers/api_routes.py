'''
Created on 30 Jun 2021

@author: jacklok
'''

from flask import Blueprint, request, Response, session 
from flask_restful import Resource, abort
import logging
from trexlib.utils.log_util import get_tracelog
from flask_httpauth import HTTPBasicAuth
from trexapi import conf
from flask_restful import Api
from trexmodel.utils.model.model_util import create_db_client
from trexmodel.models.datastore.merchant_models import MerchantUser,\
    MerchantAcct
import hashlib
from random import random
from trexlib.utils.string_util import random_string, is_not_empty
from flask.json import jsonify
from datetime import datetime, timedelta
from trexapi import conf as api_conf
from trexlib.utils.crypto_util import encrypt_json
from trexapi.decorators.api_decorators import auth_token_required
from trexapi.libs.flask_auth_wrapper import HTTPBasicAuthWrapper

#logger = logging.getLogger('api')
logger = logging.getLogger('debug')

auth = HTTPBasicAuth()
#auth = HTTPBasicAuthWrapper()


api_bp = Blueprint('api_base_bp', __name__,
                                 template_folder='templates',
                                 static_folder='static',
                                 url_prefix='/api/v1')

api = Api(api_bp)

@auth.verify_password
def verify_user_auth(username, password):
    if not (username and password):
        return False
    
    db_client   = create_db_client(caller_info="verify_user_auth")
    valid_auth  = False
    
    with db_client.context():
        merchant_user = MerchantUser.get_by_username(username)
        
        if merchant_user:
            
            md5_hashed_password = hashlib.md5(password.encode('utf-8')).hexdigest()
            
            logger.debug('verify_user_auth: username=%s', username)
            logger.debug('verify_user_auth: password=%s', password)
            logger.debug('verify_user_auth: md5_hashed_password=%s', md5_hashed_password)
            
            if merchant_user.is_valid_password(md5_hashed_password):
                valid_auth = True
            else:
                logger.warn('Invalid merchant password')
        else:
            logger.warn('Invalid merchant username=%s', username)    
        
    return valid_auth

def __generate_random():
    return hashlib.md5(str(random_string(6)).encode('utf-8')).hexdigest()

def default_generate_nonce():
    session["auth_nonce"] = __generate_random()
    return session["auth_nonce"]
 
def default_verify_nonce(nonce):
    return nonce == session.get("auth_nonce")

def default_generate_opaque():
    session["auth_opaque"] = __generate_random()
    return session["auth_opaque"]

def default_verify_opaque(opaque):
    return opaque == session.get("auth_opaque")
    
class APIBaseResource(Resource):
    @property
    def realm(self):
        return 'base'
    
    def generate_ha1(self, username, password):
        a1 = username + ":" + self.realm + ":" + password
        a1 = a1.encode('utf-8')
        return hashlib.md5(a1).hexdigest()
    
    def generate_token(self, acct_id, username):
        expiry_datetime = datetime.now() + timedelta(minutes = int(api_conf.API_TOKEN_EXPIRY_LENGTH_IN_MINUTE))
        
        logger.debug('expiry_datetime=%s', expiry_datetime)
        
        token_content =  {
                            'acct_id'           : acct_id,
                            'username'          : username,
                            'expiry_datetime'   : expiry_datetime.strftime('%d-%m-%Y %H:%M:%S'),
                            }
        
        logger.debug('token_content=%s', token_content)
        
        return (expiry_datetime, encrypt_json(token_content))
    
    
class APIVersionResource(APIBaseResource):
    
    @auth.login_required
    def get(self):
        output_json =  {
                        'version'   :   conf.VERSION,
                        'username'  :   auth.current_user()
                        }
        
        return output_json
    
class APIResource(APIBaseResource):
    
    def get(self):
        return conf.VERSION    
    
class AuthenticateAPIResource(APIBaseResource):  
    
    @auth.login_required
    def post(self):
        username    = auth.current_user()
        
        acct_id = request.headers.get('x-acct-id')
        api_key = request.headers.get('x-api-key')
        
        logger.debug('acct_id=%s', acct_id)    
        logger.debug('api_key=%s', api_key)
        
        is_authenticated = False
        output_json = {}
        
        if is_not_empty(acct_id) and is_not_empty(api_key):
            db_client = create_db_client(caller_info="AuthenticateAPIResource.post")
            with db_client.context():
                merchant_acct = MerchantAcct.fetch(acct_id)
            
                if merchant_acct:
                    if api_key == merchant_acct.api_key:
                        merchant_user               = MerchantUser.get_by_username(username)
                        (expiry_datetime, token)    = self.generate_token(acct_id, username)
                        #session['auth_username']    = username
                        #session['acct_id']          = acct_id
                        
                        logger.debug('token=%s', token)
                        logger.debug('auth_username=%s', username)
            
                        output_json =  {
                                        'auth_token'        : token,
                                        'expires_in'        : int(api_conf.API_TOKEN_EXPIRY_LENGTH_IN_MINUTE) * 60,
                                        #'expiry_datetime'   : expiry_datetime.strftime('%d-%m-%Y %h:%M:$S'),
                                        'granted_outlet'    : merchant_user.granted_outlet_details_list,
                                        'username'          : merchant_user.username,
                                        'name'              : merchant_user.name,
                                        'is_admin'          : merchant_user.is_admin,
                                        'granted_access'    : merchant_user.permission.get('granted_access'),
                                        'gravatar_url'      : merchant_user.gravatar_url,
                                        }
            
                        logger.debug('output_json=%s', output_json)
                        
                        is_authenticated = True
                    
            if is_authenticated:
                return output_json
                    
        abort(401)
        
        


class SecureAPIResource(AuthenticateAPIResource):  
    
    def __init__(self):
        super(SecureAPIResource, self).__init__()  
    
    
class CheckAuthTokenResource(SecureAPIResource):
    
    @auth_token_required
    def get(self):
        return 'Ping'             
    
     
api.add_resource(APIResource,            '/')
api.add_resource(APIVersionResource,            '/version')
api.add_resource(AuthenticateAPIResource,       '/auth')
api.add_resource(CheckAuthTokenResource,       '/auth-check')    
    
        
        
        
        