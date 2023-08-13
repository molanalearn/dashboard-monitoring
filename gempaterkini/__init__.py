def ekstraksi_data():
    """
    Tanggal: 29 Juli 2023
    Waktu: 18:19:11 WIB
    Maginitudo: 5.0
    Kedalaman: 51 km
    Geo: LS=1.40 BT=128.31
    Pusat Gempa: Pusat gempa berada di laut 21 km BaratLaut Halmahera Timur
    Dirasakan: Dirasakan (Skala MMI): III Morotai Selatan, II-III Halmahera Timur, II Halmahera Utara
    :return:
    """
    hasil = dict()
    hasil['tanggal'] = '29 Juli 2023'
    hasil['waktu'] = '18:19:11 WIB'
    hasil['magnitudo'] = 5.0
    hasil['kedalaman'] = '51 km'
    hasil['geo'] = {'ls': 1.40,'bt': 128.31}
    hasil['pusat'] = 'Pusat gempa berada di laut 21 km BaratLaut Halmahera Timur'
    hasil['dirasakan'] = 'Dirasakan (Skala MMI): III Morotai Selatan, II-III Halmahera Timur, II Halmahera Utara'

    return hasil


def tampilkan_data(result):
    print('Gempa terakhir berdasarkan BMKG')
    print(f"Tanggal {result['tanggal']}")
    print(f"Waktu {result['waktu']}")
    print(f"Magnitudo {result['magnitudo']}")
    print(f"Kedalaman {result['kedalaman']}")
    print(f"Geo: LS={result['geo']['ls']}, BT={result['geo']['bt']}")
    print(f"Pusat Gempa: {result['pusat']}")
    print(f"Dirasakan: {result['dirasakan']}")