tasks = []

try:
    with open("tasks.txt", "r") as file:
        for line in file:
            nama, status = line.strip().split("|")
            tasks.append({
                "nama": nama,
                "done": status == "True"
            })
except FileNotFoundError:
    pass


def simpan_task():
    with open("tasks.txt", "w") as file:
        for task in tasks:
            file.write(f"{task['nama']}|{task['done']}\n")


def tambah_task():
    nama = input("Masukkan task: ")
    tasks.append({
        "nama": nama,
        "done": False
    })
    simpan_task()
    print("Task berhasil ditambahkan")


def lihat_task():
    if len(tasks) == 0:
        print("Belum ada task")
    else:
        print("\nDaftar Task:")
        for i, task in enumerate(tasks, start=1):
            status = "✔" if task["done"] else " "
            print(f"{i}. [{status}] {task['nama']}")


def tandai_selesai():
    if len(tasks) == 0:
        print("Belum ada task")
        return

    lihat_task()

    try:
        nomor = int(input("Pilih nomor task yang selesai: "))
        if nomor <= 0 or nomor > len(tasks):
            print("Nomor tidak valid")
        else:
            tasks[nomor - 1]["done"] = True
            simpan_task()
            print("Task ditandai selesai")
    except ValueError:
        print("Masukkan angka yang valid")


def hapus_task():
    if len(tasks) == 0:
        print("Belum ada task")
        return

    lihat_task()

    try:
        nomor = int(input("Pilih nomor task yang ingin dihapus: "))
        if nomor <= 0 or nomor > len(tasks):
            print("Nomor tidak valid")
        else:
            tasks.pop(nomor - 1)
            simpan_task()
            print("Task berhasil dihapus")
    except ValueError:
        print("Masukkan angka yang valid")


while True:
    print("\n=== TASK MANAGER ===")
    print("1. Tambah Task")
    print("2. Lihat Task")
    print("3. Tandai Selesai")
    print("4. Hapus Task")
    print("5. Keluar")

    menu = input("Pilih menu: ")

    if menu == "1":
        tambah_task()

    elif menu == "2":
        lihat_task()

    elif menu == "3":
        tandai_selesai()

    elif menu == "4":
        hapus_task()

    elif menu == "5":
        print("Program selesai")
        break

    else:
        print("Menu tidak valid")