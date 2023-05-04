from kavenegar import *


def send_otp_code(phone_number, code):
    try:
        api = KavenegarAPI('342F646D5137715A6F6830477A785935614D61435570454B39592F416E347A7A7A736D2F41356747426D6F3D')
        params = {
            'sender': '',
            'receptor': phone_number,
            'massage': f'{code}کدتاییدشما'
        }
        response = api.sms_send(params)
        print(response)
    except APIException as e:
        print(e)
    except HTTPException as e:
        print(e)
