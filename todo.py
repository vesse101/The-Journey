tasks = []

def show_menu():
    print("\n=== TO DO LIST ===")
    print("1. Tambah tugas")
    print("2. Lihat tugas")
    print("3. Hapus tugas")
    print("4. Keluar")

while True:
    show_menu()
    choice = input("Pilih menu (1-4): ")

    if choice == "1":
        task = input("Masukkan tugas: ")
        tasks.append(task)
        print("Tugas ditambahkan!")

    elif choice == "2":
        if not tasks:
            print("Belum ada tugas.")
        else:
            print("\nDaftar Tugas:")
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task}")

    elif choice == "3":
        if not tasks:
            print("Tidak ada tugas untuk dihapus.")
        else:
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task}")
            num = int(input("Pilih nomor tugas: "))
            tasks.pop(num - 1)
            print("Tugas dihapus!")

    elif choice == "4":
        print("Keluar dari program.")
        break

    else:
        print("Pilihan tidak valid!")
