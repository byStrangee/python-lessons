from config import auth, db
import json



def sign_up(email, password):
    try:
        auth.create_user_with_email_and_password(email, password)
        print('succesfully registered')    
        return True
    except Exception as err:
        print(err)
        return False

def write_data(table, values):
    try:
        db.child(table).set(values)
        return True
    except Exception as err:
        print(err)
        return False

def get_data(table):
    try:
        d = db.child(table).get()
        return d.val()
    except Exception as err:
        return err
    

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
    
def add_new_user(email, password, _id):
    user = sign_up(email, password)
    if user:
        write_data(_id, {"email": email})
    else:
        print('ERROR')
        return False
    
def login(email, password):
    user = sign_in(email, password)
    if user:
        w = _cipher.crypt(email)
        return db.child(w)
        # name = get_data(w)
        # for i, k in name.items():
        #     print(i, k)
    else:
        return "Email or password incorrect"
