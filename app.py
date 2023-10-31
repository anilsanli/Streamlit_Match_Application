"""
import streamlit as st
import random

# Gruplara ait listeleri tanımlayın
ceza_grubu = []
odul_grubu = []

# Kullanıcıdan gruplara isim eklemesini isteyin
st.title("Eşleşme Sistemi")
st.write("Ceza ve Ödül gruplarına isimler ekleyin. İsimleri virgülle ayırın.")

# Kullanıcıdan isimleri girmesini isteyin
ceza_input = st.text_input("Ceza Grubu İsimleri")
odul_input = st.text_input("Ödül Grubu İsimleri")

# Kaydet butonunu oluşturun
if st.button("Kaydet"):
    ceza_grubu.extend([isim.strip() for isim in ceza_input.split(",") if isim.strip() != ""])
    odul_grubu.extend([isim.strip() for isim in odul_input.split(",") if isim.strip() != ""])
    st.success("İsimler başarıyla kaydedildi.")

st.write(f"Ceza Grubu: {ceza_grubu}")
st.write(f"Ödül Grubu: {odul_grubu}")

# Eşleşme yapma fonksiyonunu tanımlayın
def eslesme_yap(ceza_grubu, odul_grubu):
    random.shuffle(ceza_grubu)
    random.shuffle(odul_grubu)
    eslesmeler = []

    for i in range(min(len(ceza_grubu), len(odul_grubu))):
        ceza_uye = ceza_grubu[i]
        odul_uye = odul_grubu[i]
        eslesmeler.append(f"{ceza_uye} - {odul_uye}")

    if len(ceza_grubu) > len(odul_grubu):
        for i in range(len(odul_grubu), len(ceza_grubu)):
            ceza_uye = ceza_grubu[i]
            odul_uye = random.choice(odul_grubu)
            eslesmeler.append(f"{ceza_uye} - {odul_uye}")

    return eslesmeler

# Eşleşme butonunu oluşturun
if st.button("Eşleşmeleri Oluştur"):
    if len(ceza_grubu) == 0 or len(odul_grubu) == 0:
        st.warning("Her iki grupta da en az bir isim eklediğinizden emin olun.")
    else:
        eslesme_listesi = eslesme_yap(ceza_grubu, odul_grubu)
        st.subheader("Eşleşmeler")
        for eslesme in eslesme_listesi:
            st.write(eslesme)
"""
import streamlit as st
import random
import pandas as pd
import numpy as np

# Gruplara ait listeleri tanımlayın
ceza_grubu = []
odul_grubu = []

# Kullanıcıdan gruplara isim eklemesini isteyin
st.title("Eşleşme Sistemi")
st.write("Ceza ve Ödül gruplarına isimler ekleyin. İsimleri virgülle ayırın.")

# Kullanıcıdan isimleri girmesini isteyin
ceza_input = st.text_input("Ceza Grubu İsimleri")
odul_input = st.text_input("Ödül Grubu İsimleri")

# Kaydet ve Eşleşme yap butonunu oluşturun
if st.button("Kaydet ve Eşleşme Yap"):
    ceza_grubu.extend([isim.strip() for isim in ceza_input.split(",") if isim.strip() != ""])
    odul_grubu.extend([isim.strip() for isim in odul_input.split(",") if isim.strip() != ""])

    st.success("İsimler başarıyla kaydedildi.")

    st.write(f"Ceza Grubu: {ceza_grubu}")
    st.write(f"Ödül Grubu: {odul_grubu}")

    if len(ceza_grubu) == 0 or len(odul_grubu) == 0:
        st.warning("Her iki grupta da en az bir isim eklediğinizden emin olun.")
    else:
        random.shuffle(ceza_grubu)
        random.shuffle(odul_grubu)
        eslesmeler = []

        for i in range(min(len(ceza_grubu), len(odul_grubu))):
            ceza_uye = ceza_grubu[i]
            odul_uye = odul_grubu[i]
            eslesmeler.append(f"{ceza_uye} - {odul_uye}")

        if len(ceza_grubu) > len(odul_grubu):
            for i in range(len(odul_grubu), len(ceza_grubu)):
                ceza_uye = ceza_grubu[i]
                odul_uye = random.choice(odul_grubu)
                eslesmeler.append(f"{ceza_uye} - {odul_uye}")

        st.subheader("Eşleşmeler")
        for eslesme in eslesmeler:
            st.write(eslesme)