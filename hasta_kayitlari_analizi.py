# %%
import pandas as pd

df = pd.read_csv(r'C:\Users\yagmu\OneDrive\Belgeler\python dosyalar\py_ders\veriler\ödev 2\hasta_kayitlari.csv')

# %% [markdown]
# ### Bölüm 1: Veriyi Tanımak

# %%
df.head(8)

# %%
df.tail(4)

# %%
df.info()

# %% [markdown]
# bmi, sistolik ve maliyet_tl verilerinde sırasıyla 48, 15 ve 22 veri eksik.

# %%
df.rename(columns={"maliyet_tl":"maliyet"},inplace=True)
df.rename(columns={"yatis_gun":"yatis_suresi"},inplace=True)
df.head(3)

# %% [markdown]
# ### Bölüm 2: Veri Temizleme

# %%
print("Tekrar eden veriler silinmeden önce uzunluk: ", len(df))
df.duplicated().sum()

# %%
df=df.drop_duplicates()
print("Tekrar eden veriler silindikten sonra uzunluk: ", len(df))

# %% [markdown]
# Sütunlardaki eksik veri miktarlarını listeleyelim

# %%
print(df.isna().sum())

# %% [markdown]
# bmi, sistolik ve maliyet_tl verilerinde sırasıyla 48, 15 ve 22 veri eksik.

# %%
df['bmi'] = df['bmi'].fillna(df['bmi'].median())
print(df.isna().sum())

# %%
df['sistolik_kb'] = df['sistolik_kb'].fillna(df['sistolik_kb'].median())
print(df.isna().sum())

# %%
df = df.dropna(subset=['maliyet'])
print(df.isna().sum())

# %%
len(df)

# %% [markdown]
# ### Bölüm 3: Filtreleme ve Yeni Sütun Oluşturma

# %%
df[(df.sehir=="İstanbul") & (df.yas>50)]

# %% [markdown]
# İstanbul'da yaşayan ve yaşı 50'den büyük 124 kişi vardır

# %%
sigortasiz_yatis = df[(df.sigorta=="Yok") & (df.yatis_suresi>7)]
sigortasiz_yatis['maliyet'].mean()

# %% [markdown]
# Sigortası olmayan ve 7 günden fazla yatış yapan hastaların ortalama maliyeti 21769.53

# %%
df['gunluk_maliyet'] = df['maliyet'] / df['yatis_suresi']
df['yas_grubu'] = [
    'genç' if 18 < i <= 35 
    else 'orta yaşlı' if 35 < i < 60 
    else 'yaşlı'
    for i in df['yas']
]
df.head(3)

# %%
df[df['bolum'] == 'Kardiyoloji'].sort_values('maliyet', ascending=False).head(10)

# %% [markdown]
# Kardiyoloji bölümünde en çok maliyete sahip hastalarından ilk 10 kişiyi seçtiğimizde büyük çoğunluğu sigortalıdır (8 sigortalı, 2 sigortasız). Sigortalıların çoğu da SGK'lıdır.

# %% [markdown]
# ### Bölüm 4: Özet İstatistikleri 

# %%
df.describe().T

# %%
df['sehir'].value_counts()

# %%
df['sehir'].value_counts(normalize=True)

# %% [markdown]
# Hasta yoğunluğu olarak en kalabalık 3 şehir sırasıyla İstanbul, Ankara ve İzmir'dir. 
# Bu şehirlerin diğer şehirlere kıyasla yoğunluk oranı sırasıyla %28.9, %16.8 ve %15.4 dür.

# %%
df['bolum'].value_counts()

# %%
df['bolum'].value_counts(normalize=True)

# %% [markdown]
# Bölümlerin hasta yoğunlukları birbirlerine yakın olmakla birlikte en yoğun iki bölüm sırasıyla Kardiyoloji ve Dahiliye bölümleridir. Bu bölümlerin hasta sayısının toplama oranı sırasıyla %18.0 ve %17.5'dir.

# %%
df.groupby("bolum")[["yas", "yatis_suresi", "maliyet"]].agg(["mean", "max", "count", "sum"]).round(2).T

# %% [markdown]
# Her bölüm için ortalama ve maksimum maliyet yatış süresi ve yaş bulunmuştur.

# %%
df.groupby("yas_grubu")[["bmi"]].mean().round(2)

# %% [markdown]
# Yaş ile BMI arasında doğrusal korelasyon gözlenmiştir. Yaş arttıkça ortalama BMI artmaktadır

# %%
df.groupby("sigorta")[["yatis_suresi", "maliyet"]].mean().round(2).T

# %% [markdown]
# Sigortasıs hastaların maliyeti sigortalılara kıyasla daha fazladır.

# %%
df[df["sigorta"] == "Yok"].groupby("bolum").size().sort_values(ascending=False)

# %% [markdown]
# En çok sigortasız hasta Kardiyoloji bölümünde bulunmaktadır.


