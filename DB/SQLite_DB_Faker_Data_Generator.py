import sqlite3
from faker import Faker
import random

fake = Faker('en_GB')

conn = sqlite3.connect('credit_data.db')
c = conn.cursor()

# Create tables for personal information and credit accounts
c.execute('''CREATE TABLE IF NOT EXISTS personal_info (
                id INTEGER PRIMARY KEY,
                first_name TEXT,
                last_name TEXT,
                address TEXT,
                post_code TEXT,
                date_of_birth TEXT,
                phone_number TEXT,
                email TEXT
            )''')

c.execute('''CREATE TABLE IF NOT EXISTS credit_accounts (
                id INTEGER PRIMARY KEY,
                account_type TEXT,
                date_opened TEXT,
                credit_limit INTEGER,
                loan_amount INTEGER,
                current_balance INTEGER,
                payment_history TEXT,
                credit_utilization REAL,
                public_records TEXT,
                inquiries TEXT,
                collections TEXT,
                credit_age INTEGER,
                credit_accounts INTEGER,
                credit_mix TEXT
            )''')

for i in range(1000):
    # Personal information
    first_name = fake.first_name()
    last_name = fake.last_name()
    address = fake.street_address() + ', ' + fake.city()
    post_code = fake.postcode()
    date_of_birth = fake.date_of_birth(minimum_age=18, maximum_age=80).strftime('%Y-%m-%d')
    phone_number = fake.phone_number()
    email = fake.email()
    c.execute('''INSERT INTO personal_info (first_name, last_name, address, post_code, date_of_birth, phone_number, email)
                 VALUES (?, ?, ?, ?, ?, ?, ?)''',
              (first_name, last_name, address, post_code, date_of_birth, phone_number, email))

    # Credit accounts
    account_type = random.choice(['credit_card', 'loan', 'mortgage'])
    date_opened = fake.date_between(start_date='-10y', end_date='today').strftime('%Y-%m-%d')
    credit_limit = random.randint(1000, 200000)
    loan_amount = random.randint(1000, 100000)
    current_balance = random.randint(0, loan_amount)
    payment_history = random.choice(['on_time', 'late'])
    credit_utilization = round(random.uniform(0.1, 1.0), 2)
    public_records = random.choice(['bankruptcy', 'lien', 'judgment', 'none'])
    inquiries = random.choice(['lender', 'employer', 'landlord', 'none'])
    collections = random.choice(['yes', 'no'])
    credit_age = random.randint(1, 50)
    credit_accounts = random.randint(1, 10)
    credit_mix = random.choice(['secured', 'unsecured', 'both'])
    c.execute('''INSERT INTO credit_accounts (account_type, date_opened, credit_limit, loan_amount, current_balance, payment_history,
                 credit_utilization, public_records, inquiries, collections, credit_age, credit_accounts, credit_mix)
                 VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',
              (account_type, date_opened, credit_limit, loan_amount, current_balance, payment_history,
               credit_utilization, public_records, inquiries, collections, credit_age, credit_accounts, credit_mix))

conn.commit()
conn.close()
