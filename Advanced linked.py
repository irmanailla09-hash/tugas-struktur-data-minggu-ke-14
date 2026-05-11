# ==========================================
# Aplikasi Note-Taking Sederhana
# ==========================================

from collections import deque

# ------------------------------------------
# Class Note
# ------------------------------------------
class Note:
    def __init__(self, title, content):
        self.title = title
        self.content = content
        self.tags = []

    def add_tag(self, tag):
        self.tags.append(tag)

    def __str__(self):
        return f"Judul: {self.title}\nIsi: {self.content}\nTags: {', '.join(self.tags)}"


# ------------------------------------------
# Penyimpanan Notes
# ------------------------------------------
notes = []

# Circular buffer untuk recent changes
recent_changes = deque(maxlen=5)


# ------------------------------------------
# Tambah Note
# ------------------------------------------
def tambah_note():
    title = input("Masukkan judul note: ")
    content = input("Masukkan isi note: ")

    note = Note(title, content)

    jumlah_tag = int(input("Jumlah tag: "))

    for i in range(jumlah_tag):
        tag = input(f"Tag ke-{i+1}: ")
        note.add_tag(tag)

    notes.append(note)

    recent_changes.append(f"Menambahkan note '{title}'")

    print("Note berhasil ditambahkan!\n")


# ------------------------------------------
# Tampilkan Berdasarkan Waktu
# ------------------------------------------
def tampil_chronological():
    print("\n=== NOTE CHRONOLOGICAL ===")

    for note in notes:
        print(note)
        print("-" * 30)


# ------------------------------------------
# Tampilkan Berdasarkan Abjad
# ------------------------------------------
def tampil_alphabetical():
    print("\n=== NOTE ALPHABETICAL ===")

    sorted_notes = sorted(notes, key=lambda x: x.title)

    for note in sorted_notes:
        print(note)
        print("-" * 30)


# ------------------------------------------
# Cari Berdasarkan Tag
# ------------------------------------------
def cari_tag():
    cari = input("Masukkan tag yang dicari: ")

    print(f"\n=== NOTE DENGAN TAG '{cari}' ===")

    ditemukan = False

    for note in notes:
        if cari in note.tags:
            print(note)
            print("-" * 30)
            ditemukan = True

    if not ditemukan:
        print("Tidak ada note dengan tag tersebut.")


# ------------------------------------------
# Recent Changes
# ------------------------------------------
def tampil_recent_changes():
    print("\n=== RECENT CHANGES ===")

    for perubahan in recent_changes:
        print(perubahan)


# ------------------------------------------
# Menu Program
# ------------------------------------------
while True:
    print("\n===== APLIKASI NOTE-TAKING =====")
    print("1. Tambah Note")
    print("2. Tampilkan Chronological")
    print("3. Tampilkan Alphabetical")
    print("4. Cari Berdasarkan Tag")
    print("5. Recent Changes")
    print("6. Keluar")

    pilihan = input("Pilih menu: ")

    if pilihan == "1":
        tambah_note()

    elif pilihan == "2":
        tampil_chronological()

    elif pilihan == "3":
        tampil_alphabetical()

    elif pilihan == "4":
        cari_tag()

    elif pilihan == "5":
        tampil_recent_changes()

    elif pilihan == "6":
        print("Program selesai.")
        break

    else:
        print("Pilihan tidak valid.")