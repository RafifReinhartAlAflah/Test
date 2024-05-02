import os
import CRUD as CRUD

if __name__ == "__main__":
    sistem_operasi = os.name

    match sistem_operasi :
        case "posix" : os.system("clear") #untuk macos
        case "nt" : os.system("cls") #untuk windows

    print("SELAMAT DATANG DI STATISTIK")
    print("DATABASE STATISTIK")
    print("===========================")

    # cek
    CRUD.init_console()


    while True :
        match sistem_operasi :
            case "nt" : os.system("cls")

        print("SELAMAT DATANG DI STATISTIK")
        print("DATABASE STATISTIK")
        print("===========================")
        
        print(f"1. Read Data")
        print(f"2. Create Data ")
        print(f"3. Update Data ")
        print(f"4. Delete Data ")

        user_option = input("Masukkan opsi:")
            
        match user_option :
            case "1" : CRUD.read_console()
            case "2" : CRUD.create_console()
            case "3" : CRUD.update_console()
            case "4" : print("Delete Data")

        is_done = input("Apakah sudah selesai (y/n)?")

        if is_done == "y" or is_done == "Y":
            break
    
    print("Program berakhir :)")

    
    