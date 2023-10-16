import socket

# Inisialisasi socket server
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind socket ke alamat dan port tertentu
server_socket.bind(("127.0.0.1", 12345))

# Mendengarkan koneksi yang masuk (maksimum 5 koneksi dalam antrian)
server_socket.listen(5)
print("Server sedang mendengarkan...")

while True:
    # Menerima koneksi dari client
    client_socket, client_address = server_socket.accept()
    print(f"Koneksi dari {client_address}")

    # Menerima pesan dari client
    data = client_socket.recv(1024)
    print(f"Pesan dari client: {data.decode('utf-8')}")

    # Mengirim balasan ke client
    response = "Pesan diterima oleh server."
    client_socket.send(response.encode('utf-8'))

    # Tutup koneksi dengan client
    client_socket.close()