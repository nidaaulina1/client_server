import socket

# Inisialisasi socket client
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Hubungkan ke server
client_socket.connect(("127.0.0.1", 12345)),,

# Kirim pesan ke server
pesan = "Halo, ini pesan dari client."
client_socket.send(pesan.encode('utf-8'))

# Menerima balasan dari server
balasan = client_socket.recv(1024)
print(f"Balasan dari server: {balasan.decode('utf-8')}")

# Tutup koneksi dengan server
client_socket.close()