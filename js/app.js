const express = require('express');
const sqlite3 = require('sqlite3').verbose();
const cors = require('cors');

const app = express();
const db = new sqlite3.Database('Loan_Application.db');
app.use(cors());

// Serve static files
app.use(express.static('public'));

// Parse JSON-encoded bodies
app.use(express.json());

// Parse URL-encoded bodies
app.use(express.urlencoded({ extended: true }));

// Route to display the loan application form
app.get('/', (req, res) => {
  res.sendFile(__dirname + '/js/formApplication.html');
});

// Route to handle form submission
app.post('/submit', (req, res) => {
  const formData = req.body;

  // Save form data to the database
  saveFormData(formData)
    .then(() => {
      res.send('Loan application submitted successfully!');
    })
    .catch((err) => {
      console.error(err);
      res.status(500).send('Error occurred while saving the data');
    });
});

// Save form data to the database
function saveFormData(formData) {
  return new Promise((resolve, reject) => {
    db.serialize(() => {
      db.run('BEGIN TRANSACTION');

      // Insert LoanApplication record
      const { loan_amount, loan_term, purpose } = formData.loanApplication;
      db.run(
        'INSERT INTO LoanApplication (loan_amount, loan_term, purpose) VALUES (?, ?, ?)',
        [loan_amount, loan_term, purpose],
        function (err) {
          if (err) {
            db.run('ROLLBACK');
            reject(err);
          } else {
            const loanApplicationId = this.lastID;

            // Insert PersonalDetails record
            const {
              marital_status,
              title,
              other_title,
              first_name,
              last_name,
              gender,
              dob,
              email,
              phone_home,
              phone_mobile,
              phone_business,
              address_line,
              postcode,
              address,
              city,
              postcode_result,
              nationality,
              residential_status,
              id_type,
              driving_licence,
              brp_id,
              passport,
              eu_passport,
              eu_member_state_id_card,
            } = formData.personalDetails;
            db.run(
              `INSERT INTO PersonalDetails (
                Loan_Application_ID,
                marital_status,
                title,
                other_title,
                first_name,
                last_name,
                gender,
                dob,
                email,
                phone_home,
                phone_mobile,
                phone_business,
                address_line,
                postcode,
                address,
                city,
                postcode_result,
                nationality,
                residential_status,
                id_type,
                driving_licence,
                brp_id,
                passport,
                eu_passport,
                eu_member_state_id_card
              ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)`,
              [
                loanApplicationId,
                marital_status,
                title,
                other_title,
                first_name,
                last_name,
                gender,
                dob,
                email,
                phone_home,
                phone_mobile,
                phone_business,
                address_line,
                postcode,
                address,
                city,
                postcode_result,
                nationality,
                residential_status,
                id_type,
                driving_licence,
                brp_id,
                passport,
                eu_passport,
                eu_member_state_id_card,
              ],
              function (err) {
                if (err) {
                  db.run('ROLLBACK');
                  reject(err);
                } else {
                  const personalDetailId = this.lastID;

                  // Insert EmploymentDetails record
                  const {
                    employment_status,
                    employer_name,
                    occupation,
                    employer_address,
                    time_employment,
                    self_employed_date,
                    prev_employer_name,
                    prev_occupation,
                    prev_time_employment,
                    prev_self_employed_date,
                    annual_gross_salary,
                    net_pay_frequency,
                    daily_net_pay,
                    weekly_net_pay,
                    monthly_net_pay,
                    other_income,
                    net_annual_income,
                  } = formData.employmentDetails;
                  db.run(
                    `INSERT INTO EmploymentDetails (
                      Loan_Application_ID,
                      employment_status,
                      employer_name,
                      occupation,
                      employer_address,
                      time_employment,
                      self_employed_date,
                      prev_employer_name,
                      prev_occupation,
                      prev_time_employment,
                      prev_self_employed_date,
                      annual_gross_salary,
                      net_pay_frequency,
                      daily_net_pay,
                      weekly_net_pay,
                      monthly_net_pay,
                      other_income,
                      net_annual_income
                    ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)`,
                    [
                      loanApplicationId,
                      employment_status,
                      employer_name,
                      occupation,
                      employer_address,
                      time_employment,
                      self_employed_date,
                      prev_employer_name,
                      prev_occupation,
                      prev_time_employment,
                      prev_self_employed_date,
                      annual_gross_salary,
                      net_pay_frequency,
                      daily_net_pay,
                      weekly_net_pay,
                      monthly_net_pay,
                      other_income,
                      net_annual_income,
                    ],
                    function (err) {
                      if (err) {
                        db.run('ROLLBACK');
                        reject(err);
                      } else {
                        const employmentDetailId = this.lastID;

                        // Insert AssetsPropertyDetails record
                        const {
                          house_type,
                          bedrooms,
                          style,
                          date_purchased,
                          purchase_price,
                          mortgage_outstanding,
                          estimated_present_value,
                          monthly_repayment,
                          property_owned,
                          lender,
                        } = formData.assetsPropertyDetails;
                        db.run(
                          `INSERT INTO AssetsPropertyDetails (
                            Loan_Application_ID,
                            house_type,
                            bedrooms,
                            style,
                            date_purchased,
                            purchase_price,
                            mortgage_outstanding,
                            estimated_present_value,
                            monthly_repayment,
                            property_owned,
                            lender
                          ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)`,
                          [
                            loanApplicationId,
                            house_type,
                            bedrooms,
                            style,
                            date_purchased,
                            purchase_price,
                            mortgage_outstanding,
                            estimated_present_value,
                            monthly_repayment,
                            property_owned,
                            lender,
                          ],
                          function (err) {
                            if (err) {
                              db.run('ROLLBACK');
                              reject(err);
                            } else {
                              const assetsPropertyDetailId = this.lastID;

                              // Insert CurrentBankingDetails record
                              const {
                                bank_name,
                                account_number,
                                sort_code,
                                account_type,
                                time_at_bank,
                                credit_cards,
                              } = formData.currentBankingDetails;
                              db.run(
                                `INSERT INTO CurrentBankingDetails (
                                  Loan_Application_ID,
                                  bank_name,
                                  account_number,
                                  sort_code,
                                  account_type,
                                  time_at_bank,
                                  credit_cards
                                ) VALUES (?, ?, ?, ?, ?, ?, ?)`,
                                [
                                  loanApplicationId,
                                  bank_name,
                                  account_number,
                                  sort_code,
                                  account_type,
                                  time_at_bank,
                                  credit_cards,
                                ],
                                function (err) {
                                  if (err) {
                                    db.run('ROLLBACK');
                                    reject(err);
                                  } else {
                                    db.run('COMMIT');
                                    resolve();
                                  }
                                }
                              );
                            }
                          }
                        );
                      }
                    }
                  );
                }
              }
            );
          }
        }
      );
    });
  });
}

// Start the server
const port = 3000;
app.listen(port, () => {
  console.log(`Server is running on port ${port}`);
});
