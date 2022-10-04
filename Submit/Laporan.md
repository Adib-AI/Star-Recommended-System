# Project Overview

Menurut Sanjoyo (2010), sistem rekomendasi adalah sistem yang bertujuan untuk memperkirakan informasi yang menarik bagi pengguna dan juga membantu user dalam menentukan pilihannya [[1]](https://jursistekni.nusaputra.ac.id/article/download/63/38/). Sistem rekomendasi bisa menjadi sebuah solusi dalam peningkatan peluang khususnya dalam dunia bisnis. Menurut CNBC tahun 2016-2018 menyatakan peningkatan sepatu sneakers mencapai 50-70% [[2]](https://openlibrarypublications.telkomuniversity.ac.id/index.php/engineering/article/download/18073/17702), dari peningkatan tersebut banyak konsumen bingung memilih jenis sneakers apa yang cocok baginya. Disinilah peran sistem rekomendasi sebagai sang "pelayan ajaib", dengan bantuan teknologi yang memumpuni konsumen dapat mudah mengetahui jenis sneakers yang baik baginya dan sang perusahaan dapat memberikan pelayanan serta peningkatan bisnis. 

Sistem rekomendasi sangat berguna dalam kehidupan sehari-hari dan pada penelitian ini berusaha untuk memberikan rekomendasi nama planet berdasarkan namanya. Hal ini dasarkan membantu meningkatkan minat rakyat Indonesia terhadap dunia astronomi

# Business Understanding

**Pada pernyataan yang telah dijelaskan, sehingga masalah yang diangkat adalah**
- Bagaimana implemntasi sistem rekomendasi berbasis *content based filtering?*
- Bagaimana kemampuan content based filtering dalam memberikan rekomendasi?

**Tujuan dari masalah yang diangkat adalah**
- Mengetahui cara implementasi sistem rekomendasi berbasis *content based filtering*
- Mengetahui kemampuan *content based filtering* dalam melakukan rekomendasi

**Solusi Statements**

Solusi yang dapat dilakukan
- Menggunakan library seaborns sklearn
- Menggunakan cosine similarity
- Menggunakan pandas dan numpy
- Menggunakan precision sebagai evaluasi

# Data Understanding


Dataset yang digunakan pada penelitian ini adalah dataset astronomi tentang planet yang didapatkan dari [Kaggle](https://www.kaggle.com/datasets/amit1235813/gaia-astronomical-data). Adapun kolom-kolom pada dataset ini, antara lain:
- type : tipe-tipe dari planet yang tersedia
- name : nama dari planet-planet
- glon : Foto pengguna
- glat : Lamanya Session pengguna pada sistem yang tercatat
- distance (parsecs) : Lamanya penggunaan aplikasi perusahaan oleh pengguna
- x (parsecs)  
- y (parsecs)
- z (parsecs)
- radius (parsecs)
- log10 age (years)
- Arm (masers)
- Source : Sumber perhitungan.

Note : parsecs adalah satuan jarak tertua dimana perhitungan tersebut memanfaatkan trigonometri dengan bumi sebagai titik awal sudutnya. Sehingga, x, y, z dan radius merupakan perhitungan trigono "mentahannya"

Pada kolom diatas, **kolom** yang digunakan adalah kolom 'type','name', 'distance (parsecs)' dengan name sebagai kolom yang sebagai yang akan direkomendasi dengan ukuran data 2557 baris dan 12 kolom


Tahapan yang dilakukan untuk memahami data adalah.
- Pemilihan kolom dan cek nilai null pada kolom yang dipilih dengan pandas

# Data Preparation

### Univariate Exploratory


```python
os = 'G:\Kumpulan Dataset\Astronomi'

star = pd.read_csv(os+'/map_object_list.csv')
```


```python
star
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>type</th>
      <th>name</th>
      <th>glon</th>
      <th>glat</th>
      <th>distance (parsecs)</th>
      <th>x (parsecs)</th>
      <th>y (parsecs)</th>
      <th>z (parsecs)</th>
      <th>radius (parsecs)</th>
      <th>log10 age (years)</th>
      <th>Arm (masers)</th>
      <th>Source</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>maser</td>
      <td>G351.44+00.65</td>
      <td>351.440000</td>
      <td>0.650000</td>
      <td>1329.000000</td>
      <td>1314.111083</td>
      <td>-197.802309</td>
      <td>15.076703</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>Sgr</td>
      <td>2019ApJ...874...94W</td>
    </tr>
    <tr>
      <th>1</th>
      <td>maser</td>
      <td>G011.49-01.48</td>
      <td>11.490000</td>
      <td>-1.480000</td>
      <td>1250.000000</td>
      <td>1224.540716</td>
      <td>248.913063</td>
      <td>-32.285001</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>Sgr</td>
      <td>2019ApJ...874...94W</td>
    </tr>
    <tr>
      <th>2</th>
      <td>maser</td>
      <td>G014.33-00.64</td>
      <td>14.330000</td>
      <td>-0.640000</td>
      <td>1119.000000</td>
      <td>1084.116100</td>
      <td>276.942332</td>
      <td>-12.499090</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>Sgr</td>
      <td>2019ApJ...874...94W</td>
    </tr>
    <tr>
      <th>3</th>
      <td>maser</td>
      <td>G014.63-00.57</td>
      <td>14.630000</td>
      <td>-0.570000</td>
      <td>1831.000000</td>
      <td>1771.545918</td>
      <td>462.443798</td>
      <td>-18.215177</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>Sgr</td>
      <td>2019ApJ...874...94W</td>
    </tr>
    <tr>
      <th>4</th>
      <td>maser</td>
      <td>G015.03-00.67</td>
      <td>15.030000</td>
      <td>-0.670000</td>
      <td>2004.000000</td>
      <td>1935.311186</td>
      <td>519.651302</td>
      <td>-23.433653</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>Sgr</td>
      <td>2019ApJ...874...94W</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>2552</th>
      <td>ob association</td>
      <td>SCO OB1</td>
      <td>343.464464</td>
      <td>1.389996</td>
      <td>1529.261420</td>
      <td>1466.016362</td>
      <td>-435.243053</td>
      <td>37.107179</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>1978ApJS...38..309H</td>
    </tr>
    <tr>
      <th>2553</th>
      <td>ob association</td>
      <td>HD 156154</td>
      <td>351.196497</td>
      <td>1.369037</td>
      <td>1489.704232</td>
      <td>1472.154067</td>
      <td>-227.993641</td>
      <td>35.602076</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>1978ApJS...38..309H</td>
    </tr>
    <tr>
      <th>2554</th>
      <td>ob association</td>
      <td>SCO OB4</td>
      <td>352.465040</td>
      <td>3.119684</td>
      <td>1128.317216</td>
      <td>1118.574236</td>
      <td>-147.957489</td>
      <td>61.496259</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>1978ApJS...38..309H</td>
    </tr>
    <tr>
      <th>2555</th>
      <td>ob association</td>
      <td>R 105</td>
      <td>332.997923</td>
      <td>1.851210</td>
      <td>2433.451109</td>
      <td>2168.180764</td>
      <td>-1104.842284</td>
      <td>78.651451</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>1978ApJS...38..309H</td>
    </tr>
    <tr>
      <th>2556</th>
      <td>ob association</td>
      <td>SCO OB2</td>
      <td>352.812175</td>
      <td>20.187286</td>
      <td>118.045824</td>
      <td>117.118139</td>
      <td>-14.770179</td>
      <td>43.402669</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>1978ApJS...38..309H</td>
    </tr>
  </tbody>
</table>
<p>2557 rows × 12 columns</p>
</div>




```python
star.isna().sum()
```




    type                  0
    name                  0
    distance (parsecs)    0
    dtype: int64



Data tidak memiliki data NaN dari 2557 data yang tersedia.

Setelah mengubah data dari list (dengan setiap panjang data ialah 2557) akan dimasukkan kedalam dataframe dalam bentuk dictionary dengan variable "astronom"


```python
print(len(typee))
print(len(name))
print(len(distance))
```

    2557
    2557
    2557
    


```python
astronom
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>type</th>
      <th>name</th>
      <th>distance</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>maser</td>
      <td>G351.44+00.65</td>
      <td>1329.000000</td>
    </tr>
    <tr>
      <th>1</th>
      <td>maser</td>
      <td>G011.49-01.48</td>
      <td>1250.000000</td>
    </tr>
    <tr>
      <th>2</th>
      <td>maser</td>
      <td>G014.33-00.64</td>
      <td>1119.000000</td>
    </tr>
    <tr>
      <th>3</th>
      <td>maser</td>
      <td>G014.63-00.57</td>
      <td>1831.000000</td>
    </tr>
    <tr>
      <th>4</th>
      <td>maser</td>
      <td>G015.03-00.67</td>
      <td>2004.000000</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>2552</th>
      <td>ob association</td>
      <td>SCO OB1</td>
      <td>1529.261420</td>
    </tr>
    <tr>
      <th>2553</th>
      <td>ob association</td>
      <td>HD 156154</td>
      <td>1489.704232</td>
    </tr>
    <tr>
      <th>2554</th>
      <td>ob association</td>
      <td>SCO OB4</td>
      <td>1128.317216</td>
    </tr>
    <tr>
      <th>2555</th>
      <td>ob association</td>
      <td>R 105</td>
      <td>2433.451109</td>
    </tr>
    <tr>
      <th>2556</th>
      <td>ob association</td>
      <td>SCO OB2</td>
      <td>118.045824</td>
    </tr>
  </tbody>
</table>
<p>2557 rows × 3 columns</p>
</div>



Disini akan melakukan **TF-IDF** untuk menghitung bobot dari setiap tipe menggunakan library sklearn


```python
from sklearn.feature_extraction.text import TfidfVectorizer
```

Membuat variable baru dengan nama data yang menyimpan dataframe sebelumnya dan variable **tf** sebagai fungsi TF-IDF

Melakukan extract dan get feature dari tipe planet yang ada pada data


['association', 'cluster', 'hii', 'maser', 'ob', 'open', 'region']


Setelah melakukan get feature yang tersedia, maka ditransformasikan menjadi kolom dan apabila di shape akan mendapatkan menjadi 2557 baris dan 7 kolom


```python
pd.DataFrame(
            tfidf_matrix.todense(),
            columns=tf.get_feature_names(),
            index = data.name
            )
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>association</th>
      <th>cluster</th>
      <th>hii</th>
      <th>maser</th>
      <th>ob</th>
      <th>open</th>
      <th>region</th>
    </tr>
    <tr>
      <th>name</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>G351.44+00.65</th>
      <td>0.000000</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>0.000000</td>
      <td>0.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>G011.49-01.48</th>
      <td>0.000000</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>0.000000</td>
      <td>0.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>G014.33-00.64</th>
      <td>0.000000</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>0.000000</td>
      <td>0.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>G014.63-00.57</th>
      <td>0.000000</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>0.000000</td>
      <td>0.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>G015.03-00.67</th>
      <td>0.000000</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>0.000000</td>
      <td>0.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>SCO OB1</th>
      <td>0.707107</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.707107</td>
      <td>0.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>HD 156154</th>
      <td>0.707107</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.707107</td>
      <td>0.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>SCO OB4</th>
      <td>0.707107</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.707107</td>
      <td>0.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>R 105</th>
      <td>0.707107</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.707107</td>
      <td>0.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>SCO OB2</th>
      <td>0.707107</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.707107</td>
      <td>0.0</td>
      <td>0.0</td>
    </tr>
  </tbody>
</table>
<p>2557 rows × 7 columns</p>
</div>



Setelah melakukan extract fitur dan melakukan transform, selanjutnya akan dihitung cosine similarity nya. Nah ini lah tahapan bagaimana model akan menjadi "Pelayan Ajaib". Fungsi ini digunakan untuk menghitung kemiripan antar data, semakin mendekati 1 maka data tersebut semakin mirip dan sebaliknya. 

Fungsi cosine similarity yang digunakan disini berasala dari sklearn dan hasil tersebut akan dibuatkan data frame dengan :
 - kolom sebagai nama planet
 - baris sebagai nama planet

Hal ini dikarenakan memetakan data untuk menghitung kemiripan antar nama planet


```python
cosine_sim_df = pd.DataFrame(cosine_sim, columns = data['name'], index = data['name'])
print('Shape:', cosine_sim_df.shape)
```

    Shape: (2557, 2557)
    


```python
cosine_sim_df.sample(10, axis=1).sample(5, axis=0)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th>name</th>
      <th>UBC 219</th>
      <th>UPK_642</th>
      <th>UPK_418</th>
      <th>ASCC_21</th>
      <th>FSR_0282</th>
      <th>G049.48-00.38</th>
      <th>Berkeley_36</th>
      <th>NGC_7128</th>
      <th>Berkeley_5</th>
      <th>Ruprecht_79</th>
    </tr>
    <tr>
      <th>name</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>UBC 119</th>
      <td>1.0</td>
      <td>1.0</td>
      <td>1.0</td>
      <td>1.0</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>1.0</td>
      <td>1.0</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>UBC 580</th>
      <td>1.0</td>
      <td>1.0</td>
      <td>1.0</td>
      <td>1.0</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>1.0</td>
      <td>1.0</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>G122.01-07.08</th>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>UBC 135</th>
      <td>1.0</td>
      <td>1.0</td>
      <td>1.0</td>
      <td>1.0</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>1.0</td>
      <td>1.0</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>G208.99-19.38</th>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
    </tr>
  </tbody>
</table>
</div>



Hasil diatas dapat dilihat bahwa data memiliki tingkat kemiripan yang tinggi. 

Contoh UBC 119 memiliki tingkat kemiripan antara lain UPK_642, UBC 219, NGC_7218. Tetapi dengan G049.48-00.38 tingkat kemiripannya adalah 0 (nol)

# Modeling and Results

## Modeling 


```python
def planet_recommendations(name, similarity_data=cosine_sim_df, items= data[['name', 'type', 'distance']], k=3):
    index = similarity_data.loc[:,name].to_numpy().argpartition(
        range(-1, -k, -1))
    
    closest = similarity_data.columns[index[-1:-(k+2):-1]]
    
    closest = closest.drop(name, errors='ignore')
    
    return pd.DataFrame(closest).merge(items).tail(3)
```

Modelling diatas bekerja dengan memanfaatkan hasil perhitungan cosine similarity dengan pengambilan data terakhir hal tersebut dikarenakan dengan fungsi *tail* akan mengambil data terakhir dari hasil dataframe
Kurang lebih alur model tersebut sebagai berikut :
1. Membuat parameter name, similiratiy_data (berisi dataframe cosine_sim_df), items = dataframe tanpa cosine, dan k (sebagai pengambil 3 data) yang parameter-parameter ini dibalut dengan fungsi.
2. Cari similarity dengan kata kunci name yang diinputkan dengan bantuan fungsi argpartition dengan mengambil index data yang sama
3. Setelah didapatkan, akan diambil kolom-kolom tersebut
4. Untuk mencegah data yang kita cari tetap muncul, maka data dengan "name" (sebagai input) akan di drop
5. kembalikan data dalam bentuk dataframe

## Results 

![ab](https://github.com/Adib-AI/Data_Science/blob/main/Recom_System/data_eq.PNG?raw=True)

![result](https://github.com/Adib-AI/Data_Science/blob/main/Recom_System/result.PNG?raw=True)

# Evalution

Matrik evaluasi yang digunakan disini adalah presisi. Berdasarkan penelitian yang dilakukan oleh Nastiti, Putri [[3]](https://www.researchgate.net/publication/334320752_Penerapan_Metode_Content_Based_Filtering_Dalam_Implementasi_Sistem_Rekomendasi_Tanaman_Pangan/fulltext/5d248983458515c11c1f7ab8/Penerapan-Metode-Content-Based-Filtering-Dalam-Implementasi-Sistem-Rekomendasi-Tanaman-Pangan.pdf?origin=publication_detail) yang membahas sistem rekomendasi contetnt based filtering dalam tanaman pangan menyatakan hasil model yang dibuat akan dievaluasi dengan metrik presisi. Dengan penelitian yang sama, presisi adalah teknik perbandingan hasil rekomendasi dengan teknik sebenarnya. Presisi merupakan salah satu tahapan evaluasi dalam *confusion matrix*. Evaluasi pada confusion matrix yang sering digunakan adalah accuracy, precision, recall
![formula](https://github.com/Adib-AI/Data_Science/blob/main/Recom_System/formula.jpg?raw=True)

Pada hasil rekomendasi, tidak diketahui TP, TN, FP, FN. Nah disini saya membuat sebuah relevant yang bersumber dari [[4]](https://towardsdatascience.com/recommendation-systems-models-and-evaluation-84944a84fb8e) sehingga formula yang didapatkan ialah seperti berikut
![tp_tn_fp_fn_coding](https://github.com/Adib-AI/Data_Science/blob/main/Recom_System/tp_tn_fp_fn_ala_recom.PNG?raw=True)
![formula_coding](https://github.com/Adib-AI/Data_Science/blob/main/Recom_System/formula_acc_preci_recall.PNG?raw=True)

Hasil rekomendasi dapat dilihat bahwa tipe perhitungan dengan open cluster yang sama dengan UBC 119 adalah 10 data dari ke 10 data. Hal ini dapat dilakukan perhitungan bahwasanya hasil akurasi, precisi, rekal dan ialah 100%. Perhitungan dapat dilihat dibawah ini
![result](https://github.com/Adib-AI/Data_Science/blob/main/Recom_System/result_acc_precisisi_recall.PNG?raw=True)


Jika dilakukan perhitungan manual, diilustrasikan seperti dibawah ini
![hasil_perhitungan_presisi](https://github.com/Adib-AI/Data_Science/blob/main/Recom_System/hasil_perhitungan_presisi.PNG?raw=True)

Note: Dikali 100% untuk mendapatkan hasil dalam bentuk % (persen)
