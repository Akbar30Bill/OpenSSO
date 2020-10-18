import os
from psycopg2 import connect
import hashlib
from random_word import RandomWords
r = RandomWords()

dbcon = connect(
    database= os.getenv('POSTGRES_DB'),
    user= os.getenv('POSTGRES_USER'),
    password= os.getenv('POSTGRES_PASS'),
    host= os.getenv('POSTGRES_URL')
)

def create_user(username, password):
    cur = dbcon.cursor()
    cur.execute("""
    insert into
        opensso_user(username, hashed_password)
        values(%(USERNAME)s , %(PASSWORD)s)
    """, {
        'USERNAME': username,
        'PASSWORD': hashlib.sha512(('salt' + password).encode()).hexdigest()
    })
    dbcon.commit()
    return 'safa'

def create_service(name, username, password):
    PSK =  '-'.join(r.get_random_words(limit=10))
    cur = dbcon.cursor()
    cur.execute("""
    insert into
        opensso_services(service_name, username, hashed_password, pre_shared_key)
        values(%(SERVICE_NAME)s, %(USERNAME)s , %(PASSWORD)s, %(PSK)s)
    """, {
        'SERVICE_NAME': name,
        'USERNAME': username,
        'PASSWORD': hashlib.sha512(('salt' + password).encode()).hexdigest(),
        'PSK': PSK
    })
    dbcon.commit()
    return PSK
