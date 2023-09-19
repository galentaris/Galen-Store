# Galen Store

#### Nama : Galen Taris Bariqi
#### NPM : 2206029052
#### Kelas : PBP C


#### TUGAS 2

Link Adaptable : https://galenstore.adaptable.app/main/

<details>
<summary>
1. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
</summary>

- Membuat sebuah proyek Django baru.

Seperti yang sudah diajarkan saat tutorial 0 kemarin, saya harus membuat repositori public di github yang terhubung dengan repositori lokal di laptop. Repositori lokal tersebut berisi proyek aplikasi yang dibuat pada tugas 2 ini. Untuk membuat direktori tersebut, kita harus menggunakan beberapa command seperti :
    1. ``git init`` : Menginisiasi di direktori yang sudah dibuat dan akan membuat repositori kosong di direktori tersebut
    2. ``python -m venv env`` : Membuat virtual environment (env)
    3. ``env\Scripts\activate.bat`` : Mengaktivasi env tersebut yang akan berguna sebagai *dependecies* dari aplikasi.
    Kemudian membuat berkas requirements.txt saat env sedang aktif yang berisi beberapa *dependecies*
    4. ``pip install -r requirements.txt`` : Menjalankan *dependecies* yang sudah dimasukkan ke dalam berkas requirements.txt
    5. ``django-admin startproject galen_store .`` : Membuat proyek Django dengan nama "galen_store"

Untuk memberikan izin pada semua host dalam mengakses aplikasi web, kita harus menambahkan ``"*"`` dalam ``ALLOWED_HOSTS``. Dan yang terakhir adalah membuat berkas ``.gitignore`` dan diisi dengan text pada tutorial 0. Berkas tersebut berguna untuk mengabaikan beberapa berkas yang harus diabaikan oleh git agar tidak ter-push.

- Membuat aplikasi dengan nama main pada proyek tersebut.

Langkah selanjutnya adalah membuat direktori bernama main dalam proyek aplikasi Tugas 2 ini dengan menjalankan perintah ``python manage.py startapp main``. Kemudian menambahkan ``'main'`` ke dalam ``INSTALLED_APPS`` di ``settings.py`` direktori galen_store.

- Melakukan routing pada proyek agar dapat menjalankan aplikasi main.

Di tahap ini, saya membuat berkas urls.py untuk mendefinisikan rute URL. Kemudian, pada file urls.py yang di direktori galen_store, saya menambahkan fungsi include dari django.urls untuk mengimpor rute URL dari aplikasi lain. Setelah itu, saya menambahkan path ``'main/'`` ke dalam urls.py yang berada di direktori galen_store.

- Membuat model pada aplikasi main dengan nama Item dan memiliki atribut wajib sebagai berikut.
    1. name sebagai nama item dengan tipe CharField.
    2. amount sebagai jumlah item dengan tipe IntegerField.
    3. description sebagai deskripsi item dengan tipe TextField.

Saya membuat model-model pada aplikasi main dengan ketentuan di atas pada berkas models.py dengan meng-import class models dari django.db dan kemudian model tersebut dimigrasi untuk mengubah struktur tabel basis data sesuai perubahan yang saya lakukan. Untuk membuat migrasi model, saya menjalankan perintah ``python manage.py makemigrations`` dan menerapkan ke basis data lokal dengan ``python manage.py migrate``. 

- Membuat sebuah fungsi pada views.py untuk dikembalikan ke dalam sebuah template HTML yang menampilkan nama aplikasi serta nama dan kelas kamu.

Pertama-tama, saya mengimpor render dari django.shortcuts dengan perintah from django.shortcuts import render yang berguna untuk melakukan rendering pada tampilan HTML memakai data yang saya masukkan di file views.py. Saya membuat fungsi show_main pada berkas tersebut yang berisikan sebuah context berupa nama aplikasi, nama lengkap, serta kelas saya. Dan yang terakhir, saya melakukan return terhadap fungsi tersebut berupa ``return render(request, "main.html", context)`` agar data-data yang sudah saya masukkan dapat ditampilkan HTML-nya pada web server.

- Membuat sebuah routing pada urls.py aplikasi main untuk memetakan fungsi yang telah dibuat pada views.py.

Dari berkas urls.py pada direktori main yang sudah dibuat sebelumnya, saya meng-import fungsi show_main tersebut agar path yang mengarahkan ke fungsi tersebut bisa dimasukkan ke urlspattern di berkas tersebut.

- Melakukan deployment ke Adaptable terhadap aplikasi yang sudah dibuat sehingga nantinya dapat diakses oleh teman-temanmu melalui Internet.

Langkah terakhir setelah semua step di atas dilakukan adalah melakukan commit dan push ke repositori git yang dibuat sebelumnya. Pertama melakukan command ``git add .`` untuk menandai semua berkas yang akan di track. Kemudian melakukan perintah ``git commit -m "KOMENTAR"`` untuk meng-commit dengan pesan sesuai perubahan yang saya lakukan. Lalu, saya menjalankan perintah ``git remote add origin "URL_REPO"`` untuk menghubungkan repositori lokal dengan repositori yang ada di git. Dan yang terakhir melakukan perintah ``git push -u origin main`` untuk mengirim semua perubahan yang dilakukan ke branch main di repositori git.

</details>

<details>
<summary>
2. Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.
</summary>

![Alt Text](Bagan_Nomor_2.png)

Untuk kaitan antara berkas, urutan proses langkahnya sebagai berikut :
    1. User me-request permintaan berupa HTTP aplikasi main.html melalui web browser.
    2. urls.py akan menentukan URL dan view mana yang sesuai dengan request dari user.
    3. views.py akan menghandle request dari user sehingga menampilan main.html
    4. Di saat yang bersamaan, views.py menggunakan model yang telah didefinisikan pada models.py untuk memanipulasi data yang diperlukan sehingga dapat merender page yang diinginkan user.
</details>


<details>
<summary>
3. Jelaskan mengapa kita menggunakan virtual environment? Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment?
</summary>

Virtual Environment (env) itu berguna untuk mengisolasi package dan dependacies yang diinginkan oleh developer sehingga tidak saling bertabrakan dengan konfigurasi proyek-proyek versi lain. *Dependecies* merupakan modul yang yang diperlukan suatu software agar dapat berfungsi termasuk library, framework, atau package dan tiap proyek tersebut pasti memiliki *dependecies* yang berbeda. Selain itu, virtual environment juga memudahkan developer untuk me-manage *dependecies* dengan menginstall dan menghapus modul-modul Python menggunakan pip. Hal tersebut memudahkan developer dalam mengembangkan proyek yang memerlukan banyak *dependecies*. Virtual environment juga membantu untuk mengurangi risiko terinstall modul-modul yang tidak terpercaya.

Tanpa virtual environment, kita dapat tetap membuat aplikasi web berbasis django, tetapi hal tersebut tidak disarankan karena dependencies proyek secara global di Python mungkin terinstall dan akan menyebabkan konflik antar proyek sehingga sulit dikelola. Penggunaan virtual environment merupakan praktik terbaik dalam mengembangkan aplikasi web berbasis django untuk menghindari masalah dependencies sehingga isolasi antar proyek dapat terjadi. 
</details>

<details>
<summary>
4. Jelaskan apakah itu MVC, MVT, MVVM dan perbedaan dari ketiganya.
</summary>

##### MVC (Model View Controller)
Model = mengelola data dan mengembalikan operasi berupa logic data kepada controller.
View = tampilan yang digunakan untuk menampilkan data dan menerima input dari pengguna.
Controller = mengambil input dari View dan berinteraksi dengan Model untuk memproses data dan diperbarui tampilannya.

MVC adalah pola desain arsitektur pada software yang digunakan untuk mengorganisir suatu kode dalam aplikasi agar pengguna memungkinkan untuk mengelola dan memodifikasinya secara independen. 

##### MVT (Model View Template)
Model = mengelola data dan mengembalikan operasi berupa logic data kepada controller.
View = mengatur tampilan data kepada pengguna.
Template = menentukan tampilan dari data yang disediakan oleh model berupa HTML.

MVT adalah pola desain arsitektur pada software yang terutama dikaitkan dengan kerangka kerja web Django. Template pada MVT berfungsi untuk memisahkan logika tampilan dan logika aplikasi agar developer dapat fokus mengembangkan tampilan tanpa menghiraukan detail logika data pada pemrosesan HTTP.

##### MVVM (Model View View Model)
Model = mengelola data dan mengembalikan operasi berupa logic data kepada controller.
View = mengatur tampilan data kepada pengguna.
ViewModel = mengkonversi data dari model sehingga dapat sesuai dengan tampilan yang diinginkan oleh View.

MVVM adalah pola desain arsitektur pada software yang umumnya digunakan untuk pengembangan dalam aplikasi yang berbasis GUI. MVVM ini berfokus pada pengembangan aplikasi yang punya tampilan kompleks sehingga perlu untuk memisahkan logika tampilan dari logika bisnis.

Intinya penggunaan dari masing-masing pola desain diatas tergantung pada teknologi yang digunakan dan kebutuhan proyek oleh developer. 

</details>

#### TUGAS 3

<details>
<summary>
1. Apa perbedaan antara form POST dan form GET dalam Django?
</summary>

form POST:
- Cara Pengiriman Data
Data yang dikirim dan di*request* oleh user dalam bentuk permintaan HTTP sehingga tidak terlihat di URL. Cocok untuk mengirim berbagai data sensitif seperti *password*.
- Tipe Data yang dapat dikirim
Digunakan untuk mengirim berbagai jenis data, termasuk .txt, .jpg, dll dengan kapasitas yang besar.
- Dari segi User
User lebih sulit untuk menjadikan URL-nya sebagai bookmark karena parameternya tidak pada URL.

form GET:
- Cara Pengiriman Data
Data yang dikirim dalam bentuk parameter dalam URL sehingga data dapat lebih mudah terlihat di URL. Cocok untuk data yang tidak punya dampak apabila dipanggil berulang kali.
- Tipe Data yang dapat dikirim
Digunakan untuk mengirim jenis data yang sederhana dengan kapasitas yang lebih kecil.
- Dari segi User
User dapat dengan mudah untuk menjadikan URL-nya sebagai bookmark karena parameternya ada pada URL.

</details>

<details>
<summary>
2. Apa perbedaan utama antara XML, JSON, dan HTML dalam konteks pengiriman data?
</summary>

- XML
XML mampu mendefinisikan struktur data yang kompleks dengan fleksibel untuk melakukan pertukaran data antar sistem yang beda karena sintaksnya yang cukup kaya dan ketat. Selain untuk menukar data, XML digunakan juga untuk mengkonfigurasi data dan menyimpan data.

- JSON
Tujuan utama dari JSON sama seperti XML yaitu sebagai format pertukaran data yang lebih ringkas sehingga lebih sering digunakan untuk mengirim data server ke browser dan juga sebaliknya. Dengan sintaksnya yang sederhana, JSON lebih mudah dibaca oleh *human* dan ukuran filenya lebih kecil jika dibandingkan dengan XML.

- HTML
Berbeda dengan XML dan JSON, HTML berfokus untuk mengatur tampilan pada halaman web dan mengatur elemen-elemen yang dipakai sehingga web tersebut dapat diakses di browser dan menampilkan berbagai informasi kepada *user*. 

</details>

<details>
<summary>
3. Mengapa JSON sering digunakan dalam pertukaran data antara aplikasi web modern?
</summary>

Pada era web modern ini, tentunya dibutuhkan kecepatan pengiriman data yang tinggi. Dengan sintaksnya yang sederhana, JSON memiliki beberapa keunggulan : 

a. Sintaksnya sederhana
Dengan kesederhanaan sintaks JSON, dapat memudahkan pengguna dan developer untuk memahami dan membaca struktur data yang telah melalui proses pertukaran data.

b. Ukuran file yang kecil
JSON mengirim data dengan ukuran file yang kecil sehingga dapat mempercepatan proses pertukaran data melalui jaringan agar web bisa lebih responsif. 

c. Penggunaan bahasa pemrograman yang fleksibel
JSON dapat digunakan dengan hampir seluruh bahasa pemrograman sehingga memudahkan developer untuk mengembangkan sebuah web.

d. Didukung oleh penggunaan JavaScript
Memudahkan komunikasi dengan server JSON tanpa melakukan banyak konversi

e. Memudahkan Deserialization
Developer dapat dengan mudah mengubah data menjadi data sesuai dengan bahasa pemrograman yang digunakan tanpa memerlukan kode yang banyak.

</details>

<details>
<summary>
4. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
</summary>

- Membuat input form untuk menambahkan objek model pada app sebelumnya.

Sebelum membuat form untuk menambahkan product pada aplikasi, saya membuat folder ``templates`` pada ``root folder`` dan membuat berkas ``base.html`` sebagai kerangka umum halaman web lainnya pada aplikasi Galen Store. Kemudian saya melakukan beberapa *adjust* agar ``main.html`` yang dibuat pada tugas 2 kemarin bisa terhubung. 

Lalu, pada direktori ``main``, saya membuat berkas ``forms.py`` untuk membuat struktur form yang bisa menerima input data pada halaman web. Saya menambahkan kode berikut ini pada forms.py
```
from django.forms import ModelForm
from main.models import Product

class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ["name", "price", "amount", "description"]
```

Pada list fields tersebut, saya memasukkan name, price, amount, dan description. Sedangkan untuk date_added akan diinput secara otomatis.

Kemudian saya mengimport beberapa library yang dibutuhkan dan membuat fungsi create_product pada berkas ``views.py``. Fungsi tersebut dibuat untuk melakukan penambahan data secara otomatis ketika dari ``forms.py`` ada data yang disubmit. Tidak lupa juga, setelah saya membuat fungsi create_product, saya menambahkan path url ke ``urlpatterns`` pada ``urls.py`` di main.

Dan pada fungsi show_main dari tugas 2 kemarin, saya menambahkan kode 
```
products = Product.objects.all()
```
Kode diatas berguna untuk mengambil semua object Product pada database.

Kemudian untuk menampilkan fungsi create_product yang sudah dibuat sebelumnya, saya membuat berkas baru bernama ``create_product.html`` pada direktori ``main/templates``. Saya melakukan beberapa adjusting terhadap berkas ``create_product.html`` dan ``main.html`` sehingga tampilannya sesuai apa yang saya harapkan.

- Tambahkan 5 fungsi views untuk melihat objek yang sudah ditambahkan dalam format HTML, XML, JSON, XML by ID, dan JSON by ID.

Kemudian, tahap selanjutnya saya membuat 4 fungsi yang berguna untuk melihat data-data yang sudah diinput oleh user pada web. Data-data tersebut dapat dilihat dengan format yang beragam seperti HTML, XML, dan JSON. 

4 fungsi tersebut bernama show_xml, show_json, show_xml_by_id, dan show_json_by_id. Tiap fungsi tersebut ditambahkan return function berupa ``HttpResponse`` yang sudah di serealize menjadi bahasa pemrograman yang sesuai.

Berikut kode yang saya buat terhadap 4 fungsi tersebut : 
```
def show_xml(request):
    data = Product.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = Product.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml_by_id(request, id):
    data = Product.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json_by_id(request, id):
    data = Product.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")
```
- Membuat routing URL untuk masing-masing views yang telah ditambahkan pada poin 2.

Agar fungsi yang sudah dibuat tadi dapat diakses, saya menambahkan path url masing-masing fungsi di atas ke ``urls.py`` pada folder ``main``. Berikut kode penambahan path yang saya tambahkan.
```
...
path('xml/', show_xml, name='show_xml'),
path('json/', show_json, name='show_json'), 
path('xml/<int:id>/', show_xml_by_id, name='show_xml_by_id'),
path('json/<int:id>/', show_json_by_id, name='show_json_by_id'), 
...
```
Setelah menambahkan path url di atas, saya sekarang sudah bisa mengakses masing-masing fungsi dengan URL dan format yang sesuai.

- Mengakses kelima URL di poin 2 menggunakan Postman, membuat screenshot dari hasil akses URL pada Postman, dan menambahkannya ke dalam README.md.

a. HTML
![Alt Text](POSTMAN_HTML.png)

b. XML
![Alt Text](POSTMAN_XML.png)

c. JSON
![Alt Text](POSTMAN_JSON.png)

d. XML by ID
![Alt Text](POSTMAN_XML_ID.png)

e. JSON by ID
![Alt Text](POSTMAN_JSON_ID.png)

- Dan yang terakhir adalah melakukan push ke github dengan command ``add``, ``commit``, dan ``push``

</details>