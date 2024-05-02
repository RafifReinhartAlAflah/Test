from . import Operasi

def update_console():
    read_console() #membaca dengan menampilkan data
    while True:
        print("Silahkan pilih nomor buku yang akan di update")
        no_buku = int(input("Nomor Buku: "))
        data_buku = Operasi.read(index = no_buku) #dari file operasi dengan fungsi read dipanggilnya index dari inputan no_buku
        
        if data_buku: #jika ada datanya
            break 
        else:
            print("nomor tidak valid, silahkan masukan lagi")
    
    data_break = data_buku.split(",")
    pk = data_break[0]
    data_add = data_break[1]
    penulis = data_break[2]
    judul = data_break[3]
    tahun = data_break[4][:-1] #tambah [-1] karena ada enter dibelakangnya

    while True:
        #data yang ingin di update
        print("\n"+"="*100)
        print("Silahkan pilih data apa yang ingin anda ubah")
        print(f"1. Judul\t: {judul:.40}")
        print(f"2. Penulis\t: {penulis:.40}")
        print(f"3. Tahun\t: {tahun:4}")

        #memilih mode untuk update
        user_option = input("Pilih data [1,2,3] : ")

        match user_option:
            case "1" : judul = input("judul\t: ")
            case "2" : penulis = input("penulis\t: ")
            case "3" : 
                while True: #ngeloop terus sampai tahun hanya input integer
                    try:
                        tahun = int(input("Tahun\t: "))
                        if len(str(tahun)) == 4:
                            break
                        else:
                            print("Tahun harus 4 angka, silahkan masukkan tahun lagi (yyyy)")
                    except:
                        print("Tahun harus angka, silahkan masukkan tahun lagi (yyyy)")
            case _: print("index tidak cocokk")
        
        print("Data baru anda")
        print(f"1. Judul\t: {judul:.40}")
        print(f"2. Penulis\t: {penulis:.40}")
        print(f"3. Tahun\t: {tahun:4}")
        is_done = input("Apakah data sudah sesuai (y/n)?")

        if is_done == "y" or is_done == "Y":
            break
    
    Operasi.update(no_buku,pk,data_add,tahun,judul,penulis)


def create_console():
    print("\n\n"+"="*100)
    print("Silahkan tambah data buku\n")
    penulis = input("Penulis\t: ")
    judul = input("Judul\t: ")
    while True: #ngeloop terus sampai tahun hanya input integer
        try:
            tahun = int(input("Tahun\t: "))
            if len(str(tahun)) == 4:
                break
            else:
                print("Tahun harus 4 angka, silahkan masukkan tahun lagi (yyyy)")
        except:
            print("Tahun harus angka, silahkan masukkan tahun lagi (yyyy)")

    Operasi.create(tahun,judul,penulis) #di file operasi fungsi create kita panggil tahun judul penulis
    print("\nBerikut adalah data baru anda")
    read_console() #agar datanya tetep ada

def read_console():
    data_file = Operasi.read()

    index = "No"
    judul = "Judul"
    penulis = "Penulis"
    tahun = "Tahun"

    #Header
    print("\n"+"="*100)
    print(f'{index:4} | {judul:40} | {penulis:40}| {tahun:5}') # : sebagai lebar antar kalimat
    print("-"*100)

    #Data
    for index, data in enumerate(data_file):
        data_break = data.split(",") #akan split data yang berkoma (,)
        pk = data_break[0]
        date_add = data_break[1]
        penulis = data_break[2]
        judul = data_break[3]
        tahun = data_break[4]
        print(f'{index+1:4} | {judul:.40} | {penulis:.40}| {tahun:4}',end="") # : sebagai spasi antar kalimat


    #Footer
    print("="*100+"\n")