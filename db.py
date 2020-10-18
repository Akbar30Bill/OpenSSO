import os
from psycopg2 import connect
import hashlib

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
