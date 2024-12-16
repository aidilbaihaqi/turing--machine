from flask import Flask, render_template, request

app = Flask(__name__)

def char_to_binary(char):
    """Fungsi untuk mengonversi karakter menjadi kode biner 8-bit."""
    ascii_value = ord(char)
    binary = []
    while ascii_value > 0:
        binary.append(str(ascii_value % 2))
        ascii_value //= 2

    # Pad dengan nol hingga panjang 8-bit
    while len(binary) < 8:
        binary.append('0')

    # Balikkan urutan biner untuk mendapatkan hasil akhir
    return ''.join(reversed(binary))

def turing_machine(word):
    """Mesin Turing untuk mengonversi kata menjadi kode biner dengan setiap huruf melalui satu state."""
    tape = list(word)  # Tape input
    head = 0  # Kepala baca/tulis
    state = 'q0'  # State awal
    final_state = 'accept'  # Final state
    result = ["Hasil Proses Mesin Turing"]  # Menyimpan langkah-langkah proses mesin

    # Daftar state untuk setiap karakter
    states = {
        'a': 'q_a', 'b': 'q_b', 'c': 'q_c', 'd': 'q_d', 'e': 'q_e', 'f': 'q_f',
        'g': 'q_g', 'h': 'q_h', 'i': 'q_i', 'j': 'q_j', 'k': 'q_k', 'l': 'q_l',
        'm': 'q_m', 'n': 'q_n', 'o': 'q_o', 'p': 'q_p', 'q': 'q_q', 'r': 'q_r',
        's': 'q_s', 't': 'q_t', 'u': 'q_u', 'v': 'q_v', 'w': 'q_w', 'x': 'q_x',
        'y': 'q_y', 'z': 'q_z'
    }

    # Mesin memproses setiap simbol pada tape
    while state != final_state:
        current_char = tape[head]  # Simbol di posisi head

        # Jika membaca simbol akhir `;`, pindah ke final state
        if current_char == ';':
            result.append(f"------------\nTape: {''.join(tape)}\nhead: {current_char}\ncurrent state: {state}\nnext state: {final_state}\nwrite: (empty)\nmove: stay\n------------")
            state = final_state
            break

        # Cek apakah karakter valid (huruf kecil a-z)
        if current_char in states:
            # Simpan informasi state saat ini
            current_state = state
            next_state = states[current_char]

            # Konversi huruf ke biner
            binary = char_to_binary(current_char)

            # Simpan informasi langkah ke result sebelum tape diperbarui
            result.append(f"------------\nTape: {''.join(tape)}\nhead: {current_char}\ncurrent state: {current_state}\nnext state: {next_state}\nwrite: {binary}\nmove: right\n------------")

            # Perbarui tape dengan mengganti huruf asli dengan biner
            tape = (
                tape[:head] + 
                list(binary) + 
                tape[head + 1:]
            )

            # Pindahkan head ke posisi setelah biner
            head += len(binary)
            state = next_state
        else:
            # Jika ada simbol tidak valid
            return "Input tidak valid. Karakter tidak valid ditemukan di tape."

    # Tambahkan output akhir setelah semua langkah selesai
    result.append(f"output : {''.join(tape[:-1])}")  # Hapus simbol `;` dari output
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
