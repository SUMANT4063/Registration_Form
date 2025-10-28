from flask import Flask, render_template, request
import mysql.connector

app = Flask(__name__)

def get_db_connection():
    return mysql.connector.connect(
        host="iconnecttech.in",
        user="suman",
        password="iConnect@2401",
        database="iconnecttest"
    )

@app.route('/')
def form():
    return render_template('Profile.html')

@app.route('/submit', methods=['POST'])
def submit():
    try:
        # Get form data
        fname = request.form['fname']
        lname = request.form['lname']
        email = request.form['email']
        phone = request.form['phone']
        dob = request.form['dob']
        gender = request.form['gender']
        qualification = request.form['qualification']
        branch = request.form['branch']
        fatherName = request.form['fatherName']
        fatherPhone = request.form['fatherPhone']
        motherName = request.form['motherName']
        motherPhone = request.form['motherPhone']
        address = request.form['address']
        district = request.form['district']
        state = request.form['state']
        country = request.form['country']
        material = request.form['material']
        siblings = request.form['siblings']
        wife = request.form['wife']
        children = request.form['children']

        # Insert into MySQL table
        conn = get_db_connection()
        cursor = conn.cursor()
        sql = """INSERT INTO Registration_form
                (fname, lname, email, phone, dob, gender, qualification, branch,
                 fatherName, fatherPhone, motherName, motherPhone, address, district,
                 istate, country, material, siblings, wife, children)
                 VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
        values = (fname, lname, email, phone, dob, gender, qualification, branch,
                  fatherName, fatherPhone, motherName, motherPhone, address, district,
                  state, country, material, siblings, wife, children)
        cursor.execute(sql, values)
        conn.commit()

        cursor.close()
        conn.close()

        return "<h2 style='text-align:center;color:green;'>Registration Successful!</h2>"

    except Exception as e:
        return f"<h2 style='text-align:center;color:red;'>Error: {str(e)}</h2>"

if __name__ == "__main__":
    app.run(debug=True)
