import json
import os

FILE_NAME = "tasks.json"

# Load data dari file
def load_tasks():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    return []

# Simpan data ke file
def save_tasks(tasks):
    with open(FILE_NAME, "w") as file:
        json.dump(tasks, file, indent=4)

def show_menu():
    print("\n=== TO DO LIST ===")
    print("1. Tambah tugas")
    print("2. Lihat tugas")
    print("3. Hapus tugas")
    print("4. Keluar")

tasks = load_tasks()

while True:
    show_menu()
    choice = input("Pilih menu (1-4): ")

    if choice == "1":
        task = input("Masukkan tugas: ")
        tasks.append(task)
        save_tasks(tasks)
        print("Tugas ditambahkan & disimpan!")

    elif choice == "2":
        if not tasks:
            print("Belum ada tugas.")
        else:
            print("\nDaftar Tugas:")
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task}")

    elif choice == "3":
        if not tasks:
            print("Tidak ada tugas.")
        else:
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task}")
            num = int(input("Pilih nomor tugas: "))
            tasks.pop(num - 1)
            save_tasks(tasks)
            print("Tugas dihapus & disimpan!")

    elif choice == "4":
        print("Sampai jumpa 👋")
        break

    else:
        print("Pilihan tidak valid!")
