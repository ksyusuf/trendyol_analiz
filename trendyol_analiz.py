from bs4 import BeautifulSoup
import requests

class Siteler:
    def __init__(self, magazaSorgu, sorgu, urun_link_listesi):
        self.cikti = []
        self.magazaSorgu = magazaSorgu
        self.sorgu = sorgu
        self.urun_link_listesi = urun_link_listesi

        if magazaSorgu == "Trendyol":
            self.trendyol(sorgu, self.urun_link_listesi)
        elif magazaSorgu == "N11":
            self.n11(sorgu, self.urun_link_listesi)
        elif magazaSorgu == "Gittigidiyor":
            self.gittigidiyor(sorgu, self.urun_link_listesi)
        elif magazaSorgu == "":
            print("Magaza_sorgu boş")
        else:
            print("Farklı bir mağaza adı geldi!")

    def trendyol(self, sorgu, urun_linkler):
        print("fiyat çekiliyor...")
        if sorgu == "Ürün linki ile":
            for link in urun_linkler:
                try:
                    r = requests.get(link)
                    trendyolsite = BeautifulSoup(r.content, "html.parser")
                    fiyat = trendyolsite.find("div", attrs={"style": "display:flex"})
                    fiyat = fiyat.find("span", attrs={"class": "prc-dsc"})
                    print(fiyat.text)
                    self.cikti.append(fiyat.text)

                except requests.exceptions.MissingSchema:
                    print("hatalı link @@@@@")
        print("fiyat çekildi.")
        print(self.cikti)
        return self.cikti

    def n11(self, sorgu, urun_linkler):
        print("n11 fonksiyonu oluşturulmamış")

    def gittigidiyor(self, sorgu, urun_linkler):
        print("gittigidiyor fonksiyonu oluşturulmamış")


liste = ["https://www.trendyol.com/trend-alacati-stili/kadin-grimelanj-pacasi-lastikli-iki-iplik-esofman-alti-alc-y2933-p-32241574?boutiqueId=553411&merchantId=4484"]
site=Siteler("Trendyol","1",liste)
