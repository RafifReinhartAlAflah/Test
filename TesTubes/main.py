import os
import CRUD as CRUD

if __name__ == "__main__":
    sistem_operasi = os.name

    match sistem_operasi :
        case "nt" : os.system("cls")

    print("SELAMAT DATANG DI STATISTIK")
    print("DATABASE STATISTIK")
    print("===========================")

    #cek
    CRUD.init_console()


    while True :
        match sistem_operasi :
            case "nt" : os.system("cls")

        print("SELAMAT DATANG DI STATISTIK")
        print("DATABASE STATISTIK")
        print("===========================")
        
        print(f"1. Data Statistik")
        print(f"2. Buat Data Baru ")

        user_option = input("Masukkan opsi:")
            
        print("\n===========================\n")

        match user_option :
            case "1" : print("Read Data")
            case "2" : print("Create Data")
            case "3" : print("Update Data")
            case "4" : print("Delete Data")

        print("\n===========================\n")
        is_done = input("Apakah sudah selesai (y/n)?")

        if is_done == "y" or is_done == "Y":
            break
    
    print("Program berakhir :)")
    