'''
Created on 29 Apr 2021

@author: jacklok
'''
from trexlib.utils.string_util import is_empty, is_not_empty
from datetime import datetime
import logging

#logger = logging.getLogger('helper')
logger = logging.getLogger('debug')


'''
Customer Reward Summary format is
{
    [reward_format] : {
                        'latest_expiry_date'     : [expiry date],
                        'amount'                 : [reward balance],
                        }

}

'''
''' --------------- Start: Update reward summary for point and stamp--------------'''
def update_reward_summary_with_new_reward(existing_reward_summary, new_reward_details):
    reward_format               = new_reward_details.get('reward_format')
    reward_amount               = new_reward_details.get('amount')
    used_reward_amount          = new_reward_details.get('used_amount')
    program_key                 = new_reward_details.get('program_key')
    is_reach_reward_limit       = new_reward_details.get('is_reach_reward_limit')
    latest_expiry_date          = datetime.strptime(new_reward_details.get('expiry_date'), '%d-%m-%Y').date()
    existing_latest_expiry_date = None
    new_latest_expiry_date      = latest_expiry_date
    reward_balance              = reward_amount - used_reward_amount
    
    logger.debug('reward_amount=%s', reward_amount)
    logger.debug('used_reward_amount=%s', used_reward_amount)
    logger.debug('reward_balance=%s', reward_balance)
    
    if reward_balance<0:
        reward_balance=0
    
    if is_empty(existing_reward_summary):
        
        existing_reward_summary = {
                            reward_format:{
                                            'latest_expiry_date'    : new_latest_expiry_date.strftime('%d-%m-%Y'),
                                            'amount'                : reward_balance,
                                            
                                            'sources'                : [
                                                                        {
                                                                        'amount'                : reward_balance,
                                                                        'program_key'           : program_key, 
                                                                        'is_reach_reward_limit' : is_reach_reward_limit,
                                                                        }
                                                                      ]
                                            }
                                        
                            }
    else:
        reward_summary_by_reward_format = existing_reward_summary.get(reward_format)
        
        if reward_summary_by_reward_format is None:
            reward_summary_by_reward_format = {
                                                'amount': 0,
                                                }
            new_latest_expiry_date = latest_expiry_date
        else:
        
            existing_latest_expiry_date = reward_summary_by_reward_format.get('latest_expiry_date')
            existing_latest_expiry_date = datetime.strptime(existing_latest_expiry_date, '%d-%m-%Y').date()
            
            new_latest_expiry_date      = latest_expiry_date
            
            if latest_expiry_date > existing_latest_expiry_date:  
                new_latest_expiry_date = existing_latest_expiry_date
                
                
        reward_summary_by_reward_format['latest_expiry_date']   = new_latest_expiry_date.strftime('%d-%m-%Y')
        reward_summary_by_reward_format['amount']               = reward_summary_by_reward_format['amount'] + reward_balance
        
        reward_source_list = reward_summary_by_reward_format.get('sources') or []
        found_program_reward_source = False
        for reward_source in reward_source_list:
            existing_reward_source_program_key = reward_source.get('program_key')
            if existing_reward_source_program_key== program_key:
                reward_source['amount']                 += reward_balance
                reward_source['is_reach_reward_limit']  = is_reach_reward_limit
                
                found_program_reward_source = True
                break

        if found_program_reward_source==False:
            reward_source_list.append(
                                {
                                'amount'                : reward_balance,
                                'program_key'           : program_key, 
                                'is_reach_reward_limit' : is_reach_reward_limit,

                                }
                            )
        
        reward_summary_by_reward_format['sources'] = reward_source_list
        
        existing_reward_summary[reward_format]                  = reward_summary_by_reward_format
        
    return existing_reward_summary

def update_reward_summary_with_reverted_reward(existing_reward_summary, reverting_reward_details):
    reward_summary              = existing_reward_summary
    reward_format               = reverting_reward_details.get('reward_format')
    reward_amount               = reverting_reward_details.get('amount')
    
    logger.debug('update_reward_summary_with_reverted_reward: reward_format=%s', reward_format)
    logger.debug('update_reward_summary_with_reverted_reward: reward_amount=%s', reward_amount)
    
    existing_latest_expiry_date = None
    
    if is_not_empty(reward_summary):
        reward_summary_by_reward_format = reward_summary.get(reward_format)
        
        logger.debug('update_reward_summary_with_reverted_reward: reward_summary_by_reward_format=%s', reward_summary_by_reward_format)
        if reward_summary_by_reward_format:
            existing_latest_expiry_date = reward_summary_by_reward_format.get('latest_expiry_date')
            existing_latest_expiry_date = datetime.strptime(existing_latest_expiry_date, '%d-%m-%Y').date()
            
            final_reward_amount                         = reward_summary_by_reward_format['amount'] - reward_amount
            reward_summary_by_reward_format['amount']   = final_reward_amount
            reward_summary[reward_format]               = reward_summary_by_reward_format
            
            if final_reward_amount==0:
                del reward_summary[reward_format]
        
    return reward_summary

''' --------------- End: Update reward summary for point and stamp--------------'''

'''
customer entitled_voucher_summary format is
{
    voucher_key : 
                label : xxxxxx,
                image_url : xxxxxxxx,
                redeem_info_list :    [
                                        {
                                            redeem_code: xxxxxxxxxx,
                                            effective_date : xxxxxxxx,
                                            expiry_date : xxxxxxxx
                                        }
                                    ]

}

'''

''' --------------- Start: Update reward summary for voucher--------------'''
def update_customer_entiteld_voucher_summary_with_customer_new_voucher(customer_entitled_voucher_summary, customer_voucher):
    merchant_voucher        = customer_voucher.entitled_voucher_entity
    voucher_key             = merchant_voucher.key_in_str
    voucher_label           = merchant_voucher.label
    voucher_image_url       = merchant_voucher.image_public_url
    redeem_info_list        = [customer_voucher.to_redeem_info()]
    
    return update_customer_entiteld_voucher_summary_with_new_voucher_info(customer_entitled_voucher_summary, 
                                                                          voucher_key, 
                                                                          voucher_label, 
                                                                          voucher_image_url,
                                                                          redeem_info_list)

def update_customer_entiteld_voucher_summary_with_new_voucher_info(customer_entitled_voucher_summary, merchant_voucher_key, voucher_label, 
                                                              voucher_image_url, redeem_info_list):
    
    if customer_entitled_voucher_summary is None:
        customer_entitled_voucher_summary = {}
        
    voucher_summary     = customer_entitled_voucher_summary.get(merchant_voucher_key)
    
    if voucher_summary:
        customer_entitled_voucher_summary[merchant_voucher_key]['redeem_info_list'].extend(redeem_info_list)  
    else:
        voucher_summary = {
                            'label'             : voucher_label,
                            'image_url'         : voucher_image_url,
                            'redeem_info_list'  : redeem_info_list 
                            
                            }
        customer_entitled_voucher_summary[merchant_voucher_key] = voucher_summary

    return customer_entitled_voucher_summary

def update_customer_entiteld_voucher_summary_after_reverted_voucher(customer_entitled_voucher_summary, reverted_customer_voucher):
    '''
    removed entitled voucher from customer entitled voucher summary 
    '''
    logger.debug('customer_entitled_voucher_summary=%s', customer_entitled_voucher_summary)
    
    
    if customer_entitled_voucher_summary:
        merchant_voucher_key                    = reverted_customer_voucher.entitled_voucher_key
        redeem_code_of_reverting_voucher        = reverted_customer_voucher.redeem_code
        
        logger.debug('merchant_voucher_key=%s', merchant_voucher_key)
        logger.debug('redeem_code_of_reverting_voucher=%s', redeem_code_of_reverting_voucher)
        
        voucher_summary = customer_entitled_voucher_summary.get(merchant_voucher_key)
        
        logger.debug('voucher_summary=%s', voucher_summary)
        
        if voucher_summary:
            new_redeem_info_list = []
            redeem_info_list     = voucher_summary.get('redeem_info_list')
            for redeem_info in redeem_info_list:
                if redeem_info.get('redeem_code')!=redeem_code_of_reverting_voucher:
                    new_redeem_info_list.append(redeem_info)
                
            
            if len(new_redeem_info_list) ==0:
                del customer_entitled_voucher_summary[merchant_voucher_key]
            else:
                customer_entitled_voucher_summary[merchant_voucher_key]['redeem_info_list'] = new_redeem_info_list
    return customer_entitled_voucher_summary
    
    
def update_customer_entiteld_voucher_summary_after_redeemed_voucher(entitled_voucher_summary, redeemed_customer_voucher):
    return update_customer_entiteld_voucher_summary_after_reverted_voucher(entitled_voucher_summary, redeemed_customer_voucher)

''' --------------- End: Update reward summary for voucher--------------'''

''' --------------- Start: Update reward summary for prepaid--------------'''

def update_prepaid_summary_with_new_prepaid(existing_prepaid_summary, new_prepaid_summary):
    prepaid_amount              = new_prepaid_summary.get('amount')
    used_prepaid_amount         = new_prepaid_summary.get('used_amount')
    
    if is_empty(existing_prepaid_summary):
        prepaid_balance         = prepaid_amount - used_prepaid_amount
        existing_prepaid_summary = {
                                    'amount'  : prepaid_balance,
                                    }
        
    else:
        prepaid_balance = existing_prepaid_summary.get('amount') + (prepaid_amount-used_prepaid_amount)
        existing_prepaid_summary = {
                                    'amount'  : prepaid_balance,
                                    }        
                
    return existing_prepaid_summary

def update_prepaid_summary_with_reverted_prepaid(existing_prepaid_summary, reverted_prepaid_summary):
    prepaid_amount              = reverted_prepaid_summary.get('amount')
    used_prepaid_amount         = reverted_prepaid_summary.get('used_amount')
    
    if is_empty(existing_prepaid_summary):
        existing_prepaid_summary = {
                                    'amount'  : .0,
                                    }
        
    else:
        prepaid_balance = existing_prepaid_summary.get('amount') - (prepaid_amount-used_prepaid_amount)
        if prepaid_balance<0:
            prepaid_balance = .0
        
        existing_prepaid_summary = {
                                    'amount'  : prepaid_balance,
                                    }        
                
    return existing_prepaid_summary

''' --------------- End: Update reward summary for prepaid--------------'''