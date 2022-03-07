from config import auth, db

def sign_up(email, password):
    try:
        auth.create_user_with_email_and_password(email, password)
        print('succesfully registered')
    except:
        print('Error with connection')


def write_data(table, values):
    try:
        db.child(table).set(values)
    except Exception as err:
        print(err)

def get_data(table):
    pass

def sign_in(email, password):
    pass
