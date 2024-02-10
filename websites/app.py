from flask import Flask, render_template, redirect

app = Flask(__name__)

# Redirect from the default route to /profile
@app.route('/')
def home():
    return redirect('/profile')

# Serve the profile page with optional parameters
@app.route('/profile')
def profile():
    # Example of passing parameters to the template
    return render_template('index.html', name="Mustafa Alperen Cihan", title="Student at ITMO")

if __name__ == "__main__":
    app.run(debug=True)
