class Mahasiswa:
    def __init__(self, identification_number, full_name, year_of_admission, is_active=True):
        self._nim = identification_number
        self._nama = full_name
        self.angkatan = year_of_admission
        self.is_active = is_active

    # Setter dan getter untuk identification_number
    def set_identification_number(self, identification_number):
        self._nim = identification_number

    def get_identification_number(self):
        return self._nim

    # Setter dan getter untuk full_name
    def set_full_name(self, full_name):
        self._nama = full_name

    def get_full_name(self):
        return self._nama

    # Method untuk mengecek apakah mahasiswa aktif
    def is_active_student(self):
        return self.is_active

    # Method untuk mengembalikan informasi mahasiswa
    def student_info(self):
        status = "aktif" if self.is_active_student() else "tidak aktif"
        return f"Informasi Mahasiswa:\nNama: {self.get_full_name()}, NIM: {self.get_identification_number()}, Angkatan: {self.angkatan}, Status: {status}"

    # Method untuk mengecek apakah mahasiswa lulus berdasarkan tahun lulus
    def is_graduated(self, year_of_graduation):
        return year_of_graduation - self.angkatan >= 4

# Inisiasi objek pertama
mahasiswa1 = Mahasiswa("12214192", "Novia Listiani", 2022)

# Inisiasi objek kedua tanpa menyertakan parameter is_active
mahasiswa2 = Mahasiswa("125140007", "Mary Jane", 2019)

# Memanggil method untuk menampilkan informasi mahasiswa
print(mahasiswa1.student_info())
print(mahasiswa2.student_info())

# Memanggil method untuk mengecek apakah mahasiswa lulus
print("Status Kelulusan Mahasiswa:")
print(f"Novia Listiani: {'Belum lulus' if not mahasiswa1.is_graduated(2023) else 'Sudah lulus'}")
print(f"Mary Jane: {'Belum lulus' if not mahasiswa2.is_graduated(2023) else 'Sudah lulus'}")
