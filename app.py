from flask import Flask, request, render_template_string
import os

app = Flask(__name__)

# Tentukan direktori untuk menyimpan file yang diupload
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Pastikan direktori upload ada
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/upload')
def upload_page():
    return render_template_string('''
    <html>
    <body>
        <h1>Upload Gambar</h1>
        <form action="/upload" method="POST" enctype="multipart/form-data">
            <input type="file" name="image" accept="image/*" required>
            <button type="submit">Upload</button>
        </form>
    </body>
    </html>
    ''')

@app.route('/upload', methods=['POST'])
def upload_image():
    if 'image' not in request.files:
        return 'No file part', 400

    file = request.files['image']

    if file.filename == '':
        return 'No selected file', 400

    # Simpan file di folder uploads
    filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
    file.save(filepath)
    return f'Gambar berhasil di-upload! File disimpan di {filepath}'
from flask import Flask, render_template, request

app = Flask(__name__)

menu = {
    "Espresso": 20000,
    "Latte": 25000,
    "Cappuccino": 30000,
    "Mocha": 35000,
    "Tea": 15000,
    "Cake Slice": 20000,
}

order = {}

@app.route("/")
def index():
    return render_template("index.html", menu=menu, order=order)

@app.route("/add", methods=["POST"])
def add_to_order():
    item = request.form.get("item")
    quantity = int(request.form.get("quantity", 1))
    if item in menu:
        order[item] = order.get(item, 0) + quantity
    return render_template("index.html", menu=menu, order=order)

@app.route("/clear")
def clear_order():
    order.clear()
    return render_template("index.html", menu=menu, order=order)

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)