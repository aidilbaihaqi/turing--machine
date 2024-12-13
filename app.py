from flask import Flask, render_template, request

app = Flask(__name__)

def char_to_binary(char):
    """Fungsi untuk mengonversi karakter menjadi kode biner 8-bit."""
    return format(ord(char), '08b')

def turing_machine(word):
    """Mesin Turing untuk mengonversi kata menjadi kode biner dengan setiap huruf melalui satu state."""
    # Inisialisasi tape sebagai list dengan panjang sesuai input kata
    tape = list(word)
    head = 0  # Kepala baca/tulis
    state = 'q0'  # State awal
    result = []  # Menyimpan hasil konversi

    # State untuk setiap huruf dalam alfabet
    states = {
        'a': 'q_a', 'b': 'q_b', 'c': 'q_c', 'd': 'q_d', 'e': 'q_e', 'f': 'q_f',
        'g': 'q_g', 'h': 'q_h', 'i': 'q_i', 'j': 'q_j', 'k': 'q_k', 'l': 'q_l',
        'm': 'q_m', 'n': 'q_n', 'o': 'q_o', 'p': 'q_p', 'q': 'q_q', 'r': 'q_r',
        's': 'q_s', 't': 'q_t', 'u': 'q_u', 'v': 'q_v', 'w': 'q_w', 'x': 'q_x',
        'y': 'q_y', 'z': 'q_z'
    }

    # Mesin Turing memproses setiap huruf pada tape
    while head < len(tape):
        current_char = tape[head]

        # Cek apakah karakter valid (huruf kecil a-z)
        if current_char in states:
            # Pindah ke state sesuai dengan huruf
            state = states[current_char]

            # Konversi huruf ke biner dan simpan hasilnya
            binary = char_to_binary(current_char)
            result.append(f"{current_char} ({state}) -> {binary}")

            # Pindahkan kepala baca/tulis ke kanan
            head += 1
        else:
            # Jika ada karakter tidak valid, hentikan proses
            return "Input tidak valid. Hanya huruf kecil a-z yang diperbolehkan."

    # State akhir setelah semua huruf diproses
    state = 'accept'
    result.append(f"State akhir: {state}")
    return '\n'.join(result)

@app.route("/", methods=["GET", "POST"])
def index():
    output = None
    if request.method == "POST":
        word = request.form.get("word")
        output = turing_machine(word)
    return render_template("index.html", result=output)

if __name__ == "__main__":
    app.run(debug=True)
