from config import auth, db
# db = firebase.database()

def sign_up(email, password):
    try:
        auth.create_user_with_email_and_password(email, password)
        print('Successed')
    except:
        print('Error with connection')


def register():
    email = input('Enter an email for your new account\n>>> ')
    password = input('Enter a new password \n>>> ')
    confirmedPassword = input(f'Confirm your "{password}" password again\n>>> ')
    if password == confirmedPassword:
        sign_up(email, password)


def write_date(table, values):
    try:
        db.child(table).set(values)
    except Exception as err:
        print(err)

# auth.sign_in_with_email_and_password(email, password)

def get_data(table):


data = {
    "name": 'Apple',
    "price": 25,
    "weight": '50t'
}

write_date("fruit", data)
