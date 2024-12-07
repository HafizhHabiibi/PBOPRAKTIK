import mysql.connector

conn = mysql.connector.connect(
    user = "root",
    host = "localhost",
    password = "",
    database = "perkuliahan"
)

cur = conn.cursor()

# membuat database
# cur.execute("CREATE DATABASE perkuliahan")

# membuat tabel dosen
# cur.execute("""CREATE TABLE Dosen (
#             Kode_Dos CHAR(4) NOT NULL PRIMARY KEY,
#             Nama_Dos VARCHAR(15),
#             Alamat_Dos VARCHAR(255),
#             No_Telp VARCHAR(15))""")

# # membuat tabel kuliah
# cur.execute("""CREATE TABLE Kuliah (
#             Kode_Mk CHAR(4) NOT NULL PRIMARY KEY,
#             Kode_Dos CHAR(4),
#             Waktu VARCHAR(25),
#             Tempat VARCHAR(15))""")

# # membuat tabel mata kuliah
# cur.execute("""CREATE TABLE Mata_Kuliah (
#             Kode_Mk CHAR(4) NOT NULL PRIMARY KEY,
#             Nama_Mk VARCHAR(255),
#             SKS INT(1),
#             Semester INT(2))""")


# menambahkan foreign key

# kode dosen
# cur.execute("""ALTER TABLE Kuliah
#             ADD FOREIGN KEY (Kode_Dos)
#             REFERENCES Dosen(Kode_Dos)""")

# kode mk 
# cur.execute("""ALTER TABLE Mata_Kuliah
#             ADD FOREIGN KEY (Kode_Mk)
#             REFERENCES Kuliah(Kode_Mk)
# """)

while True:
    print("1. Tampil Data")
    print("2. Input All")
    print("3. Input Data")
    print("4. Ubah")
    print("5. Hapus")
    print("6. Keluar")

    menu = int(input("Pilihan Menu : "))

    if menu == 1:
        cur.execute("""SELECT Nama_Dos, Waktu, Tempat, Nama_Mk, SKS, Semester FROM dosen INNER JOIN (kuliah INNER JOIN mata_kuliah 
                    ON kuliah.Kode_Mk = mata_kuliah.Kode_Mk) ON dosen.Kode_Dos = kuliah.Kode_Dos""")
        
        # SELECT Nama_Dos, Waktu, Tempat, Nama_Mk, SKS, Semester FROM dosen INNER JOIN (kuliah INNER JOIN mata_kuliah ON kuliah.Kode_Mk = mata_kuliah.Kode_Mk)
        # ON dosen.Kode_Dos = kuliah.Kode_Dos

        result = cur.fetchall()

        for row in result:
            print(row)

    # Input All
    elif menu == 2:

        # Input tabel dosen
        Kode_Dos = input("Masukan Kode Dosen : ")
        Nama_Dos = input("Masukan Nama Dosen : ")
        Alamat_Dos = input("Masukan Alamat Dosen : ")
        No_Telp = input("Masukan No Telepon Dosen : ")

        cur.execute("""INSERT INTO dosen VALUES(%s,%s,%s,%s)""", [Kode_Dos, Nama_Dos, Alamat_Dos, No_Telp])

        conn.commit()

        # Input tabel kuliah
        Kode_MK = input("Masukan Kode Mata Kuliah : ")
        Waktu = input("Masukan Waktu Kuliah : ")
        Tempat = input("Masukan Tempat Kuliah : ")

        cur.execute("""INSERT INTO kuliah VALUES(%s,%s,%s,%s)""", [Kode_MK, Kode_Dos, Waktu, Tempat])

        conn.commit()

        # Input tabel mata kuliah
        Nama_MK = input("Masukan Nama Mata Kuliah : ")
        Sks = int(input("Masukan SKS Mata Kuliah : "))
        Semester = input("Masukan Semester : ")

        cur.execute("""INSERT INTO mata_kuliah VALUES(%s,%s,%s,%s)""", [Kode_MK, Nama_MK, Sks, Semester])

        conn.commit()

    elif menu == 3:
        # Input mata kuliah
        Kode_Dos = input("Masukan Kode Dosen : ")
        Nama_MK = input("Masukan Nama Mata Kuliah : ")
        Sks = int(input("Masukan SKS Mata Kuliah : "))
        Semester = input("Masukan Semester : ")

        cur.execute("""INSERT INTO kuliah VALUES(%s,%s,%s,%s)""", [Kode_MK, Nama_MK, Sks, Semester])

        conn.commit()

    elif menu == 4:
        # update mata kuliah
        Kode_MK = input("Masukan Kode Mata Kuliah Yang Akan Diubah: ")
        Waktu = input("Masukan Waktu Baru : ")
        Tempat = input(f"Tempat Baru : ")

        cur.execute("""UPDATE kuliah SET Waktu = %s, Tempat = %s WHERE Kode_Mk = %s""", [Waktu, Tempat, Kode_MK])
        conn.commit()

    elif menu == 5:
        pass
        # # Hapus
        Kode_MK = input("Masukan Kode Mata Kuliah Yang Ingin Dihapus : ")
        cur.execute("""DELETE FROM mata_kuliah WHERE Kode_Mk = %s""", [Kode_MK])
        cur.execute("""DELETE FROM kuliah WHERE Kode_Mk = %s""", [Kode_MK])
        conn.commit()

    elif menu == 6:
        break


