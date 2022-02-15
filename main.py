"""
Aplikasi deteksi gempa terkini
"""
import gempaterkini

if __name__ == '__main__':
    print('Aplikasi utama')
    result = gempaterkini.ekstrasi_data()
    gempaterkini.tampilkan_data(result)