
# import modul lain yang Anda butuhkan

from flask import Flask, request, render_template_string
import os

app = Flask(__name__)

# Tentukan direktori untuk menyimpan file yang diupload
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Pastikan direktori upload ada
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Rute untuk menampilkan form upload gambar
@app.route('/')
def index():
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

# Rute untuk menangani upload gambar
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

if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask, render_template, request

app = Flask(__name__)

# Menu caffeshop
menu = {
    "Espresso": 20000,
    "Latte": 25000,
    "Cappuccino": 30000,
    "Mocha": 35000,
    "Tea": 15000,
    "Cake Slice": 20000,
}

# Pesanan pelanggan
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
        


# Fungsi untuk menampilkan menu
def show_menu():
    print("=== Menu Caffeshop ===")
    for item, price in menu.items():
        print(f"{item}: Rp{price}")

# Fungsi untuk menambahkan item ke pesanan
def add_to_order(order, item, quantity):
    if item in menu:
        order[item] = order.get(item, 0) + quantity
        print(f"✅ {quantity}x {item} ditambahkan ke pesanan Anda.")
    else:
        print(f"⚠ {item} tidak ada di menu.")

# Fungsi untuk melihat pesanan
def view_order(order):
    if not order:
        print("Pesanan Anda kosong.")
    else:
        print("=== Pesanan Anda ===")
        total = 0
        for item, quantity in order.items():
            price = menu[item] * quantity
            total += price
            print(f"{item} ({quantity}x): Rp{price}")
        print(f"Total: Rp{total}")

# Fungsi untuk menampilkan QR Code yang sudah ada
from PIL import Image

# Membuka file gambar
image = Image.open('qrthoriq.png')  # Ganti dengan nama file gambar Anda

# Informasi tentang gambar
print("Format:", image.format)
print("Ukuran:", image.size)
print("Mode:", image.mode)

image = Image.open('qrthoriq.png')

# Menu caffeshop
menu = {
    "Espresso": 20000,
    "Latte": 25000,
    "Cappuccino": 30000,
    "Mocha": 35000,
    "Tea": 15000,
    "Cake Slice": 20000
}

# Pesanan pelanggan
order = {}

# Antarmuka sistem
while True:
    print("\n=== Caffeshop ===")
    print("1. Lihat Menu")
    print("2. Tambah ke Pesanan")
    print("3. Lihat Pesanan")
    print("4. Tampilkan QR Code Saya")
    print("5. Keluar")
    
    choice = input("Pilih opsi (1-5): ")
    
    if choice == "1":
        show_menu()
    elif choice == "2":
        item = input("Masukkan nama item: ")
        try:
            quantity = int(input("Masukkan jumlah: "))
            add_to_order(order, item, quantity)
        except ValueError:
            print("⚠ Jumlah harus berupa angka.")
    elif choice == "3":
        view_order(order)
    elif choice == "4":
        try:
            image = Image.open('qrthoriq.png')
        except FileNotFoundError:
            print("⚠ File gambar tidak ditemukan. Pastikan file tersedia di jalur yang benar.")
            image = None

    elif choice == "5":
        print("Terima kasih telah mengunjungi caffeshop kami!")
        break