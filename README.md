# Laporan Proyek Machine Learning - Saif Rayhan Naufal
#### _Polutan Penyebab Pemanasan Global_

![Gambar Cover](https://st3.depositphotos.com/10665628/34984/v/450/depositphotos_349840932-stock-illustration-air-pollution-vector-illustration-factories.jpg)

# Domain Proyek
Pemanasan global dan pencemaran udara telah menjadi isu mendesak yang memengaruhi berbagai aspek kehidupan manusia. Peningkatan suhu bumi akibat emisi gas rumah kaca dari aktivitas manusia, seperti transportasi, pembakaran bahan bakar fosil, dan industri, telah memperburuk kualitas udara, terutama di kawasan perkotaan. Polutan seperti karbon monoksida (CO), benzena (C6H6), nitrogen oksida (NOx), dan ozon (O3) berdampak serius pada kesehatan manusia dan ekosistem. Data dari Organisasi Kesehatan Dunia (WHO) menunjukkan bahwa 91% populasi dunia tinggal di wilayah dengan kualitas udara buruk, yang menyebabkan sekitar 7 juta kematian setiap tahun akibat penyakit terkait polusi udara (_[Billions of People Still Breathe Unhealthy Air]_). Kondisi ini menandakan pentingnya langkah untuk mengidentifikasi, memantau, dan mengurangi pencemaran udara agar menciptakan lingkungan yang lebih sehat dan berkelanjutan.

Pemanfaatan teknologi dan data akurat menjadi kunci dalam memahami pola pencemaran dan menganalisis tren jangka panjang. Dengan data berkualitas, para peneliti dan pembuat kebijakan dapat mengambil keputusan berbasis bukti ilmiah untuk mengurangi dampak buruk polusi udara. Selain itu, pengembangan model prediktif menggunakan machine learning dan metode pengolahan data yang baik dapat memberikan solusi yang lebih terarah dalam upaya mitigasi. Langkah ini tidak hanya membantu meningkatkan kualitas penelitian lingkungan, tetapi juga memperkuat fondasi pengambilan keputusan strategis di tingkat lokal dan global.

# Business Understanding
## Problem Statement
1. Bagaimana interaksi antara karbon monoksida (CO) dengan senyawa kimia, seperti nitrogen oksida (NOx), ozon (O3), dan polutan lainnya yang dapat mempengaruhi kualitas udara?
2. Apa saja faktor-faktor yang mempengaruhi peningkatan suhu sehingga dapat memperburuk kualitas udara?

## Goals
1. Untuk memahami bagaimana interaksi antara CO dan senyawa polutan lainnya mempengaruhi konsentrasi dan dampak polusi udara, sehingga diharapkan dapat mengurangi aktivitas yang dapat menghasilkan senyawa-senyawa tersebut
2. Untuk mengidentifikasi dan menganalisis faktor-faktor yang mempengaruhi peningkatan suhu serta dampaknya terhadap kualitas udara, sehingga memberikan informasi yang dapat digunakan dalam perencanaan kebijakan lingkungan dan pengendalian polusi.

## Solution Statements
1. Untuk memahami interaksi antara karbon monoksida (CO) dengan senyawa lainnya, visualisasi data seperti heatmaps dan pair plots akan digunakan untuk menggambarkan korelasi antar fitur. Dengan visualisasi ini, hubungan antara polutan dan faktor lingkungan lainnya dapat dengan jelas diindentifikasi serta membantu dalam mendeteksi pola-pola tersembunyi yang mungkin mempengaruhi kualitas udara. Teknik visualisasi ini akan memberikan gambaran tentang interaksi antar variabel dan bagaimana masing-masing polutan berkontribusi terhadap perubahan kualitas udara.
2. Untuk mengevaluasi faktor-faktor yang mempengaruhi peningkatan suhu, metrik Mean Absolute Error (MAE) akan digunakan dalam model regresi. MAE akan memberikan gambaran yang jelas tentang seberapa akurat prediksi suhu berdasarkan beberapa faktor. Dengan mengukur kesalahan prediksi, dapat diketahui faktor-faktor mana yang paling berpengaruh terhadap perubahan suhu dan mampu membantu memperbaiki model untuk meningkatkan akurasi dan memberikan solusi yang lebih efektif dalam mitigasi suhu dan polusi udara.

# Data Understanding
Dataset yang digunakan dalam proyek ini bersumber dari Kaggle dan berfokus pada pemantauan kualitas udara di kawasan perkotaan. Dataset ini terdiri dari 15 kolom yang berisi data hasil pengukuran dari berbagai sensor kimia, yang mengukur konsentrasi polutan udara seperti karbon monoksida (CO), nitrogen oksida (NOx), ozon (O3), dan polutan lainnya. Data dikumpulkan dari perangkat sensor yang ditempatkan di lokasi perkotaan di Italia, dengan periode pengukuran yang mencakup satu tahun, mulai dari Maret 2004 hingga Februari 2005. Dataset ini memberikan informasi penting mengenai respons sensor terhadap konsentrasi polutan, serta variabel lingkungan lainnya seperti suhu dan kelembaban. Dataset ini berisi 9357 data hasil pengukuran per jam dari lima sensor logam oksida kimia yang tertanam dalam perangkat Air Quality Chemical Multisensor Device, yang terletak di area dengan polusi tinggi di sebuah kota Italia. Data yang terekam mencakup konsentrasi rata-rata per jam untuk CO, Hidrokarbon Non-Metanik, Benzena, Nitrogen Oksida (NOx), dan Nitrogen Dioksida (NO2), yang disediakan oleh analyzer referensi bersertifikat. Nilai yang hilang pada dataset ini ditandai dengan nilai -200. Dataset ini dapat diunduh dari Kaggle melalui informasi berikut:

**Judul**: [Air-Quality]

**Pemilik**: [citrahsagala]

**Sumber**: Kaggle
    
**Variabel Dataset**

|No | Fitur | Keterangan |
| ------ | ------ | ------ |
| 1 | Date | Tanggal pengukuran dalam format DD/MM/YYYY.
| 2 | Time | Waktu pengukuran dalam format HH.MM.SS.
| 3 | CO(GT)| Konsentrasi karbon monoksida (CO) yang diukur oleh alat referensi dalam satuan mg/m³ (True hourly averaged concentration CO).
| 4 | PT08.S1(CO) | Respons sensor tin oksida (PT08.S1) yang menargetkan karbon monoksida (CO), dengan satuan relatif (sensor response).
| 5 | NMHC(GT) | Konsentrasi hidrokarbon non-metanik (NMHC) yang diukur oleh alat referensi dalam satuan µg/m³ (True hourly averaged concentration).
| 6 | C6H6(GT) | Konsentrasi benzena (C6H6) yang diukur oleh alat referensi dalam satuan µg/m³ (True hourly averaged concentration).
| 7 | PT08.S2(NMHC) | Respons sensor titania (PT08.S2) yang menargetkan hidrokarbon non-metanik (NMHC), dengan satuan relatif (sensor response).
| 8 | NOx(GT) | Konsentrasi nitrogen oksida (NOx) yang diukur oleh alat referensi dalam satuan ppb (True hourly averaged concentration).
| 9 | PT08.S3(NOx) | Respons sensor tungsten oksida (PT08.S3) yang menargetkan nitrogen oksida (NOx), dengan satuan relatif (sensor response).
| 10 | NO2(GT) | Konsentrasi nitrogen dioksida (NO2) yang diukur oleh alat referensi dalam satuan µg/m³ (True hourly averaged concentration).
| 11 | PT08.S4(NO2) | Respons sensor tungsten oksida (PT08.S4) yang menargetkan nitrogen dioksida (NO2), dengan satuan relatif (sensor response).
| 12 | PT08.S5(O3) | Respons sensor indium oksida (PT08.S5) yang menargetkan ozon (O3), dengan satuan relatif (sensor response).
| 13 | T | Suhu udara dalam derajat Celsius (°C).
| 14 | RH | Kelembaban relatif udara dalam persen (%).
| 15 | AH | Kelembaban absolut udara, yang menunjukkan jumlah uap air dalam udara, biasanya dalam satuan g/m³.

## Data Loading
Pada tahap ini, langkah pertama yang dilakukan adalah mengimpor library yang diperlukan untuk analisis data, visualisasi, dan manipulasi data berbentuk tabel. Library digunakan karena dapat membantu dalam memanipulasi, membersihkan, dan memvisualisasikan data dengan efisien. Selanjutnya, dataset yang sebelumnya diunggah ke Google Drive diimpor untuk dianalisis lebih lanjut. Data kemudian ditampilkan 5 baris teratas menggunakan fungsi `head()`, hal ini bertujuan untuk memberikan gambaran awal tentang struktur dan isi dataset, seperti kolom yang ada dan apakah ada nilai yang hilang atau tidak sesuai. Langkah ini dilakukan agar dapat mengidentifikasi masalah pada data yang perlu ditangani lebih lanjut, seperti data yang tidak relevan, sebelum melakukan analisis lebih mendalam. Dengan cara ini, data dapat dipersiapkan dengan baik untuk analisis lebih lanjut. Berikut adalah tampilan data secara garis besar.

![Data Loading](https://github.com/user-attachments/assets/f92a3f6c-a77d-47ff-aa45-93d310e45f6a)

## Exploratory Data Analysis
Exploratory Data Analysis (EDA) adalah tahap untuk memahami struktur dan pola dalam dataset sebelum melakukan analisis lebih lanjut. Pada kasus kualitas udara ini, EDA bertujuan untuk memeriksa distribusi setiap kolom data, seperti konsentrasi polutan dan faktor lingkungan, serta mengidentifikasi potensi masalah seperti outliers, missing values, atau data yang tidak relevan. Dengan melakukan visualisasi dan perhitungan statistik deskriptif, EDA membantu dalam memahami hubungan antar variabel. Proses ini juga memungkinkan untuk membersihkan data, mengatasi nilai yang hilang, dan menyaring data yang tidak konsisten, sehingga memberikan dasar yang kuat untuk analisis lebih lanjut dan pemodelan yang akurat.

### Deskripsi Variabel

Deskripsi variabel memberikan pemahaman tentang setiap kolom dalam dataset, termasuk jenis data, satuan pengukuran, dan peran masing-masing variabel. Pada tahap ini, dijelaskan variabel seperti konsentrasi polutan (CO, NOx, NO2, O3) dan faktor lingkungan seperti suhu dan kelembaban, agar analisis data berikutnya dapat dilakukan dengan tepat.

|No | Kolom | Jumlah | Tipe Data |
| ------ | ------ | ------ |  ------ |
| 1   | Date           | 9357    | object 
| 2   | Time           | 9357    | object 
| 3   | CO(GT)         | 9357    | float64
| 4   | PT08.S1(CO)    | 9357    | int64 
| 5   | NMHC(GT)       | 9357    | float64
| 6   | C6H6(GT)       | 9357    | float64
| 7   | PT08.S2(NMHC)  | 9357    | int64 
| 8   | NOx(GT)        | 9357    | int64 
| 9   | PT08.S3(NOx)   | 9357    | int64 
| 10  | NO2(GT)        | 9357    | int64 
| 11  | PT08.S4(NO2)   | 9357    | int64 
| 12  | PT08.S5(O3)    | 9357    | float64
| 13  | T              | 9357    | float64
| 14  | RH             | 9357    | float64
| 15  | AH             | 9356    | float64

Data memiliki 9.357 baris untuk setiap kolom, kecuali untuk kolom "AH" yang memiliki 9.356 baris, hal ini menunjukkan bahwa sebagian besar data terisi lengkap. Jenis data dalam kolom ini bervariasi, sebagian besar kolom memiliki tipe data numerik dengan tipe data `float64` untuk pengukuran gas dan kondisi lingkungan seperti suhu dan kelembaban, serta `int64` untuk hasil pengukuran sensor gas tertentu. Kolom "Date" dan "Time" memiliki tipe data `object`.


Langkah selanjutnya, kolom "Date" dan "Time" akan dihapus karena tidak relevan. Berikut adalah ringkasan statistik deskriptif dari dataset tersebut.

![Deskripsi Variabel](https://github.com/user-attachments/assets/13c4bdd2-a09d-4647-b733-8a6ccb22feef)

Untuk mempersiapkan analisis, dilakukan beberapa hal berikut.
1. Menghapus kolom "NMHC(GT)" karena hampir 75% nilainya negatif.
2. Indikator senyawa pada dataset  tidak mungkin bernilai negatif, sehingga data yang bernilai negatif dihapus kecuali pada data temperatur.

### Missing Value dan Outliers
Berdasarkan deskripsi variabel sebelumnya, terdapat data yang bernilai, untuk itu dilakukan penghapusan  data tersebut menggunakan fungsi `dropna()`. Berikut adalah kondisi data setelah nilai kosong dihapus.

<img src="https://github.com/user-attachments/assets/8ca5df61-9351-4b3e-ad57-daa4ca0e6d9a" alt="Missing Value" width="300">

Data tersebut berkurang dari yang sebelumnya berjumlah 9357 menjadi 6941 karena penghapusan data kosong.

Selanjutnya, untuk mengidentifikasi keberadaan outliers, digunakan visualisasi menggunakan box plot

![Boxplot](https://github.com/user-attachments/assets/a8aa1e50-38ea-489a-9812-bd9dfcb60a6d)

Boxplot di atas menunjukkan adanya outliers pada masing-masing fitur, sehingga perlu dilakukan penanganan untuk memastikan model yang dibangun tidak terpengaruh oleh data yang ekstrem. Penanganan outliers dapat dilakukan dengan menghapus data yang mengandung outlier. Untuk menghapus data outlier, digunakan metode IQR dengan cara menghapus data yang berada di luar rentang IQR yang dihitung dari kuartil pertama (Q1) dan kuartil ketiga (Q3)

### Univariate Analysis
Analisis univariate pada kasus dilakukan dengan menggunakan histogram untuk setiap fitur dalam dataset. Histogram akan memberikan gambaran visual mengenai distribusi data di setiap kolom yang membantu memahami pola dan sebaran nilai pada setiap fitur. Melalui histogram, data dapat diindentifikasi apakah terdistribusi secara normal, memiliki distribusi miring (skewed), atau terdapat outlier yang perlu diperhatikan. 

![Histogram](https://github.com/user-attachments/assets/2d599b46-91af-4645-89aa-617ab8606162)

Berdasarkan visualisasi di atas, diperoleh beberapa informasi berikut.
1. Setiap fitur memiliki distribusi yang berbeda. Sebagai contoh, beberapa fitur seperti "C6H6(GT)" dan "NOx(GT)" menunjukkan distribusi yang miring ke kanan, hal ini berarti lebih banyak data bernilai kecil dibanding data yang bernilai besar, semisal pada C6H6(GT) menunjukkan bahwa semakin tinggi kadar benzena, semakin jarang peristiwa tersebut terjadi.
2. Beberapa senyawa seperti "PT08.S4(NO2)" dan "RH" menunjukkan distribusi yang lebih simetris, menunjukkan data terdistribusi secara normal berbentuk seperti lonceng. Artinya, sebagian besar data terpusat di sekitar nilai tengah (mean), dan semakin sedikit data yang jauh dari nilai tengah tersebut.


### Multivariate Analysis
Multivariate Analysis adalah teknik analisis yang digunakan untuk melihat hubungan antara lebih dari dua variabel secara bersamaan. Pengukuran ini berfungsi untuk memahami kualitas udara dan faktor-faktor seperti suhu, kelembapan, dan konsentrasi polutan (CO, NOx, C6H6, dll.) saling berinteraksi satu sama lain dan mempengaruhi fenomena tertentu. Multivariate analysis pada kasus ini menggunakan dua pendekatan, yakni menggunakan pair plot dan heatmap

#### Pair Plot

![Pair Plot](https://github.com/user-attachments/assets/8599722e-b5d4-499a-a5dd-d60c4d239e03)

#### Heatmap

![Heatmap](https://github.com/user-attachments/assets/b8d8e326-3519-49c6-9e05-aad5f50b84e5)

Berdasarkan kedua visualisasi di atas yang menggambarkan korelasi antar variabel, diperoleh beberapa informasi sebagai berikut
1. Terdapat korelasi sebesar 0.63 antara temperatur dengan pengukuran NO2 menggunakan sensor  perangkat Air Quality Chemical Multisensor System. Selain itu, terdapat korelasi antara temperatur dengan Air Humidity sebesar 0.66.
    - NO2 merupakan penyumbang utama dalam pembentukan ozon yang memiliki efek pemanasan pada atmosfer. Saat temperatur meningkat, reaksi kimia yang melibatkan NO2 menjadi lebih cepat, mempercepat pembentukan ozon yang kemudian dapat meningkatkan temperatur.
    - AH (Air Humidity) merupakan salah satu faktor yang sangat berpengaruh terhadap temperatur. Uap air sangat efektif  menyerap dan memerangkap radiasi yang menyebabkan peningkatan temperatur. Ketika AH meningkat, atmosfer menjadi lebih lembab dan cenderung menyimpan lebih banyak energi panas.
2. Karbon monoksida baik yang diukur langsung menggunakan alat analitik maupun melalui sensor menunjukkan adanya korelai dengan zat lain seperti C6H6, NMHC, NOx, NO2, dan O3. Hal ini terjadi karena senyawa tersebut merupakan zat yang dihasilkan dari proses pembakaran yang tidak sempurna, seperti emisi kendaraan bermotor, aktivitas industri, dan pembakaran bahan bakar fosil. Korelasi ini mencerminkan hubungan antara berbagai polutan dalam memengaruhi kualitas udara.

# Data Preparation

Data preparation dilakukan untuk memastikan model machine learning tidak mengalami overfitting dan dapat menggeneralisasi dengan baik. Tahap ini memungkinkan model dilatih menggunakan data latih dan dievaluasi menggunakan data uji yang belum pernah dilihat sebelumnya, sehingga memberikan gambaran tentang kinerja model. Selain itu, tahap ini juga memudahkan dalam pemisahan fitur (X) dan target (y), yang penting untuk pelatihan model yang efektif dan evaluasi yang akurat.

Data preparation yang dilakukan pada kasus ini hanya berupa train test split, hal ini karena dataset ini tidak mengandung fitur kategori yang digunakan dalam analisis atau variabel kategorikal yang memerlukan encoding, karena semua fitur yang ada adalah numerik. Selain itu, dataset ini tidak menunjukkan indikasi adanya dimensi yang sangat tinggi yang memerlukan pengurangan, sehingga tidak dilakukan reduksi dimensi.


**Train-Test-Split**
Dataset dibagi menjadi dua bagian utama, yaitu data latih dan data uji untuk memastikan model yang dikembangkan dapat belajar dari data latih dan diukur kinerjanya menggunakan data uji. Data latih bertujuan untuk mengajari model pola yang terdapat dalam data, sedangkan data uji digunakan untuk mengevaluasi sejauh mana model dapat menggeneralisasi pola tersebut pada data baru yang belum pernah dilihat sebelumnya.



Berikut langkah-langkah yang dilakukan untuk membagi dataset tersebut.
1. Menentukan kolom mana yang menjadi target (variabel yang ingin diprediksi) dan kolom mana yang menjadi fitur (variabel yang digunakan untuk prediksi). Dalam hal ini, targetnya adalah kolom "T", sementara fitur adalah semua kolom lainnya.
2. Data target diekstrak ke dalam satu variabel (y) dan data fitur ke dalam variabel lain (X). Ini memastikan bahwa data target terisolasi dari fitur yang akan digunakan oleh model.
3. Menentukan proporsi data yang akan digunakan untuk pelatihan model sebanyak 80% dan data yang akan digunakan untuk pengujian model sebanyak 20%.
4. Dataset akan terbagi menjadi empat bagian, diantaranya `X_train`, `X_test`, `y_train`, dan `y_test`. Bagian `X_train` dan `y_train` digunakan untuk melatih model, sedangkan `X_test` dan `y_test` digunakan untuk menguji performa model.

Berdasarkan pembagian, dari 6222 data yang sebelumnya sudah melalui proses pembersihan outlier, diperoleh 4977 data untuk data latih dan sisanya sebanyak 1245 untuk data uji.

<img src="https://github.com/user-attachments/assets/3140c966-b1c2-4201-b509-747af55646e9" alt="Missing Value" width="400">

# Modelling
Lima algoritma yang akan digunakan, antara lain:

- K-Nearest Neighbor
- Random Forest
- Boosting Algorithm
- Linear Regression
- Decision Tree

Pada proses pemodelan regresi, tahapan yang dilakukan adalah sebagai berikut:
1. Mengimport sub modul berbagai model dari package `sklearn`.
2. Menyiapkan dataset yang telah dibagi sebelumnya menjadi data latih (`X_train` dan `y_train`)  untuk melatih model regresi.
3. Memilih berbagai algoritma regresi diterapkan, yaitu K-Nearest Neighbor (KNN), Random Forest, AdaBoost, Linear Regression, dan Decision Tree. 
4. Model-model regresi dilatih menggunakan data latih yang sudah disiapkan sebelumnya dengan fungsi `fit()`.

### K-Nearest Neighbor
Parameter
- `n_neighbors=10` untuk menentukan banyaknya jumlah neighbors terdekat yang digunakan untuk memprediksi nilai target.

Kelebihan
- Sederhana dan mudah dipahami.
- Tidak memerlukan asumsi distribusi data.
- Bisa menangani data non-linear dengan baik.

Kekurangan
- Performa menurun pada dataset besar.
- Rentan terhadap noise dan outliers.
- Membutuhkan banyak memori.

### Random Forest
Parameter
- `n_estimators=50` mengindikasikan bahwa model akan menggunakan 50 decision trees untuk melakukan prediksi.
- `max_depth=16` berfungsi membatasi kedalaman setiap decision trees hingga 16 level untuk menjaga kompleksitas dan generalisasi tetap seimbang.

Kelebihan
- Mengurangi overfitting dibandingkan dengan desicion trees tunggal.
- Dapat menangani data besar dan kompleks dengan baik.

Kekurangan
- Lebih lambat untuk pelatihan dan prediksi.
- Kurang interpretatif karena banyaknya pohon yang digunakan.

### Boosting Algorithm
Parameter
- `learning_rate = 0.05` berfungsi mengontrol seberapa besar kontribusi setiap base learner terhadap prediksi akhir. Dengan nilai learning rate 0.05, model akan mengadaptasi pembelajaran dengan langkah yang lebih kecil, mengurangi kemungkinan overfitting.
- `random_state = 55` untuk memastikan bahwa hasil eksperimen dapat direproduksi dengan cara menetapkan nilai acak yang sama di setiap eksekusi kode. Nilai ini mengontrol aspek acak dalam algoritma agar hasilnya tetap konsisten.

Kelebihan
- Meningkatkan akurasi model yang lebih lemah.
- Efektif untuk data dengan noise atau ketidakseimbangan.

Kekurangan
- Rentan terhadap overfitting jika learning rate terlalu tinggi.
- Kinerja menurun pada data yang sangat tidak seimbang.

### Linear Regression
Parameter
- Tidak ada parameter tambahan yang diberi nilai dalam kode untuk model Linear Regression.

Kelebihan
- Mudah dipahami dan cepat.
- Memberikan interpretasi yang jelas tentang hubungan antara fitur dan target.

Kekurangan
- Tidak efektif untuk data non-linear.
- Rentan terhadap outliers.

### Decision Tree
Parameter
- `max_depth = 16`, seperti pada Random Forest, parameter ini membatasi kedalaman decision trees hingga 16 level.
- `random_state = 55`, sama seperti pada Boosting, parameter ini mengontrol aspek acak dalam pembuatan decision trees, sehingga hasilnya bisa direplikasi di masa depan.


Kelebihan
- Mudah dipahami dan diinterpretasikan.
- Dapat menangani data numerik dan kategorikal.

Kekurangan
- Rentan terhadap overfitting, terutama jika pohon terlalu dalam.
- Kurang stabil, perubahan kecil pada data dapat menghasilkan pohon yang berbeda.

# Evaluation
Metrik yang akan digunakan pada evaluasi ini adalah MSE atau Mean Squared Error yang menghitung jumlah selisih kuadrat rata-rata nilai sebenarnya dengan nilai prediksi. MSE pada kasus ini digunakan untuk mengevaluasi kinerja lima model regresi yang diterapkan pada data temperatur.

**Formula MSE**

![Formula MSE](https://github.com/user-attachments/assets/eebc4db3-c3e1-481f-9c9b-2de83e1eb686)

Keterangan
- n adalah jumlah data
- 𝑦 true,𝑖 adalah nilai sebenarnya (ground truth)
- 𝑦 pred, 𝑖 adalah nilai prediksi yang dihasilkan oleh model

MSE mengukur seberapa besar kesalahan antara prediksi model dan nilai aktualnya. Nilai MSE yang lebih kecil menunjukkan bahwa model memiliki prediksi yang lebih akurat, karena kesalahan antara nilai prediksi dan nilai aktual lebih kecil.

**Hasil Evaluasi Berdasarkan Metrik MSE**

|Model | Train | Test |
| ------ | ------ | ------ |
| KNN               | 0.011909  | 0.016444
| RF                | 0.000027  | 0.000177
| Boosting          | 0.011982  | 0.01283
| LinearRegression  | 0.005254  | 0.005991
| DecisionTree      |      0.0  | 0.000655

![Grafik MSE](https://github.com/user-attachments/assets/fee65cc2-d5d1-4f92-aaff-16f963533df8)

MSE yang dihitung untuk masing-masing model pada data latih dan data uji memberikan gambaran tentang seberapa baik model dalam memprediksi temperatur baik pada data yang dilatih (train) maupun data uji (test). Berikut adalah hasil evaluasi dengan metrik MSE.
1. **Random Forest (RF)** memberikan nilai MSE yang paling kecil di antara semua model. Ini menunjukkan bahwa model RF memiliki prediksi yang paling akurat di data latih (train) dan data uji (test). MSE yang rendah menunjukkan bahwa model RF dapat menangani variabilitas data dengan baik dan memberikan prediksi yang lebih mendekati nilai sebenarnya.
2. **K-Nearest Neighbors (KNN)** menunjukkan nilai MSE yang paling besar dibandingkan model lainnya, hal ini mengindikasikan bahwa model KNN memiliki kesalahan prediksi yang lebih besar, yang mungkin disebabkan oleh ketidakmampuan model untuk menangani hubungan kompleks dalam data atau pemilihan parameter.
3. **Boosting, Linear Regression, dan Decision Tree**  memiliki MSE yang lebih tinggi daripada RF, tetapi lebih rendah dari KNN. Meskipun mereka lebih baik dari KNN, performa mereka tetap tidak dapat menandingi RF dalam hal akurasi prediksi.

**Prediksi Berdasarkan MSE:**

![Prediksi MSE](https://github.com/user-attachments/assets/f8cd956b-87ef-4cfa-b333-7b5f5f378301)

Pada contoh prediksi untuk 3 data uji (seperti yang ditampilkan dalam tabel), model yang menggunakan Random Forest (RF) menghasilkan nilai prediksi yang lebih mendekati nilai aktual dibandingkan dengan model-model lainnya, yang semakin mengkonfirmasi bahwa RF adalah model terbaik yang dipilih berdasarkan hasil MSE terendah.

[Billions of People Still Breathe Unhealthy Air]: <https://www.who.int/news/item/04-04-2022-billions-of-people-still-breathe-unhealthy-air-new-who-data>
[Air-Quality]: <https://www.kaggle.com/datasets/citrahsagala/airquality>
[citrahsagala]: <https://www.kaggle.com/citrahsagala>
