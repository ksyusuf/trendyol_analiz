### klasik olarak route lar ayrı bi dosyaya koyuluyormuş flask çalışmalarında

from MARKETLER import app
from flask import Flask, render_template, request, jsonify
import trendyol_analiz


@app.route('/') # anasayfa bu route ile oluşuyor sanırım. okey
def anasayfa():
    return render_template('index.html', title="Anasayfa")

@app.route("/veri-kazima-sayfasi", methods=['POST', 'GET'])
def form():
    return render_template('veri_kazima_girisi.html')

@app.route('/veri_kazima_islemi', methods=['POST'])
def say_name():
    print("giriş geldi")
    gelen_veri = request.get_json()
    linkler_listesi = gelen_veri["linkler_listesi"]
    magaza_adi = gelen_veri["magaza_adi"]
    arama_tipi = gelen_veri["arama_tipi"]
    print(gelen_veri)
    print(magaza_adi+"@@@"+arama_tipi)

    if ( magaza_adi == "" or arama_tipi == "" ):
        print("mağaza sorgu veya arama tipi boş")
        return jsonify(hata_durumu="var")
    else:
        fiyat_listesi = (trendyol_analiz.Siteler(magaza_adi, arama_tipi, linkler_listesi)).cikti
        print(fiyat_listesi)
        return jsonify(fiyat_listesi=fiyat_listesi, hata_durumu="yok")