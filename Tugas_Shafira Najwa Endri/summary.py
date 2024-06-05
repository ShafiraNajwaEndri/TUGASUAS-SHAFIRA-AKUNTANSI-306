import pandas as pd

# Data tabel penjualan
penjualan_data = {
    'Tanggal': ['2024-06-01', '2024-06-02', '2024-06-03'],
    'Barang': ['Kursi', 'Meja', 'Lemari'],
    'Jumlah Terjual': [20, 15, 10],
    'Pendapatan': [2000000, 3000000, 5000000]
}
penjualan_df = pd.DataFrame(penjualan_data)

# Data tabel absensi karyawan
absensi_data = {
    'Tanggal': ['2024-06-01', '2024-06-02', '2024-06-03'],
    'Nama': ['Andi', 'Budi', 'Cici'],
    'Jam Masuk': ['08:00', '08:30', '09:00'],
    'Jam Pulang': ['17:00', '18:00', '17:30']
}
absensi_df = pd.DataFrame(absensi_data)

# Data tabel evaluasi kinerja
evaluasi_data = {
    'Tanggal': ['2024-06-01', '2024-06-02', '2024-06-03'],
    'Nama': ['Andi', 'Budi', 'Cici'],
    'Penilaian': ['Baik', 'Cukup', 'Sangat Baik'],
    'Komentar': ['Pekerja keras', 'Perlu meningkatkan efisiensi', 'Selalu memberikan ide kreatif']
}
evaluasi_df = pd.DataFrame(evaluasi_data)

# Jawaban Pertanyaan 1
tanggal_cari = '2024-06-02'
total_pendapatan = penjualan_df[penjualan_df['Tanggal'] == tanggal_cari]['Pendapatan'].sum()
print("1. Total pendapatan pada tanggal", tanggal_cari, "adalah:", total_pendapatan)

# Jawaban Pertanyaan 2
tanggal_cari = '2024-06-03'
karyawan_terlambat = absensi_df[(absensi_df['Tanggal'] == tanggal_cari) & (absensi_df['Jam Masuk'] > '08:00')]['Nama'].tolist()
print("2. Karyawan yang datang terlambat pada tanggal", tanggal_cari, "adalah:", karyawan_terlambat)

# Jawaban Pertanyaan 3
tanggal_cari = '2024-06-01'
karyawan_sangat_baik = evaluasi_df[(evaluasi_df['Tanggal'] == tanggal_cari) & (evaluasi_df['Penilaian'] == 'Sangat Baik')]['Nama'].tolist()
if karyawan_sangat_baik:
    print("3. Karyawan yang mendapat penilaian 'Sangat Baik' pada tanggal", tanggal_cari, "adalah:", karyawan_sangat_baik)
else:
    print("3. Tidak ada karyawan yang mendapat penilaian 'Sangat Baik' pada tanggal", tanggal_cari)

