from flask import Flask, render_template, request

app = Flask(__name__)

# Route to render the HTML form
@app.route('/')
def upload_file():
    return render_template('upload.html')

# Route to handle file upload
@app.route('/upload', methods=['POST'])
def upload_files():
    if request.method == 'POST':
        # Get the files from the request
        file1 = request.files['file1']
        file2 = request.files['file2']
        
        # Save the files to a specified location
        file1.save('uploads/' + file1.filename)
        file2.save('uploads/' + file2.filename)
        
        return 'Files uploaded successfully.'

if __name__ == '__main__':
    app.run(debug=True)
