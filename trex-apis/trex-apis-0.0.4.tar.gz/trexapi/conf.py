'''
Created on 30 Jun 2021

@author: jacklok
'''
import os
APPLICATION_NAME                                                = os.environ.get('APPLICATION_NAME')
SECRET_KEY                                                      = os.environ.get('SECRET_KEY')
VERSION                                                         = '0.0.1'
UPDATED_DATE                                                    = '5 July 2021'

API_TOKEN_EXPIRY_LENGTH_IN_MINUTE                               = os.environ.get('API_TOKEN_EXPIRY_LENGTH_IN_MINUTE') 
