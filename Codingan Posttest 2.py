import os
os.system('cls')
import csv
from prettytable import from_csv

filename_csv = 'list_diamond.csv'

def utama():
    print(45 * "=")
    print("Selamat Datang di Myrfad Store, toko DM MLBB Termurah")
    print(" ---------------===0851-6300-1728===---------------  ")
    print(45 * "=")
    role = input("Anda disini sebagai apa? (Customer/Admin) = ")
    user = login(role)
    list_menu(role)
    while True:
        pilihan = input("Pilih Menu = ")
        if role == "Customer":
            if pilihan == "1":
                with open(filename_csv) as csv_file:
                    csv_reader = csv.reader(csv_file, delimiter=",")
                    print(csv_reader)
                    for code in csv_reader:
                        code = from_csv(csv_file)
                        print(code)
            elif pilihan == "2":
                username = input("Masukkan Username = ")
                id = input("Masukkan ID = ")
                server = input("Masukkan Server = ")
                code = input("Silahkan masukkan kode DM yang ingin dibeli> ")
                user.pembelian(username, id, server, code)
            elif pilihan == "3":
                print("Terima kasih telah mempercayai kami")
                break
            else:
                print("Input salah")
                utama()
        elif role == "Admin":
            if pilihan == "1":
                code = input("Masukkan Kode Baru = ")
                nominal = input("Masukkan Nominal Baru = ")
                harga = input("Masukkan Harga Baru = ")
                user.create(code, nominal, harga)
            elif pilihan == "2":
                user.read()
            elif pilihan == "3":
                update = []
                with open(filename_csv, mode="r") as csv_file:
                    csv_reader = csv.DictReader(csv_file)
                    for row in csv_reader:
                        update.append(row)
                    for data in update:
                            print("-----------------------")
                            code = input("Pilih Kode yang ingin diubah> ")
                            nominal= input("Nominal baru: ")
                            harga = input("Harga baru: ")
                            indeks = 0
                            for data in update:
                                if (data['Kode'] == code):
                                    update[indeks]['Nominal'] = nominal
                                    update[indeks]['Harga'] = harga
                                indeks = indeks + 1
                            with open(filename_csv, mode="w", newline='') as csv_file:
                                fieldnames = ['Kode','Nominal','Harga']
                                writer = csv.DictWriter(csv_file,fieldnames=fieldnames)
                                writer.writeheader()
                                for new_data in update:
                                    writer.writerow({'Kode': new_data['Kode'], 'Nominal': new_data['Nominal'], 'Harga': new_data['Harga']})
                            user.update(code, nominal, harga)
                            break
            elif pilihan == "4":
                delete = []
                with open(filename_csv, mode="r") as csv_file:
                    csv_reader = csv.DictReader(csv_file)
                    for row in csv_reader:
                        delete.append(row)
                    for data in delete:
                        print(f"{data['Kode']} \t {data['Nominal']} \t {data['Harga']}")
                    print("-----------------------")
                    no = input("Hapus Kode> ")
                    indeks = 0
                    for data in delete:
                        if (data['Kode'] == code):
                            delete.remove(delete[indeks])
                            indeks = indeks + 1
                        with open(filename_csv, mode="w", newline='') as csv_file:
                            fieldnames = ['Kode', 'Nominal', 'Harga']
                            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
                            writer.writeheader()
                            for new_data in delete:
                                writer.writerow({'Kode': new_data['Kode'], 'Nominal': new_data['Nominal'], 'Harga': new_data['Harga']})
                            user.delete(code,nominal,harga)
                            break
            elif pilihan == "5":
                print("Terima Kasih, MinKu")
                break
            else:
                print("Input salah")
                break
        else:
            print("Input salahh")
            break

def login(role):
    if role == "Customer":
        username = input("Masukkan Username = ")
        password = input("Masukkan Password = ")
        if username == "Customer" and password == "king":
            return customer(username, id, "server")
        else:
            print("Username atau Password salah")
            login(role)
    elif role == "Admin":
        admin_id = input("Masukkan ID Admin = ")
        admin_pw = input("Masukkan Password Admin = ")
        if admin_id == "Miku" and admin_pw == "dayooo":
            print("Selamat Datang, MinKu")
            return admin(admin_id, admin_pw)
        else:
            print("Username atau Password salah")
            login(role)
    else:
        print("Role Tidak Diketahui")
        utama()

def list_menu(role):
    if role == "Customer":
        print("-" * 45)
        print("1. List Harga")
        print("2. Pembelian")
        print("3. Keluar")
        print("-" * 45)
    elif role == "Admin":
        print("-" * 45)
        print("Admin Only")
        print("1. Create list baru")
        print("2. Read list")
        print("3. Update list")
        print("4. Delete list")
        print("5. Keluar")
        print("-" * 45)
    else:
        print("Role Tidak Diketahui")
        return None

class admin:
    def __init__(self, admin_id, admin_pw):
        self.admin_id = admin_id
        self.admin_pw = admin_pw
    
    def create(self, code, nominal, harga):
        self.code = code
        self.nominal = nominal
        self.harga = harga
        addon = [code, nominal, harga]
        with open(filename_csv, "r") as infile:
            reader = list(csv.reader(infile))
            reader.append(addon)

        with open(filename_csv, "w", newline='') as outfile:
            writer = csv.writer(outfile)
            for line in reader:
                writer.writerow(line)
        print(f"Anda telah berhasil menambah item dgn kode {code}")

    def read(self):
        with open(filename_csv) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=",")
            print(csv_reader)
            for code in csv_reader:
                code = from_csv(csv_file)
                print(code)

    def update(self, code, nominal, harga):
        self.code = code
        self.nominal = nominal
        self.harga = harga
        print(f"Anda telah berhasil mengubah data'{code}'")
        

    def delete(self, code, nominal, harga):
        self.code = code
        self.nominal = nominal
        self.harga = harga
        print(f"Anda telah menghapus item '{code}'")

class customer:
    def __init__(self, username, id, server):
        self.username = username
        self.id = id
        self.server = server
    
    def pembelian(self, username, id, server, code):
        self.username = username
        self.id = id
        self.server = server
        self.code = code
        print(f"Anda telah berhasil membeli DM dengan kode'{code}'")

utama()