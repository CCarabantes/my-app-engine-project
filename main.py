from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        name = request.form.get('name', '')
        address = request.form.get('address', '')
        city = request.form.get('city', '')
        state = request.form.get('state', '')
        zip_code = request.form.get('zip', '')
        phone = request.form.get('phone', '')
        email = request.form.get('email', '')
        major = request.form.get('major', '')
        career_goal = request.form.get('career_goal', '')
        favorite_song = request.form.get('favorite_song', '')
        favorite_band = request.form.get('favorite_band', '')

        return f"""
        <html>
        <head><title>Submitted Info</title></head>
        <body>
            <h1>Here is the information you submitted:</h1>
            <p><b>Name:</b> {name}</p>
            <p><b>Address:</b> {address}</p>
            <p><b>City:</b> {city}</p>
            <p><b>State:</b> {state}</p>
            <p><b>Zip Code:</b> {zip_code}</p>
            <p><b>Phone:</b> {phone}</p>
            <p><b>Email:</b> {email}</p>
            <p><b>Major:</b> {major}</p>
            <p><b>Career Goal:</b> {career_goal}</p>
            <p><b>Favorite Song:</b> {favorite_song}</p>
            <p><b>Favorite Band:</b> {favorite_band}</p>
            <br><a href="/">Go Back</a>
        </body>
        </html>
        """
    return render_template("form.html")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
