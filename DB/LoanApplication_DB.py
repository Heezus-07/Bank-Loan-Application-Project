import sqlite3

conn = sqlite3.connect('Loan_Application.db')
c = conn.cursor()

c.execute('''
    CREATE TABLE IF NOT EXISTS LoanApplication (
        Loan_Application_ID INTEGER PRIMARY KEY,
        loan_amount REAL,
        loan_term INTEGER,
        purpose TEXT
    )
''')

c.execute('''
    CREATE TABLE IF NOT EXISTS PersonalDetails (
        Personal_Detail_ID INTEGER PRIMARY KEY,
        Loan_Application_ID INTEGER,
        marital_status TEXT,
        title TEXT,
        other_title TEXT,
        first_name TEXT,
        last_name TEXT,
        gender TEXT,
        dob TEXT,
        email TEXT,
        phone_home TEXT,
        phone_mobile TEXT,
        phone_business TEXT,
        address_line TEXT,
        postcode TEXT,
        address TEXT,
        city TEXT,
        postcode_result TEXT,
        nationality TEXT,
        residential_status TEXT,
        id_type TEXT,
        driving_licence TEXT,
        brp_id TEXT,
        passport TEXT,
        eu_passport TEXT,
        eu_member_state_id_card TEXT,
        FOREIGN KEY (Loan_Application_ID) REFERENCES LoanApplication (Loan_Application_ID)
    )
''')

c.execute('''
    CREATE TABLE IF NOT EXISTS EmploymentDetails (
        Employment_Detail_ID INTEGER PRIMARY KEY,
        Loan_Application_ID INTEGER,
        employment_status TEXT,
        employer_name TEXT,
        occupation TEXT,
        employer_address TEXT,
        time_employment TEXT,
        self_employed_date TEXT,
        prev_employer_name TEXT,
        prev_occupation TEXT,
        prev_time_employment TEXT,
        prev_self_employed_date TEXT,
        annual_gross_salary REAL,
        net_pay_frequency TEXT,
        daily_net_pay REAL,
        weekly_net_pay REAL,
        monthly_net_pay REAL,
        other_income TEXT,
        net_annual_income REAL,
        FOREIGN KEY (Loan_Application_ID) REFERENCES LoanApplication (Loan_Application_ID)
    )
''')

c.execute('''
    CREATE TABLE IF NOT EXISTS AssetsPropertyDetails (
        Assets_Property_Detail_ID INTEGER PRIMARY KEY,
        Loan_Application_ID INTEGER,
        house_type TEXT,
        bedrooms TEXT,
        style TEXT,
        date_purchased TEXT,
        purchase_price REAL,
        mortgage_outstanding REAL,
        estimated_present_value REAL,
        monthly_repayment REAL,
        property_owned TEXT,
        lender TEXT,
        FOREIGN KEY (Loan_Application_ID) REFERENCES LoanApplication (Loan_Application_ID)
    )
''')

c.execute('''
    CREATE TABLE IF NOT EXISTS CurrentBankingDetails (
        Current_Banking_Detail_ID INTEGER PRIMARY KEY,
        Loan_Application_ID INTEGER,
        bank_name TEXT,
        account_number TEXT,
        sort_code TEXT,
        account_type TEXT,
        time_at_bank TEXT,
        credit_cards INTEGER,
        FOREIGN KEY (Loan_Application_ID) REFERENCES LoanApplication (Loan_Application_ID)
    )
''')

c.execute('''
    CREATE TABLE IF NOT EXISTS UploadDocuments (
        Document_ID INTEGER PRIMARY_KEY,
        Loan_Application_ID INTEGER,
        Document_Type TEXT,
        Document_Data_1 BLOB,
        Document_Data_2 BLOB,
        Document_Data_3 BLOB,
        FOREIGN KEY (Loan_Application_ID) REFERENCES LoanApplication (Loan_Application_ID)
    )
''')

conn.commit()
conn.close()
