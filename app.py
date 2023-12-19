from flask import Flask, render_template, request
import qrcode
from io import BytesIO
import base64

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        data = request.form['url']
        filename = "try.png"
        img = qrcode.make(data)

        # Save the image to a BytesIO object
        img_buffer = BytesIO()
        img.save(img_buffer)
        img_buffer.seek(0)

        # Convert the image to base64 for displaying in HTML
        img_str = base64.b64encode(img_buffer.read()).decode('utf-8')

        return render_template('index.html', url=data, img_str=img_str)

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
