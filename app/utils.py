from config import auth, db
import json
def sign_up(email, password):
    try:
        auth.create_user_with_email_and_password(email, password)
        print('succesfully registered')    
        return True
    except:
        print('Error with connection')
        return False

def write_data(table, values):
    try:
        db.child(table).set(values)
        return True
    except Exception as err:
        print(err)
        return False

def get_data(table):
    pass

def sign_in(email, password):
    try:
        auth.sign_in_with_email_and_password(email, password)
        print('Succesfully logged in')
        return True
    except Exception as err:
        _err = json.loads(err.strerror)
        _errno = err.errno
        _errmessage = _err['error']['message']
        print(_errno)
        print(_errmessage)
        return {"err": _errmessage, "errno": _errno}