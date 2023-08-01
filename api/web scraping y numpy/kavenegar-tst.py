from kavenegar import *

api = KavenegarAPI('')
params = { 'sender': '10008663', 'receptor': '', 'message' :'سلام از طرف پایتون' }
response = api.sms_send(params)


