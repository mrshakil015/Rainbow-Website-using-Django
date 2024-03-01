from flask import Flask, render_template, redirect, url_for, request

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def index():
    data_dict ={}
    if request.method == 'POST':
        data_dict =entrydata()
        studentname = data_dict['studentname']
        message = "Form Submitted Successfully"
        return render_template('entryform.html', message = message)
    return render_template('entryform.html')

def entrydata():
    data = {}
    studentname = request.form['studentname']
    institute = request.form['institute']
    designation = request.form['designation']
    course = request.form['course']
    image_file = request.files['image']
    image_name = image_file.filename
    print("Image: ",image_file.filename)
    if image_file:
        image_file.save('static/' + image_name)

    data = {'studentname': studentname, 'institute': institute, 'designation': designation, 'course': course, 'image_name': image_name}
    print(data['studentname'])
    
    return data


if __name__ == '__main__':
    app.run(debug=True, port=8080)