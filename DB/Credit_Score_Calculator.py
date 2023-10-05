import sqlite3
import random

conn = sqlite3.connect('credit_data.db')
c = conn.cursor()

c.execute('''ALTER TABLE personal_info
              ADD COLUMN credit_score INTEGER''')

def calculate_credit_score(person_id):
    c.execute('''SELECT *
                  FROM personal_info
                  WHERE rowid=?''', (person_id,))
    personal_info = c.fetchone()
    c.execute('''SELECT *
                  FROM credit_accounts
                  WHERE rowid=?''', (person_id,))
    credit_accounts = c.fetchall()

    score = 0
    age = 2023 - int(personal_info[5][:4])
    score += age * 2

    credit_limit = int(credit_accounts[0][3])
    current_balance = int(credit_accounts[0][5])
    if credit_limit == 0:
        credit_utilization_factor = 0
    else:
        credit_utilization_factor = current_balance / credit_limit
    score += int(credit_utilization_factor * 400)

    credit_history_factor = 0
    if credit_accounts[0][6] == 'on_time':
        credit_history_factor += 100
    else:
        credit_history_factor -= 50
    if credit_accounts[0][8] == 'none':
        credit_history_factor += 100
    else:
        credit_history_factor -= 300
    if credit_accounts[0][9] == 'no':
        credit_history_factor += 700
    score += credit_history_factor

    score = min(max(score, 300), 1000)

    if score == 300:
        score = random.randint(300, 500)

    if score == 1000:
        score = random.randint(700, 820)

    c.execute('''UPDATE personal_info
                  SET credit_score=?
                  WHERE rowid=?''', (score, person_id))
    conn.commit()

c.execute('''SELECT rowid FROM personal_info''')
person_ids = c.fetchall()
for person_id in person_ids:
    calculate_credit_score(person_id[0])

conn.close()
