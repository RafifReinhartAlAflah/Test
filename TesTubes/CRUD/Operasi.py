from . import Database
from .Util import random_string
import time

def update(no_buku,pk,data_add,tahun,judul,penulis):
    data = Database.TEMPLATE.copy() #salin data yang ada di file database, copy isi template
    
    data["pk"] = pk
    data["date_add"] = data_add
    data["penulis"] = penulis + Database.TEMPLATE["penulis"][len(penulis):] #menampilkan penulis di terminal
    data["judul"] = judul + Database.TEMPLATE["judul"][len(judul):] #menampilkan judul di terminal
    data["tahun"] = str(tahun) #menampilkan tahun di terminal
    
    data_str = f'{data["pk"]}, {data["date_add"]},{data["penulis"]},{data["judul"]},{data["tahun"]}\n'
    
    panjang_data = len(data_str)

    try:
        with (open(Database.DB_NAME,'r+', encoding="utf-8")) as file: #'r+' untuk nimpa file baru
            file.seek(panjang_data*(no_buku-1)) 
            file.write(data_str)    #nulis data barunya
    except:
        print("Error dalam update data")

def create(tahun,judul,penulis):
    data = Database.TEMPLATE.copy() #salin data yang ada di file database, copy isi template
    
    data["pk"] = random_string(6) #memanggil fungsi dari file Util.py 
    data["date_add"] = time.strftime("%Y-%m-%d-%H-%M-%S%z",time.gmtime()) #print tahun-bulan-tanggal-jam-menit-detik+gmt indonesia
    data["penulis"] = penulis + Database.TEMPLATE["penulis"][len(penulis):] #menampilkan penulis di terminal
    data["judul"] = judul + Database.TEMPLATE["judul"][len(judul):] #menampilkan judul di terminal
    data["tahun"] = str(tahun) #menampilkan tahun di terminal
    
    data_str = f'{data["pk"]}, {data["date_add"]},{data["penulis"]},{data["judul"]},{data["tahun"]}\n'
    try: 
        with open(Database.DB_NAME,'a', encoding="utf-8") as file: # 'a' buat nambah data baru
            file.write(data_str) #nulis data di txt
    except:
        print("Data sulit ditambahkan cuy, gagal maning")



def create_first_data():
    penulis = input("Penulis:")
    judul = input("Judul:")
    while True: #ngeloop terus sampai tahun hanya input integer
        try:
            tahun = int(input("Tahun\t: "))
            if len(str(tahun)) == 4:
                break
            else:
                print("Tahun harus 4 angka, silahkan masukkan tahun lagi (yyyy)")
        except:
            print("Tahun harus angka, silahkan masukkan tahun lagi (yyyy)")

    data = Database.TEMPLATE.copy() #salin data yang ada di file database, copy isi template
    
    data["pk"] = random_string(6) #memanggil fungsi dari file Util.py 
    data["date_add"] = time.strftime("%Y-%m-%d-%H-%M-%S%z",time.gmtime()) #print tahun-bulan-tanggal-jam-menit-detik+gmt indonesia
    data["penulis"] = penulis + Database.TEMPLATE["penulis"][len(penulis):] #menampilkan penulis di terminal
    data["judul"] = judul + Database.TEMPLATE["judul"][len(judul):] #menampilkan judul di terminal
    data["tahun"] = str(tahun) #menampilkan tahun di terminal

    data_str = f'{data["pk"]}, {data["date_add"]},{data["penulis"]},{data["judul"]},{data["tahun"]}\n'
    print(data_str)

    try: 
        with open(Database.DB_NAME,'w', encoding="utf-8") as file:
            file.write(data_str) #nulis data di txt
    except:
        print("udah lah gagal cuy")


def read(**kwargs):
    try:
        with open(Database.DB_NAME, 'r') as file:
            content = file.readlines()
            jumlah_buku = len(content)

            if "index" in kwargs:
                index_buku = kwargs["index"]-1 #isi dari data dengan index-1 (karena indexnya kita set mulai dari 1)
                if index_buku < 0 or index_buku> jumlah_buku:
                    return False
                else:
                    return (content[index_buku]) #print isi dari data 

            else: 
                return content
    except: 
        print("Membaca database error")
        return False

