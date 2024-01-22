import streamlit as st
import random
import os

# Takım isimlerini ve logolarını içeren klasör yolu
logo_klasoru = "/Users/cgunduz/PycharmProjects/ztk_draw/logolar"

liste1 = ["Fenerbahçe", "Galatasaray", "Beşiktaş", "Başakşehir",
          "Trabzonspor", "Karagümrük", "Konyaspor", "Ankaragücü"]
liste2 = ["Antalyaspor", "Sivasspor", "Gaziantep FK", "Hatayspor",
          "Samsunspor", "Bandırmaspor", "Gençlerbirliği", "24 Erzincanspor"]
takimlar = liste1 + liste2

# Streamlit uygulaması
st.title("Kura Çekimi Uygulaması")

# Eşleşmeleri kontrol etmek için bir session state oluştur
if "eslesmeler" not in st.session_state:
    st.session_state.eslesmeler = []
    st.session_state.cekilen_takimlar = []

while len(st.session_state.eslesmeler) < 8:
    cekilen_takim = random.choice(takimlar)

    # Daha önce çekilen takımları kontrol et
    if cekilen_takim in st.session_state.cekilen_takimlar:
        continue

    st.session_state.cekilen_takimlar.append(cekilen_takim)

    if cekilen_takim in liste1:
        liste1.remove(cekilen_takim)
        rakip = random.choice(liste2)
        liste2.remove(rakip)
        takimlar.remove(rakip)
    else:
        liste2.remove(cekilen_takim)
        rakip = random.choice(liste1)
        liste1.remove(rakip)
        takimlar.remove(rakip)

    st.session_state.eslesmeler.append((cekilen_takim, rakip))

# Button tıklama sayısını kontrol etmek için bir session state oluştur
if "i" not in st.session_state:
    st.session_state.i = 0

if st.button("Kura Çek") and st.session_state.i < 8:
    num_eslesme = st.session_state.i + 1  # 2. tıklamadan itibaren bir sonraki esleşmeyi ekleyerek devam et
    for j in range(num_eslesme):
        # Takım isimlerine eşleşen logoların yolu
        takim_logo_yolu_0 = os.path.join(logo_klasoru, st.session_state.eslesmeler[j][0] + ".png")
        takim_logo_yolu_1 = os.path.join(logo_klasoru, st.session_state.eslesmeler[j][1] + ".png")

        # Logoları ve "vs." metnini yan yana görüntüle
        col1, col2 = st.columns([1, 1])  # İlk ve üçüncü sütunlara daha fazla genişlik ver
        with col1:
            st.image(takim_logo_yolu_0, caption=st.session_state.eslesmeler[j][0], width=50)

        with col2:
            st.image(takim_logo_yolu_1, caption=st.session_state.eslesmeler[j][1], width=50)

        # Takım isimlerini sağ üst köşede görüntüle
        # st.write(f"**{st.session_state.eslesmeler[j][0]}** vs. **{st.session_state.eslesmeler[j][1]}**", key=f"match_{j}")

        # Takım isimleri arasında boşluk bırak
        st.write("\n")
        st.write("---")

    st.session_state.i += 1
elif st.session_state.i == 8:
    st.session_state.i = 0
