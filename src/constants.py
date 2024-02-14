""" Tipų konstantos ir stulpeliai su tipais.
"""

DATETIME_TYPE = 'datetime64[ns]'
STRING_TYPE = 'string'
CATEGORY_TYPE = 'category'
NUMERIC_TYPE = 'numeric'
BOOL_TYPE = 'bool'

cols_and_types = {
    'PERIOD':DATETIME_TYPE,
    'CUSTOMER_NR_H':STRING_TYPE,
    'CUSTOMER_AGE_GROUP':CATEGORY_TYPE,
    'CUSTOMER_GENDER':CATEGORY_TYPE,
    'SUBSCRIBER_NR_H':STRING_TYPE,
    'SUBSCRIBER_ON_DATE':DATETIME_TYPE,
    'SUBSCRIBER_OFF_DATE':DATETIME_TYPE,
    'SUBSCRIBER_STATUS':CATEGORY_TYPE,
    'PLAN_H':CATEGORY_TYPE,
    'PLAN_ON_DATE':DATETIME_TYPE,
    'PLAN_OFF_DATE':DATETIME_TYPE,
    'PLAN_CHANGE_FLAG':BOOL_TYPE,
    'OFFER_PREV':CATEGORY_TYPE,
    'PLAN_PREV_H':CATEGORY_TYPE,
    'TP_FLAG':BOOL_TYPE,
    'DATA_USAGE_MB':NUMERIC_TYPE,
    'MIN_BUCKET':NUMERIC_TYPE,
    'SMS_BUCKET':NUMERIC_TYPE,
    'DATA_BUCKET_MB':NUMERIC_TYPE,
    'SERVICE_CONTRACT_STATUS':CATEGORY_TYPE,
    'SERVICE_CONTRACT_ON_DATE':DATETIME_TYPE,
    'SERVICE_CONTRACT_OFF_DATE':DATETIME_TYPE,
    'USED_DEVICE_FLAG':BOOL_TYPE,
    'USED_DEVICE_TYPE':CATEGORY_TYPE,
    'USED_DEVICE_HIERARCHY_GROUP':CATEGORY_TYPE,
    'USED_DEVICE_HIERARCHY_TYPE':CATEGORY_TYPE,
    'FMF_NORM':NUMERIC_TYPE,
    'FMF_CHANGE':CATEGORY_TYPE,
    'ADDRESS_ID_H':STRING_TYPE,
    #'POSTAL_CODE':STRING_TYPE, # Pasto kodo duomenyse nera
    'GRID_ID_500_H':STRING_TYPE
}