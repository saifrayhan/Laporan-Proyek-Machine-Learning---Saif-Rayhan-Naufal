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
2. Untuk mengevaluasi faktor-faktor yang mempengaruhi peningkatan suhu, metrik MSE akan digunakan dalam model regresi. MSE akan memberikan gambaran yang jelas tentang seberapa akurat prediksi suhu berdasarkan beberapa faktor. Dengan mengukur kesalahan prediksi, dapat diketahui faktor-faktor mana yang paling berpengaruh terhadap perubahan suhu dan mampu membantu memperbaiki model untuk meningkatkan akurasi dan memberikan solusi yang lebih efektif dalam mitigasi suhu dan polusi udara.

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

Langkah selanjutnya, kolom "Date" dan "Time" akan dihapus karena tidak relevan. Penghapusan ini menggunakan fungsi `dropna()`. Selain menghapus kolom tersebut, untuk mempersiapkan analisis dilakukan beberapa hal berikut.
1. Menghapus kolom "NMHC(GT)" karena hampir 75% nilainya negatif. 
2. Indikator senyawa pada dataset  tidak mungkin bernilai negatif, sehingga data yang bernilai negatif dihapus kecuali pada data temperatur.

Berikut adalah ringkasan statistik deskriptif dari dataset yang sudah dilakukan pembersihan nilai negatif.

![Deskripsi Variabel](https://github.com/user-attachments/assets/ba225f5a-92cb-4f10-bebe-e491a41e5285)


### Missing Value dan Outliers
Berdasarkan deskripsi variabel sebelumnya, terdapat data yang bernilai null, untuk itu perlu dicek kembali apakah setelah dilakukan pembersihan sebelumnya masih terdapat missing value. Pengecekan dilakukan menggunakan fungsi `isna().sum()`. Setelah dicek, sudah tidak terdapat missing value pada dataset

<img src="https://github.com/user-attachments/assets/8ca5df61-9351-4b3e-ad57-daa4ca0e6d9a" alt="Missing Value" width="300">

Data tersebut berkurang dari yang sebelumnya berjumlah 9357 menjadi 6941 karena data yang bernilai negatif sudah dibersihkan.

Selanjutnya, untuk mengidentifikasi keberadaan outliers, digunakan visualisasi menggunakan box plot. Boxplot bekerja dengan menggambarkan distribusi data melalui lima angka penting, diantaranya nilai minimum, kuartil pertama (Q1), median (Q2), kuartil ketiga (Q3), dan nilai maksimum. Outlier diidentifikasi sebagai data yang berada di luar rentang interkuartil (IQR), yaitu Q3 − Q1, biasanya lebih kecil dari Q1 − 1.5×IQR atau lebih besar dari Q3 + 1.5×IQR. 

![Boxplot](https://github.com/user-attachments/assets/a8aa1e50-38ea-489a-9812-bd9dfcb60a6d)

Boxplot di atas menunjukkan adanya outliers pada masing-masing fitur, sehingga perlu dilakukan penanganan untuk memastikan model yang dibangun tidak terpengaruh oleh data yang ekstrem. Penanganan outliers dapat dilakukan dengan menghapus data yang mengandung outlier. Untuk menghapus data outlier, digunakan metode IQR dengan cara menghapus data yang berada di luar rentang IQR yang dihitung dari kuartil pertama (Q1) dan kuartil ketiga (Q3). Setelah outlier dihapus menggunakan metode IQR, data yang sebelumnya berjumlah 6941 berkurang menjadi 6222.

<img src="https://github.com/user-attachments/assets/8537a275-889d-4311-8aac-10d5010b0c65" alt="IQR" width="600">

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

## Train-Test-Split
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

### K-Nearest Neighbor
K-Nearest Neighbors (KNN) adalah salah satu algoritma yang sederhana namun kuat, digunakan untuk masalah klasifikasi dan regresi. Model ini termasuk dalam kategori algoritma instance-based learning atau lazy learning, yang berarti bahwa model ini tidak membangun suatu model atau fungsi yang eksplisit selama proses pelatihan, tetapi menyimpan seluruh dataset pelatihan untuk digunakan pada saat prediksi. Berikut adalah cara kerja dari model ini.
1. Model KNN dibuat dengan menggunakan kelas `KNeighborsRegressor`. Kelas ini digunakan untuk tugas regresi, di mana model akan memprediksi nilai numerik berdasarkan kedekatannya dengan data lain.
2. Model KNN dilatih menggunakan data pelatihan yang disediakan, yaitu `X_train` (fitur atau atribut) dan `y_train` (nilai target atau label). Pada tahap ini, model tidak benar-benar "belajar" seperti pada algoritma lain. KNN hanya menyimpan data pelatihan dan menggunakannya nanti untuk melakukan prediksi.
3. Setelah model dilatih, model akan memprediksi nilai untuk data pelatihan itu sendiri. Prediksi ini dilakukan dengan mencari tetangga terdekat dari setiap titik data pelatihan dalam ruang fitur, dan nilai target yang diprediksi adalah nilai rata-rata dari target tetangga terdekat tersebut.
4. MSE dihitung dengan cara membandingkan nilai yang diprediksi oleh model terhadap nilai yang sebenarnya di `y_train`, dengan menghitung rata-rata dari kuadrat selisih antara nilai prediksi dan nilai aktual.
5. Nilai MSE yang dihitung disimpan ke dalam sebuah struktur data seperti `models.loc` untuk dibandingan dengan model lain.

|Kelebihan | Kekurangan |
| ------ | ------ |
| - Sederhana dan mudah dipahami. | - Performa menurun pada dataset besar. | 
| - Tidak memerlukan asumsi distribusi data. | - Rentan terhadap noise dan outliers. | 
| - Bisa menangani data non-linear dengan baik. | - Membutuhkan banyak memori. | 

Parameter
- `n_neighbors=10` untuk menentukan banyaknya jumlah neighbors terdekat yang digunakan untuk memprediksi nilai target.

### Random Forest
Random Forest adalah salah satu algoritma machine learning yang digunakan untuk tugas klasifikasi dan regresi. Algoritma ini merupakan ensemble method, yang berarti ia menggabungkan hasil dari banyak model sederhana untuk membuat keputusan yang lebih kuat dan stabil. Berikut adalah cara kerja dari model ini.
1. Model `RandomForestRegressor` dibuat dengan parameter yang telah ditentukan, seperti jumlah decision trees (`n_estimators`) dan kedalaman maksimum pohon (`max_depth`). Model ini bertujuan untuk memprediksi nilai numerik pada data baru.
2. Model dilatih dengan menggunakan data pelatihan, yaitu `X_train` (fitur) dan `y_train` (target). Pada proses ini, Random Forest membangun banyak decision trees yang masing-masing dilatih menggunakan subset data yang berbeda.
3. Setelah dilatih, model akan digunakan untuk memprediksi nilai target pada data pelatihan. Setiap decision trees memberikan prediksi dan Random Forest akan menggabungkan hasil prediksi dari semua pohon untuk menghasilkan prediksi akhir.
4. Model dievaluasi dengan menghitung Mean Squared Error (MSE), yang mengukur seberapa jauh prediksi model dari nilai yang sebenarnya. MSE dihitung dengan membandingkan hasil prediksi dengan nilai asli dalam data pelatihan (`y_train`).

|Kelebihan | Kekurangan |
| ------ | ------ |
| - Mengurangi overfitting dibandingkan dengan desicion trees tunggal. | - Lebih lambat untuk pelatihan dan prediksi.
| - Dapat menangani data besar dan kompleks dengan baik. | - Kurang interpretatif karena banyaknya pohon yang digunakan.

Parameter
- `n_estimators=50` mengindikasikan bahwa model akan menggunakan 50 decision trees untuk melakukan prediksi.
- `max_depth=16` berfungsi membatasi kedalaman setiap decision trees hingga 16 level untuk menjaga kompleksitas dan generalisasi tetap seimbang.

### Boosting Algorithm
Boosting adalah salah satu teknik ensemble learning yang bertujuan untuk meningkatkan kinerja model dengan menggabungkan hasil dari banyak model yang lebih sederhana untuk menghasilkan model yang lebih kuat. Teknik ini berfokus pada membangun model secara bertahap, di mana setiap model baru berusaha memperbaiki kesalahan yang dibuat oleh model sebelumnya. Berikut adalah cara kerja dari model ini.
1. Model `AdaBoostRegressor` diinisialisasi dengan parameter seperti `learning_rate` dan `random_state`. `learning rate` mengontrol seberapa besar perubahan yang dilakukan pada setiap iterasi, sedangkan `random_state` memastikan hasil yang konsisten setiap kali model dilatih.
2. Model dilatih menggunakan data pelatihan yang terdiri dari fitur (`X_train`) dan nilai target (`y_train`). AdaBoost bekerja dengan membangun beberapa model (biasanya decision trees sederhana). Model pertama dilatih pada data pelatihan biasa, tetapi model-model berikutnya dilatih pada data yang lebih sulit atau data yang sebelumnya diprediksi dengan kesalahan lebih besar.
3. Setiap model yang dibangun dalam proses AdaBoost bertujuan untuk memperbaiki kesalahan yang dibuat oleh model sebelumnya. Dengan kata lain, setiap model baru mencoba memperbaiki kesalahan prediksi yang ada dengan lebih fokus pada data yang sulit diprediksi.
4. Setelah proses pelatihan selesai, model digunakan untuk memprediksi nilai target pada data pelatihan. Semua prediksi dari setiap model digabungkan untuk menghasilkan prediksi akhir.
5. Model dievaluasi dengan menghitung Mean Squared Error (MSE), yang mengukur seberapa jauh prediksi model dari nilai yang sebenarnya dalam data pelatihan.

|Kelebihan | Kekurangan |
| ------ | ------ |
| - Meningkatkan akurasi model yang lebih lemah. | - Rentan terhadap overfitting jika learning rate terlalu tinggi. | 
| - Efektif untuk data dengan noise atau ketidakseimbangan. | - Kinerja menurun pada data yang sangat tidak seimbang. | 

Parameter
- `learning_rate = 0.05` berfungsi mengontrol seberapa besar kontribusi setiap base learner terhadap prediksi akhir. Dengan nilai learning rate 0.05, model akan mengadaptasi pembelajaran dengan langkah yang lebih kecil, mengurangi kemungkinan overfitting.
- `random_state = 55` untuk memastikan bahwa hasil eksperimen dapat direproduksi dengan cara menetapkan nilai acak yang sama di setiap eksekusi kode. Nilai ini mengontrol aspek acak dalam algoritma agar hasilnya tetap konsisten.

### Linear Regression
Linear Regression adalah metode statistika yang digunakan untuk memodelkan hubungan antara satu atau lebih variabel independen (fitur) dengan variabel dependen (target) menggunakan fungsi linier. Pada dasarnya, model ini mencoba untuk menggambarkan hubungan antara variabel-variabel tersebut dengan mencari garis lurus (atau hiperplane dalam dimensi lebih tinggi) yang paling cocok dengan data. Berikut adalah cara kerja dari model ini.
1. Model `LinearRegression` dari `sklearn.linear_model` diinisialisasi tanpa parameter tambahan. Ini berarti model akan menggunakan metode standar dalam regresi linier.
2. Model dilatih dengan data pelatihan yang terdiri dari fitur (`X_train`) dan target/label (`y_train`). Proses pelatihan ini bertujuan untuk mencari garis (atau hiperplane pada dimensi lebih tinggi) yang paling sesuai dengan data tersebut.
3. Selama pelatihan, model mencoba untuk menemukan hubungan linier antara fitur dan target. Artinya, model mencari koefisien atau bobot yang dapat menggambarkan hubungan tersebut dengan cara meminimalkan perbedaan antara nilai yang diprediksi dan nilai sebenarnya.
4. Setelah pelatihan selesai, model dapat digunakan untuk memprediksi nilai target berdasarkan fitur input (misalnya, `X_train`). Prediksi ini dihitung berdasarkan persamaan linier yang ditemukan selama pelatihan.
5. Setelah prediksi dilakukan, model dievaluasi dengan menghitung Mean Squared Error (MSE) yang mengukur seberapa besar perbedaan antara prediksi model dan nilai target sebenarnya.

|Kelebihan | Kekurangan |
| ------ | ------ |
| - Mudah dipahami dan cepat. | - Tidak efektif untuk data non-linear.
| - Memberikan interpretasi yang jelas tentang hubungan antara fitur dan target. | - Rentan terhadap outliers.

Parameter
- Tidak ada parameter tambahan yang diberi nilai dalam kode untuk model Linear Regression.

### Decision Tree
Decision Tree adalah algoritma pembelajaran mesin yang digunakan untuk klasifikasi dan regresi. Model ini membangun struktur seperti pohon yang membuat keputusan berdasarkan serangkaian aturan yang diperoleh dari data. Setiap cabang pohon mewakili keputusan berdasarkan fitur tertentu, dan setiap daun mewakili nilai prediksi atau keputusan akhir. Berikut adalah cara kerja dari model ini.
1. Model `DecisionTreeRegressor` diinisialisasi dengan parameter seperti `max_depth` yang membatasi kedalaman decision tree dan `random_state` untuk memastikan hasil yang dapat direproduksi.
2. Model dilatih menggunakan data pelatihan yang terdiri dari fitur (`X_train`) dan target/label (`y_train`). Selama pelatihan, model membangun struktur decision tree.
3. Model membagi dataset ke dalam subset yang lebih kecil dengan memilih fitur dan nilai terbaik untuk membagi data pada setiap node pohon. Proses ini terus berlanjut hingga tercapai kedalaman maksimum yang telah ditentukan (`max_depth`) atau sampai pembagian data tidak lagi memberikan peningkatan dalam model.
4. Setelah decision tree dibangun, model dapat digunakan untuk memprediksi nilai target untuk data baru. Model mengarahkan data melalui cabang pohon berdasarkan nilai fitur yang ada, dan sampai pada daun yang memberikan nilai prediksi.
5. Setelah prediksi dilakukan, model dievaluasi dengan menghitung Mean Squared Error (MSE), yang mengukur perbedaan antara prediksi model dan nilai target sebenarnya.

|Kelebihan | Kekurangan |
| ------ | ------ |
| - Mudah dipahami dan diinterpretasikan. | - Rentan terhadap overfitting, terutama jika pohon terlalu dalam.
| - Dapat menangani data numerik dan kategorikal. | - Kurang stabil, perubahan kecil pada data dapat menghasilkan pohon yang berbeda.

Parameter
- `max_depth = 16`, seperti pada Random Forest, parameter ini membatasi kedalaman decision trees hingga 16 level.
- `random_state = 55`, sama seperti pada Boosting, parameter ini mengontrol aspek acak dalam pembuatan decision trees, sehingga hasilnya bisa direplikasi di masa depan.

# Evaluation
Metrik yang akan digunakan pada evaluasi ini adalah MSE atau Mean Squared Error yang menghitung jumlah selisih kuadrat rata-rata nilai sebenarnya dengan nilai prediksi. MSE pada kasus ini digunakan untuk mengevaluasi kinerja lima model regresi yang diterapkan pada data temperatur.

**Formula MSE**

<img src="https://github.com/user-attachments/assets/eebc4db3-c3e1-481f-9c9b-2de83e1eb686" alt="Formula MSE" width="300">

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

Berikut adalah hasil evaluasi terhadap Business Understanding.

**Problem Statement**
1. Model yang telah dibangun seperti Random Forest (RF) menunjukkan prediksi paling akurat yang dapat memberikan wawasan tentang pola-pola temperatur yang mungkin dipengaruhi oleh polutan seperti CO, NOx, dan O3. Hasil ini bisa digunakan sebagai dasar untuk melakukan analisis lebih lanjut mengenai hubungan antara polutan dengan suhu dan kualitas udara.
2. Model regresi yang dievaluasi seperti Random Forest dan Decision Tree memberikan prediksi suhu yang cukup akurat dan ini berkaitan langsung dengan pemahaman faktor-faktor yang mempengaruhi suhu. Metrik MSE yang kecil pada model Random Forest menunjukkan bahwa model dapat memberikan prediksi suhu yang lebih baik yang sangat relevan dengan upaya mengidentifikasi faktor-faktor yang mempengaruhi suhu. Oleh karena itu, model ini membantu dalam memahami faktor-faktor yang perlu diperhatikan dalam perencanaan kebijakan untuk mitigasi suhu dan polusi.

**Goals**
1. Visualisasi data seperti heatmaps dan pair plots yang digunakan dalam analisis dapat membantu memahami hubungan antar variabel. Hal ini bisa memberikan gambaran yang lebih jelas tentang bagaimana masing-masing polutan berkontribusi terhadap kualitas udara.
2. Random Forest memberikan gambaran yang lebih jelas mengenai faktor-faktor yang mempengaruhi suhu dengan MSE yang rendah. Ini menunjukkan bahwa model tersebut dapat memberikan informasi yang berguna dalam perencanaan kebijakan lingkungan, karena hasil prediksi yang lebih akurat memungkinkan pembuat kebijakan untuk mengidentifikasi variabel yang berkontribusi besar terhadap peningkatan suhu dan polusi udara.

**Solution Statements**
1. Solusi berupa penggunaan visualisasi data seperti heatmaps dan pair plots akan sangat berguna untuk menggambarkan pola-pola antara polutan dan variabel lain yang mempengaruhi kualitas udara. Hasil evaluasi model, terutama Random Forest, yang menunjukkan prediksi yang akurat, dapat memperkuat visualisasi tersebut dengan memberikan data yang lebih terpercaya untuk dianalisis.
2. Penggunaan MSE untuk mengevaluasi faktor-faktor yang mempengaruhi suhu telah terbukti efektif, terutama dengan model Random Forest yang menghasilkan nilai MSE terendah. Ini menunjukkan bahwa solusi yang direncanakan berdampak dalam memberikan prediksi suhu yang lebih akurat, yang dapat digunakan dalam perencanaan kebijakan lingkungan dan pengendalian polusi. 

[Billions of People Still Breathe Unhealthy Air]: <https://www.who.int/news/item/04-04-2022-billions-of-people-still-breathe-unhealthy-air-new-who-data>
[Air-Quality]: <https://www.kaggle.com/datasets/citrahsagala/airquality>
[citrahsagala]: <https://www.kaggle.com/citrahsagala>
