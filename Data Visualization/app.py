from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')  # Replace with actual about content

@app.route('/home')
def home():
    return render_template('home.html')  # Replace with actual home content

@app.route('/visualization')
def visualization():
    # Sample list of image filenames (replace with actual filenames)
    images = ['1.png','2.png','3.png','7.png','5.png','6.png','4.png']
    return render_template('visualization.html', images=images)

@app.route('/contact')
def contact():
    return render_template('index.html')  # Replace with actual contact content

if __name__ == '__main__':
    app.run(debug=True)
