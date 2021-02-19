from flask import Flask, render_template, request, redirect, abort, flash, url_for, make_response, jsonify
from flask import Flask, render_template, request, jsonify
import trendyol_analiz
import os

app = Flask(__name__)
port = int(os.environ.get("PORT"), 5000)  # herokuya atma işleminde bu satır gerekiyormuş

@app.route('/') # anasayfa bu route ile oluşuyor sanırım. okey
def anasayfa():
    # return render_template("anasayfa.html")
    return render_template("anasayfa.html")

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


if __name__ == "__main__":
    # app.run(debug=True, port=2000)
    app.run(debug=True, host='0.0.0.0', port=port)
