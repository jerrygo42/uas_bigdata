# Buat koneksi ke server MySQL
import mysql.connector
db_connection = mysql.connector.connect(

    host="localhost",

    user="root",

    password="",

    database="uas_bigdata_019"  # Ganti dengan nama database yang telah Anda buat

)

 

# Buat objek cursor

db_cursor = db_connection.cursor()

 

# Definisikan struktur tabel 'mahasiswa'

create_table_query = """

CREATE TABLE kesehatan (

    id INT AUTO_INCREMENT PRIMARY KEY,
    kode_provinsi VARCHAR(255),
    nama_provinsi VARCHAR(255),
    kode_kabupaten_kota VARCHAR(255),
    nama_kabupaten_kota VARCHAR(255),
    jenis VARCHAR(255),
    jumlah VARCHAR(255),
    satuan VARCHAR(255),
    tahun VARCHAR(255)

)

"""

 

# Eksekusi perintah SQL untuk membuat tabel

db_cursor.execute(create_table_query)

 

# Komit perubahan ke database

db_connection.commit()

 

# Tutup cursor dan koneksi

db_cursor.close()

db_connection.close()