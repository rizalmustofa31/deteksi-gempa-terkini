"""
Aplikasi deteksi gempa terkini
"""


def ekstrasi_data():
    """
    Tanggal: 04 Februari 2022
    Waktu: 17:10:45 WIB
    Magnitudo: 5.5
    Kedalaman: 10 km
    Lokasi: LS=7.48 LS - BT=105.92 BT
    Pusat gempa: Pusat gempa berada di laut 71 Km Barat Daya Bayah
    Dirasakan: Dirasakan (Skala MMI): IV Pelabuhan Ratu, III Malingping, III Bayah, III Cihara, III Panggarangan
    :return:
    """
    hasil = dict()
    hasil['tanggal'] = '04 Februari 2022'
    hasil['waktu'] = '17:10:45 WIB'
    hasil['magnitudo'] = 5.5
    hasil['lokasi'] = {'ls': 7.48, 'bt': 105.92 }
    hasil['pusat'] = 'Pusat gempa berada di laut 71 Km Barat Daya Bayah'
    hasil['dirasakan'] = 'Dirasakan (Skala MMI): IV Pelabuhan Ratu, III Malingping, III Bayah, III Cihara, III Panggaran'

    return hasil


def tampilkan_data(result):
    print('Gempa terakhir berdasarkan BMKG')
    print(f"Tanggal {result['tanggal']}")
    print(f"Waktu {result['waktu']}")
    print(f"Magnitudo {result['magnitudo']}")
    print(f"Lokasi: LS={result['lokasi']['ls']}, BT={result['lokasi']['bt']}")
    print(f"Pusat {result['pusat']}")
    print(f"Dirasakan {result['dirasakan']}")


if __name__ == '__main__':
    print('Aplikasi utama')
    result = ekstrasi_data()
    tampilkan_data(result)