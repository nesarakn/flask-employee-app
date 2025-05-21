from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def employee_form():
    employee_data = None
    if request.method == 'POST':
        # Get form data
        name = request.form['name']
        email = request.form['email']
        department = request.form['department']
        
        # Package the data into a dictionary
        employee_data = {
            'name': name,
            'email': email,
            'department': department
        }
        
        # Log the data to the console (for debugging)
        print(employee_data)

    # Render the form template and pass data to it
    return render_template('form.html', employee=employee_data)

if __name__ == '__main__':
    app.run(debug=True)
