import requests
from bs4 import BeautifulSoup


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
    try:
        content = requests.get('https://www.bmkg.go.id/')
    except Exception:
        return None

    if content.status_code == 200:
        soup = BeautifulSoup(content.text, 'html.parser')

        result = soup.find('span', {'class': 'waktu'})
        result = result.text.split (', ')
        tanggal = result[0]
        waktu = result[1]

        result = soup.find('div', {'class': 'col-md-6 col-xs-6 gempabumi-detail no-padding'})
        result = result.findChildren('li')
        i = 0
        magnitudo = None
        kedalaman = None
        ls = None
        bt = None
        lokasi = None
        dirasakan = None


        for res in result:
            if i == 1:
                magnitudo = res.text
            elif i == 2:
                kedalaman = res.text
            elif i == 3:
                koordinat = res.text.split(' - ')
                ls = koordinat[0]
                bt = koordinat[1]
            elif i == 4:
                lokasi = res.text
            elif i == 5:
                dirasakan = res.text

            i = i + 1

        hasil = dict()
        hasil['tanggal'] = tanggal #'29 Juli 2023'
        hasil['waktu'] = waktu #'18:19:11 WIB'
        hasil['magnitudo'] = magnitudo #5.0
        hasil['kedalaman'] = kedalaman #'51 km'
        hasil['koordinat'] = {'ls': ls,'bt': bt}
        hasil['lokasi'] = lokasi #'Pusat gempa berada di laut 21 km BaratLaut Halmahera Timur'
        hasil['dirasakan'] = dirasakan #'Dirasakan (Skala MMI): III Morotai Selatan, II-III Halmahera Timur, II Halmahera Utara'
        return hasil
    else:
        return None


def tampilkan_data(result):
    if result is None:
        print('Tidak bisa menemukan data gempa terkini')
        return

    print('Gempa terakhir berdasarkan BMKG')
    print(f"Tanggal {result['tanggal']}")
    print(f"Waktu {result['waktu']}")
    print(f"Magnitudo {result['magnitudo']}")
    print(f"Kedalaman {result['kedalaman']}")
    print(f"Koordinat: LS={result['koordinat']['ls']}, BT={result['koordinat']['bt']}")
    print(f"Lokasi: {result['lokasi']}")
    print(f"Dirasakan: {result['dirasakan']}")