# -*- coding: utf-8 -*-
"""Submission 1 - Predictive Analytics- Air Quality

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1hu4NbuWx4m__hNjkhRyF3yphTXsyUnxZ

# **Laporan Proyek Machine Learning - Saif Rayhan Naufal**

# **Domain Proyek**

**Polutan Penyebab Pemanasan Global**

Pemanasan global dan pencemaran udara telah menjadi isu mendesak yang memengaruhi berbagai aspek kehidupan manusia. Peningkatan suhu bumi akibat emisi gas rumah kaca dari aktivitas manusia, seperti transportasi, pembakaran bahan bakar fosil, dan industri, telah memperburuk kualitas udara, terutama di kawasan perkotaan. Polutan seperti karbon monoksida (CO), benzena (C6H6), nitrogen oksida (NOx), dan ozon (O3) berdampak serius pada kesehatan manusia dan ekosistem. Data dari Organisasi Kesehatan Dunia (WHO) menunjukkan bahwa 91% populasi dunia tinggal di wilayah dengan kualitas udara buruk, yang menyebabkan sekitar 7 juta kematian  setiap tahun akibat penyakit terkait polusi udara ([Billions of People Still Breathe Unhealthy Air](https://www.who.int/news/item/04-04-2022-billions-of-people-still-breathe-unhealthy-air-new-who-data)). Kondisi ini menandakan pentingnya langkah untuk mengidentifikasi, memantau, dan mengurangi pencemaran udara agar menciptakan lingkungan yang lebih sehat dan berkelanjutan.

Pemanfaatan teknologi dan data akurat menjadi kunci dalam memahami pola pencemaran dan menganalisis tren jangka panjang. Dengan data berkualitas, para peneliti dan pembuat kebijakan dapat mengambil keputusan berbasis bukti ilmiah untuk mengurangi dampak buruk polusi udara. Selain itu, pengembangan model prediktif menggunakan machine learning dan metode pengolahan data yang baik dapat memberikan solusi yang lebih terarah dalam upaya mitigasi. Langkah ini tidak hanya membantu meningkatkan kualitas penelitian lingkungan, tetapi juga memperkuat fondasi pengambilan keputusan strategis di tingkat lokal dan global.

# **Business Understanding**

## **Problem Statement**

1.   Bagaimana interaksi antara karbon monoksida (CO) dengan senyawa kimia, seperti nitrogen oksida (NOx), ozon (O3), dan polutan lainnya yang dapat mempengaruhi kualitas udara?
2.   Apa saja faktor-faktor yang mempengaruhi peningkatan suhu sehingga dapat memperburuk kualitas udara?

## **Goals**

1.   Untuk memahami bagaimana interaksi antara CO dan senyawa polutan lainnya mempengaruhi konsentrasi dan dampak polusi udara, sehingga diharapkan dapat mengurangi aktivitas yang dapat menghasilkan senyawa-senyawa tersebut
2.  Untuk mengidentifikasi dan menganalisis faktor-faktor yang mempengaruhi peningkatan suhu serta dampaknya terhadap kualitas udara, sehingga memberikan informasi yang dapat digunakan dalam perencanaan kebijakan lingkungan dan pengendalian polusi.

## **Solution Statements**

1.   Untuk memahami interaksi antara karbon monoksida (CO) dengan senyawa lainnya, visualisasi data seperti heatmaps dan pair plots akan digunakan untuk menggambarkan korelasi antar fitur. Dengan visualisasi ini, hubungan antara polutan dan faktor lingkungan lainnya dapat dengan jelas diindentifikasi serta membantu dalam mendeteksi pola-pola tersembunyi yang mungkin mempengaruhi kualitas udara. Teknik visualisasi ini akan memberikan gambaran tentang interaksi antar variabel dan bagaimana masing-masing polutan berkontribusi terhadap perubahan kualitas udara.

2.   Untuk mengevaluasi faktor-faktor yang mempengaruhi peningkatan suhu, metrik MSE akan digunakan dalam model regresi. MSE akan memberikan gambaran yang jelas tentang seberapa akurat prediksi suhu berdasarkan beberapa faktor. Dengan mengukur kesalahan prediksi, dapat diketahui faktor-faktor mana yang paling berpengaruh terhadap perubahan suhu dan mampu membantu memperbaiki model untuk meningkatkan akurasi dan memberikan solusi yang lebih efektif dalam mitigasi suhu dan polusi udara.

# **Data Understanding**

Dataset yang digunakan dalam proyek ini bersumber dari Kaggle dan berfokus pada pemantauan kualitas udara di kawasan perkotaan. Dataset ini terdiri dari 15 kolom yang berisi data hasil pengukuran dari berbagai sensor kimia, yang mengukur konsentrasi polutan udara seperti karbon monoksida (CO), nitrogen oksida (NOx), ozon (O3), dan polutan lainnya. Data dikumpulkan dari perangkat sensor yang ditempatkan di lokasi perkotaan di Italia, dengan periode pengukuran yang mencakup satu tahun, mulai dari Maret 2004 hingga Februari 2005. Dataset ini memberikan informasi penting mengenai respons sensor terhadap konsentrasi polutan, serta variabel lingkungan lainnya seperti suhu dan kelembaban. Dataset ini berisi 9357 data hasil pengukuran per jam dari lima sensor logam oksida kimia yang tertanam dalam perangkat Air Quality Chemical Multisensor Device, yang terletak di area dengan polusi tinggi di sebuah kota Italia. Data yang terekam mencakup konsentrasi rata-rata per jam untuk CO, Hidrokarbon Non-Metanik, Benzena, Nitrogen Oksida (NOx), dan Nitrogen Dioksida (NO2), yang disediakan oleh analyzer referensi bersertifikat. Nilai yang hilang pada dataset ini ditandai dengan nilai -200. Dataset ini dapat diunduh dari Kaggle melalui informasi berikut:

---

**Judul**   : [Air-Quality](https://www.kaggle.com/datasets/citrahsagala/airquality)

**Pemilik** : [citrahsagala](https://www.kaggle.com/citrahsagala)

**Sumber**  : Kaggle

---

**Deskripsi Data**

1. **Date**: Tanggal pengukuran dalam format DD/MM/YYYY.
2. **Time**: Waktu pengukuran dalam format HH.MM.SS.
3. **CO(GT)**: Konsentrasi karbon monoksida (CO) yang diukur oleh alat referensi dalam satuan mg/m³ (True hourly averaged concentration CO).
4. **PT08.S1(CO)**: Respons sensor tin oksida (PT08.S1) yang menargetkan karbon monoksida (CO), dengan satuan relatif (sensor response).
5. **NMHC(GT)**: Konsentrasi hidrokarbon non-metanik (NMHC) yang diukur oleh alat referensi dalam satuan µg/m³ (True hourly averaged concentration).
6. **C6H6(GT)**: Konsentrasi benzena (C6H6) yang diukur oleh alat referensi dalam satuan µg/m³ (True hourly averaged concentration).
7. **PT08.S2(NMHC)**: Respons sensor titania (PT08.S2) yang menargetkan hidrokarbon non-metanik (NMHC), dengan satuan relatif (sensor response).
8. **NOx(GT)**: Konsentrasi nitrogen oksida (NOx) yang diukur oleh alat referensi dalam satuan ppb (True hourly averaged concentration).
9. **PT08.S3(NOx)**: Respons sensor tungsten oksida (PT08.S3) yang menargetkan nitrogen oksida (NOx), dengan satuan relatif (sensor response).
10. **NO2(GT)**: Konsentrasi nitrogen dioksida (NO2) yang diukur oleh alat referensi dalam satuan µg/m³ (True hourly averaged concentration).
11. **PT08.S4(NO2)**: Respons sensor tungsten oksida (PT08.S4) yang menargetkan nitrogen dioksida (NO2), dengan satuan relatif (sensor response).
12. **PT08.S5(O3)**: Respons sensor indium oksida (PT08.S5) yang menargetkan ozon (O3), dengan satuan relatif (sensor response).
13. **T**: Suhu udara dalam derajat Celsius (°C).
14. **RH**: Kelembaban relatif udara dalam persen (%).
15. **AH**: Kelembaban absolut udara, yang menunjukkan jumlah uap air dalam udara, biasanya dalam satuan g/m³.

## **Data Loading**

Mengimpor library yang diperlukan untuk analisis data, visualisasi, dan manipulasi data berbentuk tabel.
"""

# Commented out IPython magic to ensure Python compatibility.
# Import library

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
# %matplotlib inline
import seaborn as sns

"""Mengambil dataset yang sebelumnya sudah diunggah ke Google Drive, lalu menampilkan 5 baris teratas dari data tersebut untuk melihat gambaran data"""

file_id = '1i7aAp0YjQ-f1G3cnJeVJZtyzsoIr8GGA'
url = f'https://drive.google.com/uc?id={file_id}'
df = pd.read_csv(url)

# Menampilkan data
df.head()

"""## **Exploratory Data Analysis**

### **Deskripsi Variabel**

Mengecek informasi umum tentang dataset, seperti tipe data dan jumlah nilai non-null dalam setiap kolom
"""

# cek informasi pada dataset
df.info()

"""Memeriksa ukuran dataset (jumlah baris dan kolom)"""

df.describe()

"""### **Univariate Analysis untuk Identifikasi Outliers**

#### Boxplot

Membuat boxplot untuk setiap kolom numerik untuk memvisualisasikan keberadaan outliers dalam dataset.
"""

numerical_cols = df.select_dtypes(include=['int64', 'float64']).columns

n_cols = 3
n_rows = (len(numerical_cols) // n_cols) + (len(numerical_cols) % n_cols > 0)

fig, axes = plt.subplots(n_rows, n_cols, figsize=(15, 5 * n_rows))
axes = axes.flatten()

for i, col in enumerate(numerical_cols):
    sns.boxplot(x=df[col], ax=axes[i], color='skyblue')
    axes[i].set_title(f"Boxplot of {col}")
    axes[i].set_xlabel(col)

plt.tight_layout()
plt.show()

"""#### Histogram

Membuat histogram pada setiap fitur dalam dataset untuk melihat distribusi data dari masing-masing kolom. Histogram ini membantu dalam memahami pola dan sebaran data pada setiap kolom serta mengidentifikasi outliers
"""

df.hist(bins=50, figsize=(15,10))
plt.show()

"""### **Multivariate Analysis**

#### Pair Plot

Menggunakan pairplot untuk menganalisis hubungan antar fitur numerik dalam dataset. Pairplot ini memberikan visualisasi hubungan antar pasangan kolom secara berpasangan, serta distribusi data.
"""

# Mengamati hubungan antar fitur numerik dengan fungsi pairplot()
sns.pairplot(df, diag_kind = 'kde')

"""#### Heatmap

Membuat heatmap untuk menampilkan matriks korelasi antar fitur numerik, yang menunjukkan hubungan linear antara kolom-kolom dalam dataset. Heatmap ini memberikan gambaran visual tentang kekuatan dan arah korelasi antara fitur-fitur numerik yang ada.
"""

# Memamnggil kolom numerik dari dataset
numerical_features = df.select_dtypes(include=['float64', 'int64']).columns

# Menghitung matriks korelasi untuk seluruh fitur numerik
correlation_matrix = df[numerical_features].corr().round(2)

# Membuat visualisasi heatmap
plt.figure(figsize=(10, 8))
sns.heatmap(data=correlation_matrix, annot=True, cmap='coolwarm', linewidths=0.5)
plt.title("Correlation Matrix untuk Fitur Numerik", size=20)
plt.show()

"""# **Data Preparation**

## **Hapus Fitur**

Menghapus kolom Date dan Time karena tidak akan digunakan sehingga tidak relevan dengan analisis yang akan dilakukan.
"""

df = df.drop(['Date', 'Time'], axis = 1)
df.shape

"""Menghapus kolom NMHC(GT) karena hampir 75% nilainya negatif, karena nilai negatif merupakan pengisi untuk data null sehingga akan mempengaruhi hasil analisis jika tidak dihapus. Selain itu, beberapa indikator senyawa tersebut tidak mungkin bernilai negatif, sehingga data yang bernilai negatif dihapus kecuali pada data temperatur"""

df = df.drop(['NMHC(GT)'], axis = 1)
df.shape

"""## **Hapus Data yang Tidak Wajar**"""

# Daftar kolom yang tidak termasuk 'T' (kolom temperatur)
columns_to_check = df.columns[df.columns != 'T']

# Menghapus baris dengan nilai negatif di semua kolom kecuali kolom temperatur
df = df[(df[columns_to_check] >= 0).all(axis=1)]

df.describe()

"""## **Hapus Outliers dan Missing Value**

Setelah penghapusan, data di cek kembali apakah masing terdapat missing value
"""

df.info()

"""Setelah penghapusan data bernilai negatif, data null sebelumnya juga ikut terhapus, sehingga langkah selanjutnya adalah menghapus outliers. Metode IQR digunakan untuk mengidentifikasi dan menghapus outliers, dengan menghapus data yang berada di luar rentang IQR yang dihitung dari kuartil pertama (Q1) dan kuartil ketiga (Q3)"""

# membuat IQR
numerical_cols = df.select_dtypes(include=['int64', 'float64']).columns

Q1 = df[numerical_cols].quantile(0.25)
Q3 = df[numerical_cols].quantile(0.75)
IQR = Q3 - Q1
df = df[~((df[numerical_cols] < (Q1-1.5*IQR)) | (df[numerical_cols] > (Q3+1.5*IQR))).any(axis=1)]

df.shape

"""## **Train-Test-Split**

Membagi dataset menjadi data latih dan data uji menggunakan fungsi train_test_split dari library scikit-learn dengan proporsi 80:20. Data latih digunakan untuk melatih model, sedangkan data uji digunakan untuk mengevaluasi performa model.
"""

# Menggunakan proporsi pembagian sebesar 80:20 dengan fungsi train_test_split dari sklearn
from sklearn.model_selection import train_test_split

X = df.drop(["T"],axis =1)
y = df["T"]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 123)

"""Memastikan jumlah sampel pada dataset keseluruhan, data latih, dan data uji telah sesuai dengan proporsi pembagian."""

# Mengecek jumlah sampel pada masing-masing bagian
print(f'Total # of sample in whole dataset: {len(X)}')
print(f'Total # of sample in train dataset: {len(X_train)}')
print(f'Total # of sample in test dataset: {len(X_test)}')

"""# **Modelling**

Lima algoritma yang akan digunakan, antara lain:


1.   K-Nearest Neighbor
2.   Random Forest
1.   Boosting Algorithm
1.   Linear Regression
2.   Decision Tree
"""

# Menyiapkan dataframe untuk analisis model
models = pd.DataFrame(index=['train_mse', 'test_mse'],
                      columns=['KNN', 'RandomForest', 'Boosting', 'LinearRegression', 'DecisionTree'])

"""## **K-Nearest Neighbor**

Melatih model regresi menggunakan algoritma K-Nearest Neighbor (KNN) dengan n_neighbors sebesar 10.
"""

from sklearn.neighbors import KNeighborsRegressor
from sklearn.metrics import mean_squared_error

knn = KNeighborsRegressor(n_neighbors=10)
knn.fit(X_train, y_train)

models.loc['train_mse','knn'] = mean_squared_error(y_pred = knn.predict(X_train), y_true=y_train)

"""## **Random Forest**

Melatih model regresi menggunakan Random Forest Regressor dengan n_estimators dan max_depth masing-masing sebesar 50 dan 16
"""

from sklearn.ensemble import RandomForestRegressor

RF = RandomForestRegressor(n_estimators=50, max_depth=16, random_state=55, n_jobs=-1)
RF.fit(X_train, y_train)

models.loc['train_mse','RandomForest'] = mean_squared_error(y_pred=RF.predict(X_train), y_true=y_train)

"""## **Boosting Algorithm**

Melatih model regresi menggunakan algoritma boosting dengan AdaBoost Regressor. dengan parameter Learning rate 0.05 dan Random state 55
"""

from sklearn.ensemble import AdaBoostRegressor

boosting = AdaBoostRegressor(learning_rate=0.05, random_state=55)
boosting.fit(X_train, y_train)
models.loc['train_mse','Boosting'] = mean_squared_error(y_pred=boosting.predict(X_train), y_true=y_train)

"""## **Linear Regression**

Melatih model regresi menggunakan metode Linear Regression untuk memprediksi nilai target berdasarkan fitur yang ada.
"""

from sklearn.linear_model import LinearRegression

linear_reg = LinearRegression()
linear_reg.fit(X_train, y_train)
models.loc['train_mse', 'LinearRegression'] = mean_squared_error(y_pred=linear_reg.predict(X_train), y_true=y_train)

"""## **Decision Tree**

Melatih model regresi menggunakan algoritma Decision Tree Regressor dengan max_depth sebesar 16.
"""

from sklearn.tree import DecisionTreeRegressor

decision_tree = DecisionTreeRegressor(max_depth=16, random_state=55)
decision_tree.fit(X_train, y_train)
models.loc['train_mse', 'DecisionTree'] = mean_squared_error(y_pred=decision_tree.predict(X_train), y_true=y_train)

"""# **Evaluation**

Metrik yang akan digunakan pada prediksi ini adalah MSE atau Mean Squared Error yang menghitung jumlah selisih kuadrat rata-rata nilai sebenarnya dengan nilai prediksi.
"""

# Evaluasi kelima model kita dengan metrik MSE

# Membuat variabel mse yang isinya adalah dataframe nilai mse data train dan test pada masing-masing algoritma
mse = pd.DataFrame(columns=['train', 'test'], index=['KNN', 'RF', 'Boosting', 'LinearRegression', 'DecisionTree',])

# Buat dictionary untuk setiap algoritma yang digunakan
model_dict = {
    'KNN': knn,
    'RF': RF,
    'Boosting': boosting,
    'LinearRegression': linear_reg,
    'DecisionTree': decision_tree,
}

# Menghitung Mean Squared Error masing-masing algoritma pada data train dan test
for name, model in model_dict.items():
    mse.loc[name, 'train'] = mean_squared_error(y_true=y_train, y_pred=model.predict(X_train)) / 1e3
    mse.loc[name, 'test'] = mean_squared_error(y_true=y_test, y_pred=model.predict(X_test)) / 1e3

# Panggil mse
print(mse)

# Membuat plot metrik tersebut menggunakan bar chart

fig, ax = plt.subplots()
mse.sort_values(by='test', ascending=False).plot(kind='barh', ax=ax, zorder=3)
ax.grid(zorder=0)

"""Dari gambar di atas, terlihat bahwa, model Random Forest (RF) memberikan nilai eror yang paling kecil. Sedangkan model dengan algoritma KNN memiliki eror yang paling besar. Sehingga model RF yang akan kita pilih sebagai model terbaik untuk melakukan prediksi temperatur."""

# Melakukan prediksi menggunakan beberapa temperatur dari data test

prediksi = X_test.iloc[:3].copy()
pred_dict = {'y_true':y_test[:3]}
for name, model in model_dict.items():
    pred_dict['prediksi_'+name] = model.predict(prediksi).round(1)

pd.DataFrame(pred_dict)