import mysql.connector

import pandas

# Buat koneksi ke server MySQL

db_connection = mysql.connector.connect(

    host="localhost",

    user="root",

    password="",

    database="uas_bigdata_019"

)

# Buat objek cursor

db_cursor = db_connection.cursor()

 
# Contoh pernyataan SQL SELECT

select_query = "SELECT * FROM kesehatan"
 

# Eksekusi pernyataan SELECT

db_cursor.execute(select_query)

# Ambil hasil SELECT

results = db_cursor.fetchall()

# Tutup cursor dan koneksi

db_cursor.close()

db_connection.close()

 

# Konversi hasil SELECT menjadi dataframe pandas

df = pandas.DataFrame(results, columns=["ID", "Kode Provinsi", "Nama Provinsi", "Kode Kabupaten Kota", "Nama Kabupaten Kota", "Jenis", "Jumlah", "Satuan", "Tahun"])

 

# Simpan dataframe sebagai file Excel

df.to_csv("data_kesehatan.csv", index=False)

 

print("Data telah disimpan dalam file CSV 'data_kesehatan.csv'") #csv / xlsx

 