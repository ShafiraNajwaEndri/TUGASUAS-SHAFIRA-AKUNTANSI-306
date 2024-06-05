import pandas as pd
import matplotlib.pyplot as plt
from matplotlib_venn import venn2
import seaborn as sns

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

# Jawaban Pertanyaan 2
tanggal_cari = '2024-06-03'
karyawan_terlambat = absensi_df[(absensi_df['Tanggal'] == tanggal_cari) & (absensi_df['Jam Masuk'] > '08:00')]['Nama'].tolist()

# Jawaban Pertanyaan 3
tanggal_cari = '2024-06-01'
karyawan_sangat_baik = evaluasi_df[(evaluasi_df['Tanggal'] == tanggal_cari) & (evaluasi_df['Penilaian'] == 'Sangat Baik')]['Nama'].tolist()

# Visualisasi 1: Histogram
plt.figure(figsize=(8, 6))
sns.histplot(penjualan_df['Pendapatan'], bins=3, kde=True, color='skyblue')
plt.title('Histogram Pendapatan Penjualan')
plt.xlabel('Pendapatan')
plt.ylabel('Frekuensi')
plt.show()

# Visualisasi 2: Scatterplot
plt.figure(figsize=(8, 6))
plt.scatter(absensi_df['Jam Masuk'], absensi_df['Jam Pulang'], color='green')
plt.title('Scatterplot Jam Masuk vs Jam Pulang')
plt.xlabel('Jam Masuk')
plt.ylabel('Jam Pulang')
plt.show()

# Visualisasi 3: Diagram Venn
plt.figure(figsize=(8, 6))
venn2(subsets = (2, 2, 1), set_labels = ('Absensi Terlambat', 'Penilaian "Sangat Baik"'))
plt.title('Diagram Venn Karyawan Terlambat dan Penilaian "Sangat Baik"')
plt.show()

# Visualisasi 4: Pie Chart
plt.figure(figsize=(8, 6))
evaluasi_count = evaluasi_df['Penilaian'].value_counts()
plt.pie(evaluasi_count, labels=evaluasi_count.index, autopct='%1.1f%%', startangle=140, colors=['gold', 'lightcoral', 'lightskyblue'])
plt.title('Persentase Penilaian Karyawan')
plt.axis('equal')
plt.show()
