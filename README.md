# Vending Machine Inventory
#### by Ravie Hasan Abud - 2206031864 - PBP A
#### Tugas 2: https://vending-machine.adaptable.app/main/
#### Tugas 3: (belum ada perintah deployment)
<hr>

# Tugas 2

## 1. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial)!

### Cara Pengerjaan Checklist
- [ ] Membuat sebuah proyek Django baru. <br>
    - Membuat directory baru bernama `vending_machine` yang akan dijadikan local directory/repository dari github repository
    - Membuka CMD pada directory `vending_machine` dan menjalankan `git init`,  `git config user.name <user_name>`, dan `git config user.email <user_email` untuk konfigurasi github
    - Membuat reporitory github baru bernama `vending-machine`
    - Membuat file `README.md` dan mengeditnya melalui VSCODE
    - Menjalankan `git branch -M main`, `git remote add origin https://github.com/raviehasan/vending-machine.git`, dan `git push -u origin main` untuk membuat main branch dengan nama `main`, menghubungkan local directory/repository dengan repository github, dan push/update semua perubahan ke github
    - Menjalankan `python -m venv env` untuk membuat virtual environment untuk directory agar dapat maintain versi-versi django dan lain sebagainya yang dipakai di device
    - Menjalankan `env\Scripts\activate.bat` untuk mengaktifkan virtual environment
    - Membuat file baru bernama `requirements.txt` dan mengisinya dengan hal-hal yang ingin diinstall agar tidak terlalu banyak menjalankan command `pip install ...`, saya mengisinya dengan:
    ```bash
    django
    gunicorn
    whitenoise
    psycopg2-binary
    requests
    urllib3
    ```
    - Menjalankan `pip install -r requirements.txt` untuk install hal-hal yang telah ditambahkan pada `requirements.txt` tadi
    - Menjalankan `django-admin startproject vending_machine .`
    - Membuka file `settings.py` dan ubah `ALLOWED_HOSTS = []` menjadi `ALLOWED_HOSTS = ["*"]` karena akan diperlukan untuk proses deployment 
    - Membuat file baru bernama `.gitignore` untuk memberikan informasi mengenai berkas yang perubahannya tidak perlu ditrack oleh Git, saya mengisina dengan:
    ```bash
    # Django
    *.log
    *.pot
    *.pyc
    __pycache__
    db.sqlite3
    media
    
    # Backup files
    *.bak 
    
    # If you are using PyCharm
    # User-specific stuff
    .idea/**/workspace.xml
    .idea/**/tasks.xml
    .idea/**/usage.statistics.xml
    .idea/**/dictionaries
    .idea/**/shelf
    
    # AWS User-specific
    .idea/**/aws.xml
    
    # Generated files
    .idea/**/contentModel.xml
    
    # Sensitive or high-churn files
    .idea/**/dataSources/
    .idea/**/dataSources.ids
    .idea/**/dataSources.local.xml
    .idea/**/sqlDataSources.xml
    .idea/**/dynamic.xml
    .idea/**/uiDesigner.xml
    .idea/**/dbnavigator.xml
    
    # Gradle
    .idea/**/gradle.xml
    .idea/**/libraries
    
    # File-based project format
    *.iws
    
    # IntelliJ
    out/
    
    # JIRA plugin
    atlassian-ide-plugin.xml
    
    # Python
    *.py[cod] 
    *$py.class 
    
    # Distribution / packaging 
    .Python build/ 
    develop-eggs/ 
    dist/ 
    downloads/ 
    eggs/ 
    .eggs/ 
    lib/ 
    lib64/ 
    parts/ 
    sdist/ 
    var/ 
    wheels/ 
    *.egg-info/ 
    .installed.cfg 
    *.egg 
    *.manifest 
    *.spec 
    
    # Installer logs 
    pip-log.txt 
    pip-delete-this-directory.txt 
    
    # Unit test / coverage reports 
    htmlcov/ 
    .tox/ 
    .coverage 
    .coverage.* 
    .cache 
    .pytest_cache/ 
    nosetests.xml 
    coverage.xml 
    *.cover 
    .hypothesis/ 
    
    # Jupyter Notebook 
    .ipynb_checkpoints 
    
    # pyenv 
    .python-version 
    
    # celery 
    celerybeat-schedule.* 
    
    # SageMath parsed files 
    *.sage.py 
    
    # Environments 
    .env 
    .venv 
    env/ 
    venv/ 
    ENV/ 
    env.bak/ 
    venv.bak/ 
    
    # mkdocs documentation 
    /site 
    
    # mypy 
    .mypy_cache/ 
    
    # Sublime Text
    *.tmlanguage.cache 
    *.tmPreferences.cache 
    *.stTheme.cache 
    *.sublime-workspace 
    *.sublime-project 
    
    # sftp configuration file 
    sftp-config.json 
    
    # Package control specific files Package 
    Control.last-run 
    Control.ca-list 
    Control.ca-bundle 
    Control.system-ca-bundle 
    GitHub.sublime-settings 
    
    # Visual Studio Code
    .vscode/* 
    !.vscode/settings.json 
    !.vscode/tasks.json 
    !.vscode/launch.json 
    !.vscode/extensions.json 
    .history
    ```
    <hr>

- [ ] Membuat aplikasi dengan nama `main` pada proyek tersebut.<br>
    - Masih pada CMD yang sama, jalankan `python manage.py startapp main` untuk membuat django app baru bernama `main` pada django project bernama `vending_machine`
    - Membuka file `settings.py` dan tambahkan `'main'` pada variabel `INSTALLED_APPS`
    - Membuka directory `main` dan buat directory baru bernama `templates` untuk menyimpan file `.html` yang akan digunakan karena django menggunakan Model-View-Template (MVT) 
    - Membuat file baru bernama `main.html` pada directory `templates` dan mengisinya dengan konten-konten yang diperlukan. Untuk Tugas 2, yang wajib muncul adalah nama aplikasi, nama, dan kelas
    <hr>

- [ ] Melakukan *routing* pada proyek agar dapat menjalankan aplikasi `main`. <br>
    - Membuka file `urls.py` pada directory `vending_machine`
    - Menambahkan `from django.urls import path, include`
    - Mengubah `urlpatterns` menjadi:
    ```bash
    urlpatterns = [
    path('admin/', admin.site.urls),
    path('main/', include('main.urls')),
    ]
    ```
    Note:
    - `path('main/', include('main.urls')),` digunakan untuk menambahkan routing dari `urls.py` pada directory `main` dan url yang ada pada `urls.py` di `main` akan menjadi `.../main/...`
    <hr>

- [ ] Membuat model pada aplikasi `main` dengan nama `Item` dan memiliki atribut wajib sebagai berikut.
    - `name` sebagai nama *item* dengan tipe `CharField`.
    - `amount` sebagai jumlah *item* dengan tipe `IntegerField`.
    - `description` sebagai deskripsi *item* dengan tipe `TextField`.
    <br>
    
    - Membuka `models.py` dan mengisinya dengan attributes/fields yang diperlukan. Pada kasus ini, saya menggunakan 5 attributes, yakni `name` (CharField), `amount` (IntegerField), `description` (TextField), `price` (IntegerField), dan `date_added` (DateField). Isi file `models.py` adalah sebagai berikut:
    ```bash
    from django.db import models

    class Product(models.Model):
        name = models.CharField(max_length=255, name="name")
        amount = models.IntegerField(name="amount")
        description = models.TextField(name="description")
        price = models.IntegerField(name="price")
        date_added = models.DateField(auto_now_add=True, name="date_added")

        def __str__(self):
            return f"Name: {self.name} {self.amount} {self.price} {self.date_added} {self.description}"
    .
    ```
    Note:
    - `__str__` diperlukan untuk keperluan unit tests
    <hr>

- [ ] Membuat sebuah fungsi pada `views.py` untuk dikembalikan ke dalam sebuah *template* HTML yang menampilkan nama aplikasi serta nama dan kelas kamu. <br>
    - Membuka `views.py` dan menambahkan potongan kode di bawah ini untuk menghubungkan Views dan Templates (e.g.: substitute `{{ <desired_variable> }}` pada file-file di directory `templates`). Saya memerlukan variables `name`, `class`, `student_id`, dan `products` (berisi detail setiap product yang ada). Sehingga, isi `views.py` sebagai berikut:
    ```bash
    from django.shortcuts import render
    from .models import Product

    def show_main(request):
        context = {
            'name': 'Ravie Hasan Abud',
            'class': 'PBP A',
            'student_id': '2206031864',
        }

        return render(request, "main.html", context)

    ```
    Note:
    - show_main digunakan untuk  `https://vending-machine.adaptable.app/main/`
    <hr>

- [ ] Membuat sebuah *routing* pada `urls.py` aplikasi `main` untuk memetakan fungsi yang telah dibuat pada `views.py`. <br>
    - ubah `urlpatterns` menjadi seperti ini:
    ```bash
    urlpatterns = [
        path('', show_main, name='show_main'), 
    ]
    ```
    Notes:
    - `products/` = ketika mengakses `.../main/products/` akan memanggil `show_products` dari `views.py`
    - `''` = ketika mengakses `.../main/` akan memanggil `show_main` dari `views.py`
    <hr>

- [ ] Melakukan *deployment* ke Adaptable terhadap aplikasi yang sudah dibuat sehingga nantinya dapat diakses oleh teman-temanmu melalui Internet. <br>
    - Menjalankan `git pull origin main`, `git add <desired_file>`, `git commit -m "<desired_message>"`, dan `git push -u origin main` untuk update github repository agar sesuai dengan locak repository
    - Klik `New App` -> `Connect an Existing Repository` -> `raviehasan/vending-machine` -> `main` -> `Python App Template` -> `PostgreSQL` -> python version = `3.10` (laptop saya menggunakan python version 3.10) -> `Start Command` dan tambahkan `python manage.py migrate && gunicorn vending_machine.wsgi` -> enable `HTTP Listener on PORT` -> `Deploy App` 
    - Jika deployment sudah berhasil, periksa `https://vending-machine.adaptable.app/main/` dan `https://vending-machine.adaptable.app/main/products/` untuk memastikan deployment berjalan dengan lancar
    <hr>

### Cara Pengerjaan Bonus (Unit Tests)
- Membuka directory `main` 
- Membuka `tests.py` mengisinya dengan tests yang diinginkan
- Saya ingin tes apakah url `.../main/` dan `.../main/products/` ada, maka perlu import `TestCase` dam `Client`
- Saya ingin tes model juga, sehingga perlu import `Product` dari `models.py`
```bash
from django.test import TestCase, Client
from .models import Product
from django.utils import timezone

class MainTest(TestCase):
    def test_main_url_is_exist(self):
        response = Client().get('/main/')
        self.assertEqual(response.status_code, 200)

    def test_main_using_main_template(self):
        response = Client().get('/main/')
        self.assertTemplateUsed(response, 'main.html')

class TestModels(TestCase):
    @classmethod
    def setUpTestData(cls):
        Product.objects.create(name="Chitato", amount=100, price=10000, date_added=timezone.now, description="Chips")

    def test_string_method(self):
        product = Product.objects.get(id=1)
        expected_string = f"Name: {product.name} {product.amount} {product.price} {product.date_added} {product.description}"
        self.assertEqual(str(product), expected_string)
```
- Jalankan `python manage.py test` untuk mengecek apakah test sudah sukses
- Jalankan `coverage run --source='.' manage.py test` untuk menjalankan tes dan mengumpulkan coverage data
- Jalankan `coverage run --source='.' manage.py test` untuk melihat report dari coverage data
Notes:
- `test_main_url_is_exist` digunakan untuk test apakah terdapat url `https://vending-machine.adaptable.app/main/`
- `test_main_using_main_template` digunakan untuk test apakah `https://vending-machine.adaptable.app/main/` menggunakan `main.html` sebagai template
- `setUpTestData` digunakan untuk membuat objek baru dengan attributes yang diinginkan dijadikan argumen 
- `test_string_method` digunakan untuk test apakah objek yang telah dibuat memiliki atribut yang sesuai
<hr>

## 2. Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html
![alt-text](images/client-django-flow.png)
- Client mengirim request ke Internet -> forward ke Python/Django -> forward ke urls.py -> forward ke views.py untuk memproses url -> read/write data dari/ke models.py dan database -> input/display data dari/ke templates -> return html file yang telah dimerge dengan value-value yang diinginkan -> proses ke internet -> display ke client's device
<hr>

## 3. Jelaskan mengapa kita menggunakan virtual environment? Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment?
- Virtual environment dapat mengisolasi dependencies untuk masing-masing django project. Tujuannya adalah karena dapat mempermudah ketika kita berkolaborasi dengan orang lain karena orang tersebut dapat include dependencies (python version, django version, etc.) yang digunakan pada django project kita. Dengan alasan yang sama, virtual environment juga memungkinkan kita untuk dapat mengerjakan project yang sama melalui berbagai device berbeda dengan cara include dependencies dari project tersebut.
- Walaupun demikian, kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment. Hanya saja ada banyak risiko muncul error, dimulai dari bibsa terjadi konflik antar project karena dependencies antar project (misal perbedaan versi python dan django, etc.), akan lebih sulit untuk melakukan development project, hingga risiko gagal melakukan deploy juga cukup tinggi karena hal-hal tersebut.
<hr>

## 4. Jelaskan apakah itu MVC, MVT, MVVM dan perbedaan dari ketiganya.
- <b>MVC (Model-View-Controller)</b>
    - Model: untuk mencari dan mengolah data yang diminta oleh Database
    - View: menampilkan data dengan design yang dibuat di sini (kurang lebih seperti Template pada MVT dan View pada MVVM)
    - Controller: mengatur bagaimana data akan ditampilkan di View (kurang lebih seperti View pada MVT)
    - Input diterima oleh Controller
    - Kurang cocok untuk aplikasi berskala kecil
- <b>MVT/MTV (Model-View-Template)</b>
    - Model: untuk mencari dan mengolah data yang diminta oleh database
    - View: mengatur bagaimana data akan ditampilkan di Template (kurang lebih seperti Controller pada MVC)
    - Template: menampilkan data dengan design yang dibuat di sini (kurang lebih seperti View pada MVC dan MVVM)
    - Input diterima oleh View
    - Cocok digunakan baik untuk aplikasi berskala besar maupun kecil
    - Mudah melakukan modifikasi
- <b>MVVM (Model-View-ViewModel)</b>
    - Model: tempat untuk menyimpan informasi
    - View: menampilkan data dengan design yang dibuat di sini (kurang lebih seperti View pada MVC dan Template pada MVVM)
    - ViewModel: menghubungkan Model dan View
    - Input diterima oleh View
    - Kurang cocok untuk palikasi berskala kecil
    - Memiliki kelebihan dalam proses binding data
    <hr>
    
## References
- [Slide 2 SCeLE "Introduction to Internet and Web Framework"](https://scele.cs.ui.ac.id/pluginfile.php/193239/mod_resource/content/1/02%20-%20Introduction%20to%20the%20Internet%20and%20Web%20Framework.pdf)
- [Slide 3 SCeLE "MTV Django Architecture"](https://scele.cs.ui.ac.id/pluginfile.php/193781/mod_resource/content/1/03%20-%20MTV%20Django%20Architecture.pdf)
- [Tutorial 0 dan Tutorial 1](https://pbp-fasilkom-ui.github.io/ganjil-2024/docs)
- [Getting Started with Django Unit Testing](https://www.section.io/engineering-education/django-unit-testing/)
- [Definition Model-View-ViewModel (MVVM)](https://www.techtarget.com/whatis/definition/Model-View-ViewModel)
- [MVC Framework - Introduction](https://www.tutorialspoint.com/mvc_framework/mvc_framework_introduction.htm)
<hr>

# Tugas 3

## 1. Apa perbedaan antara form `POST` dan form `GET` dalam Django?
- <b>POST</b>
    - Digunakan untuk mengirimkan data ke server (membuat, mengganti, menghapus, etc.), return HTTP status code 201 jika berhasil
    - Values tidak visible pada URL (data dikirimkan saat HTML request)
    - Tidak memiliki limitasi panjang karakter
    - Dapat menggunakan berbagai tipe data (contoh: string, integer)
    - Lebih secured karena data tidak terekspos pada URL
    - Dapat digunakan untuk mengirimkan data penting (contoh: password)
    - Parameter tidak disimpan pada history browser
    - Non-idempotent
- <b>GET</b>
    - Digunakan untuk membaca/mengakses data dari web server, retrun HTTP status code 200 jika berhasil
    - Values visible pada URL --> user dapat input nilai variabel baru dengan lebih mudah
    - Panjang karakter terbatas (umumnya maksimal 255 karakter)
    - Hanya dapat menggunakan tipe data string
    - Kurang aman karena data terekspos pada URL
    - Dapat digunakan untuk mengirimkan data yang tidak terlalu penting
    - Parameter disimpan pada history browser
    - Idempotent (request selanjutnya akan diabaikan hingga request yang sedang dijalankan selesai mengirimkan respon)
<hr>

## 2. Apa perbedaan utama antara XML, JSON, dan HTML dalam konteks pengiriman data?
- <b>HTML</b>
    - Menurut saya kurang human-readable apabila merepresentasikan data menggunakan HTML (apabila dilihat melalui Postman)
    - Secara umum digunakan untuk membuat struktur, layout, dan konten dari web page yang akan ditampilkan. Untuk data yang bersifat dinamis dapat memanfaatkan tools semacam XML, JSON, etc.
- <b>XML</b>
    - Menurut saya human-readable karena strukturnya jelas untuk dibaca, namun proses delivery datanya memerlukan waktu lebih lama jika dibandingkan dengan JSON.
    - Secara umum digunakan untuk menyimpan dan melakukan transfer/pertukaran data melalui internet, banyak digunakan pada web dan mobile app
    - XML lebih secure jika dibandingkan dengan JSON (JSON lebih vulnerable)
    - Waktu eksekusi tidak secepat JSON
    - Struktur data dapat terlihat dengan sangat jelas karena tag nya dapat dicustom (berbeda dengan HTML). Namun, waktu eksekusi program menjadi sedikit lebih lama karena banyak tag
- <b>JSON</b>
    - Menurut saya human-readable karena JSON menggunakan list dan dictionary python. Proses delivery dengan JSON jauh lebih cepat jika dibandingkan dengan menggunakan XML.
    - Secara umum digunakan untuk menyimpan dan melakukan transfer/pertukaran data antara server dan aplikasi web, banyak digunakan juga pada web dan mobile app
    - JSON lebih compatible terhadap teknologi-teknologi web dan lebih mudah untuk dimaintain oleh web developers jika dibandingkan dengan XML
    - Waktu eksekusi lebih cepat dibandingkan XML
    - Tidak menggunakan tag, sehingga lebih ringkas dan bisa merepresentasikan dengan ukuran file yang kecil
<hr>

## 3. Mengapa JSON sering digunakan dalam pertukaran data antara aplikasi web modern?
- Tingkat simplicity dan readability yang tinggi karena karena syntax dan indentasinya yang ringkas
- Memiliki banyak method yang dapat mempercepat proses penyusunan program (contoh: JSON.parse() untuk mengubah JSON string menjadi Object dengan atribut-atributnya)
- Dapat merepresentasikan data dengan ukuran file yang kecil karena syntaxnya ringkas (seperti tidak menggunakan tag, etc.)
- JDapat melakukan transfer/pertukaran data dengan sangat cepat (tidak perlu banyak parse karena syntaxnya juga singkat)
- Sangat compatible dengan berbagai teknologi web, seperti JavaScript dan lain-lain.
- Mendukung tipe data native, seperti numbers, booleans, null, etc.
<hr>

## 4. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial)!
- [ ] Membuat input `form` untuk menambahkan objek model pada app sebelumnya.
    1. Membuat `base.html` pada root/templates dan mengisinya dengan:
    ```html
    {% load static %}
    <!DOCTYPE html>
    <html lang="en">
        <head>
            <meta charset="UTF-8" />
            <meta
                name="viewport"
                content="width=device-width, initial-scale=1.0"
            />
            {% block meta %}
            {% endblock meta %}
        </head>

        <body>
            {% block content %}
            {% endblock content %}
        </body>
    </html>
    ```
    - `{% something %}` dapat diisi dari file lain (seperti semacam placeholder)
    2. Membuat `forms.py` pada `vending_machine/main` dan mengisinya dengan:
    ```python
    from django.forms import ModelForm
    from main.models import Product

    class ProductForm(ModelForm):
        class Meta:
            model = Product
            fields = ["name", "price", "amount", "description"]
    ```
    - `model = Product` menandakan bahwa isian form akan disimpan sebagai object Product
    - `fields` menandakan bahwa object Product memiliki 4 atribut yang dapat diisi melalui form (name, price, amount, description)
    3. Ubah function `show_main` pada `vending_machine/vending_machine/main/views.py` menjadi sebagai berikut:
    ```python
    def show_main(request):
        products = Product.objects.all()
        context = {
            'name': 'Ravie Hasan Abud',
            'class': 'PBP A',
            'student_id': '2206031864',
            'products': products,
            'total_products': products.__len__(),
        }

        return render(request, "main.html", context)
    ```
    - `'products` akan menyimpan seluruh product yang ada pada project saat ini
    - `total_products` akan menyimpan banyak product yang ada pada project saat ini
    4. Buat `create_product.html` pada `vending_machine/mcending_machine/main/templates/` dan isi sebagai berikut:
    ```html
    {% extends 'base.html' %} 

    {% block content %}
    <h1>Add New Product</h1>

    <form method="POST">
        {% csrf_token %}
        <table>
            {{ form.as_table }}
            <tr>
                <td></td>
                <td>
                    <input type="submit" value="Add Product"/>
                </td>
            </tr>
        </table>
    </form>

    {% endblock %}
    ```
    - `{% block content %} ... {% endblock %}` adalah konten yang akan mengisi placeholder block content pada `base.html`
    - `<form method="POST>` karena user akan memberikan beberapa input

<hr>

- [ ] Tambahkan 5 fungsi `views` untuk melihat objek yang sudah ditambahkan dalam format HTML, XML, JSON, XML *by ID*, dan JSON *by ID*.
    1. `create_product` untuk menerima input user, dapat diakses ketika user klik button "Add New Product" atau ketika user mengakses `(url)/create-product`
    ```python
    def create_product(request):
        form = ProductForm(request.POST or None)

        if form.is_valid() and request.method == "POST":
            form.save()
            return HttpResponseRedirect(reverse('main:show_main'))

        context = {'form': form}
        return render(request, "create_product.html", context)    
    ```
    2. `show_xml` untuk menampilkan representasi seluruh products dalam format XML, dapat diakses pada `(url)/xml`
    ```python
    def show_xml(request):
        data = Product.objects.all()
        return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")
    ```
    3. `show_json` untuk menampilkan representasi seluruh products dalam format JSON, dapat diakses pada `(url)/json`
    ```python
    def show_json(request):
        data = Product.objects.all()
        return HttpResponse(serializers.serialize("json", data), content_type="application/json")    
    ```
    4. `show_xml_by_id` untuk menampilkan representasi product dengan id yang diinginkan dalam format XML, dapat diakses pada `(url)/xml/(desired_id)`
    ```python
    def show_xml_by_id(request, id):
        data = Product.objects.filter(pk=id)
        return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")    
    ```
    5. `show_json_by_id` untuk menampilkan representasi product dengan id yang diinginkan dalam format JSON, dapat diakses pada `(url)/json/(desired_id)`
    ```python
    def show_json_by_id(request, id):
        data = Product.objects.filter(pk=id)
        return HttpResponse(serializers.serialize("json", data), content_type="application/json")    
    ```
<hr>

- [ ] Membuat routing URL untuk masing-masing `views` yang telah ditambahkan pada poin 2.
    1. Isi `vending_machine/vending_machine/main/templates/urls.py` dengan:
    ```python
    from django.urls import path
    from main.views import show_main, create_product, show_xml, show_json, show_xml_by_id, show_json_by_id # , show_products

    app_name = 'main'

    urlpatterns = [
        path('', show_main, name='show_main'), 
        path('create-product', create_product, name='create_product'),
        path('xml/', show_xml, name='show_xml'), 
        path('json/', show_json, name='show_json'),
        path('xml/<int:id>/', show_xml_by_id, name='show_xml_by_id'),
        path('json/<int:id>/', show_json_by_id, name='show_json_by_id'), 
    ]
    ```
    `urlpatterns` digunakan agar function-function yang telah dicantumkan pada `views.py` dapat diakses dengan url yang diinginkan, untuk project ini detailnya sebagai berikut:
    - `(url)/create-product`: Untuk user input product baru
    - `(url)/xml`: Untuk menampilkan representasi seluruh products dalam format XML
    - `(url)/json`: Untuk menampilkan representasi seluruh products dalam format JSON
    - `(url)/xml/(desired_id)`: Untuk menampilkan representasi product dengan id yang diinginkan dalam format XML
    - `(url)/xml/(desired_id)`: Untuk menampilkan representasi product dengan id yang diinginkan dalam format JSON
<hr>

### Cara Pengerjaan Bonus:
1. Tambahkan `'total_products': products.__len__(),` pada `vending_machine/main/views.py` untuk menyimpan bannyaknya jumlah product saat ini
2. Tambahkan `<h3>Kamu menyimpan {{total_products}} product pada aplikasi ini</h3>` pada `vending_machine/vending_machine/main/templates/main.html` karena banyaknya product saat ini disimpan pada `total_products`
<hr>

## 5. Mengakses kelima URL di poin 2 menggunakan Postman, membuat screenshot dari hasil akses URL pada Postman, dan menambahkannya ke dalam README.md
NOTE: Saya sempat menghapus product ke-2 (pk="2") sehingga setelah pk="1" langsung pk="2"
1. 
- HTML: `(url)`: Untuk user melihat available products
![alt-text](images/tugas3_html.png)
- HTML: `(url)/create-product`: Untuk user input product baru
![alt-text](images/tugas3_html_create_product.png)
2. XML: `(url)/xml`: Untuk menampilkan representasi seluruh products dalam format XML
![alt-text](images/tugas3_xml.png)
3. JSON: `(url)/json`: Untuk menampilkan representasi seluruh products dalam format JSON
![alt-text](images/tugas3_json.png)
4. XML by ID: `(url)/xml/(desired_id)`: Untuk menampilkan representasi product dengan id yang diinginkan dalam format XML
![alt-text](images/tugas3_xml_by_id.png)
5. JSON by ID: `(url)/xml/(desired_id)`: Untuk menampilkan representasi product dengan id yang diinginkan dalam format JSON
![alt-text](images/tugas3_json_by_id.png)
<hr>

## References
- [Slide 4 SCeLE "Data Delivery"](https://scele.cs.ui.ac.id/mod/resource/view.php?id=150830)
- [Tutorial 2](https://pbp-fasilkom-ui.github.io/ganjil-2024/docs/tutorial-2)
- [Get vs. Post](https://www.javatpoint.com/get-vs-post)
- [Handling an HTML Form – GET and POST Methods, and Data Encoding [Dev Concepts #38]](https://softuni.org/dev-concepts/handling-an-html-form/)
- [What’s the Relationship Between XML, JSON, HTML and the Internet?](https://www.deltaxml.com/blog/xml/whats-the-relationship-between-xml-json-html-and-the-internet/#:~:text=In%20short%2C%20HTML%20is%20the,is%20really%20no%20practical%20alternative.)
- [What are the advantages and disadvantages of using JSON vs XML?](https://www.linkedin.com/advice/0/what-advantages-disadvantages-using-json-vs-xml#:~:text=Generally%20speaking%2C%20JSON%20is%20more,but%20less%20secure%20than%20XML.)
<hr> 

# Tugas 4

## 1. Apa itu Django `UserCreationForm`, dan jelaskan apa kelebihan dan kekurangannya?
- Merupakan form yang disediakan Django dan dapat digunakan untuk membuat (register) user baru dan user tersebut kemudian dapat login
- By default, terdiri atas 3 fields, yaitu `username`, `passowrd1`, dan `password2`
- Kelebihan:
    - Telah disediakan/diimplementasikan oleh Django, sehingga kita dapat langsung menggunakannya (tidak perlu membuat from scratch), baik cukup dengan default yang disediakan maupun ingin menambahkan fields custom lain
    - By default, telah memvalidasi input dari user, e.g. `password must be at least 8 characters`, `password can't be entirely numeric`, etc., sehingga kita tidak perlu mengimplementasikan manual
- Kekurangan:
    - Kurang customizable, jika perlu menambahkan kustomisasi (e.g. menambahkan fields baru) perlu mengedit beberapa file dan mengimplementasikannya secara manual
    - Untuk fitur seperti login, logout, etc. tetap ada beberapa hal yang harus diimplementasikan secara manual (tidak disediakan oleh Django UserCreationForm)
    - Ketentuan passwordnya agak strict sehingga dapat agak merepotkan

<hr>

## 2. Apa perbedaan antara autentikasi dan otorisasi dalam konteks Django, dan mengapa keduanya penting?
- Autentikasi
    - Merupakan mekanisme verifikasi terkait sapakah yang ingin mengakses web page, apakah user tersebut terdaftar pada sistem?
    - Autentikasi penting karena semacam step awal dari user untuk dapat mengakses web page yang menerapkan authorization, apabila user tidak terdaftar pada sistem maka user tidak akan dapat mengakses web page tersebut. Hal ini penting untuk segi keamanan web juga untuk memastikan hanya user yang terdaftar yang dapat mengakses
    - Contoh: Login page pada SIAK di mana user akan diminta input berupa username dan password yang kemudian akan diperiksa apakah benar ada user dengan username dan password tersebut, jika iya maka user tersebut dapat mengakses page SIAK, jika tidak maka akan diminta input ulang.
- Otorisasi
    - Merupakan mekanisme verifikasi apakah user yang telah terautentikasi dapat mengakses suatu web, fitur, resources, etc.
    - Otorisasi penting karena digunakan untuk mengelola dan membatasi apa saja hal-hal yang dapat dilakukan dan tidak dapat dilakukan oleh seorang user. Hal ini penting untuk pengelolaan pengguna juga agar tidak ada user yang dapat mengakses/mengubah suatu hal yang seharusnya hanya dapat diakses oleh beberapa user
    - Contoh: Pada Spotify terdapat regular user dan premium user, user premium memiliki akses berbeda dengan user biasa (e.g. tidak ada ads, dapat play secara shuffle maupun berurut, etc.). Maka dari itu, kita dapat menggunakan otorisasi untuk membedakan terkait resources apa saja yang dapat diakses oleh regular user dan premium user
    - Contoh lain: Pada SIAK terdapat beberapa jenis role (e.g. Dosen, Mahasiswa, etc.) di mana role Dosen dapat memberikan dan melihat nilai banyak mahasiswa, sedangkan role Mahasiswa hanya dapat melihat nilai masing-masing (jika sudah dipublish)
<hr>

## 3. Apa itu cookies dalam konteks aplikasi web, dan bagaimana Django menggunakan cookies untuk mengelola data sesi pengguna?
Cookies merupakan informasi/data kecil yang disimpan saat user berinteraksi dengan aplikasi web. Cookies sering digunakan untuk mengelola data sesi pengguna (dapat memanfaatkan holding state karena HTTP bersifat stateless), track preferensi user, mengumpulkan data analitis, hingga personalisasi konten untuk masing-masing pengguna. Cookies memiliki tanggal dan waktu kedaluwarsa dan akan dihapus secara otomatis ketika waktu kedaluwarsanya tiba.

Contoh implementasi cookie di Django:
- `response.set_cookie('last_login', str(datetime.datetime.now()))` dapat digunakan untuk menambahkan cookie dengan nama `last_login` yang akan menyimpan kapan user terkait terakhir kali login
- Kemudian kita bisa menambahkan `'last_login': request.COOKIES['last_login'],` pada function di views.py untuk mengakses cookie `last_login` yang telah dibuat dan disimpan tadi
<hr>

## 4. Apakah penggunaan cookies aman secara default dalam pengembangan web, atau apakah ada risiko potensial yang harus diwaspadai?
Sebenarnya cookie tidak berbahaya karena cookie hanyalah sebuah data dan bersifat pasif. Hanya saja, walaupun cookie bersifat pasif (hanya merupakan data dan tidak bisa mengakses data, membaca data, maupun mengganti data yang ada di sistem), penggunaan cookies dalam pengembangan web tetap memiliki sejumlah risiko potensial yang perlu diwaspadai. Perlu dicatat bahwa yang berbahaya bukan cookie, melainkan bagaimana cara cookies digunakan dalam konteks aplikasi web yang ternyata dapat disalahgunakan. Dalam penggunaan cookies, harus waspada terkait CSRF, XSS, Cookie theft, dan lain-lain. Oleh karena itu, sebaiknya tidak menyimpan data yang tergolong sensitif di cookies.
<hr>

## 5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
- [ ] Mengimplementasikan fungsi registrasi, login, dan logout untuk memungkinkan pengguna untuk mengakses aplikasi sebelumnya dengan lancar.
    - Tambahkan kode berikut ke `vending_machine/vending_machine/main/viesw.py`
    ```python
        def register(request):
            form = UserCreationForm()

            if request.method == "POST":
                form = UserCreationForm(request.POST)
                if form.is_valid():
                    form.save()
                    messages.success(request, 'Your account has been successfully created!')
                    return redirect('main:login')
            context = {'form':form}
            return render(request, 'register.html', context)

        def login_user(request):
            if request.method == 'POST':
                username = request.POST.get('username')
                password = request.POST.get('password')
                user = authenticate(request, username=username, password=password)
                if user is not None:
                    login(request, user)
                    response = HttpResponseRedirect(reverse("main:show_main")) 
                    response.set_cookie('last_login', str(datetime.datetime.now()))
                    return response
                else:
                    messages.info(request, 'Sorry, incorrect username or password. Please try again.')
            context = {}
            return render(request, 'login.html', context)

        def logout_user(request):
            logout(request)
            response = HttpResponseRedirect(reverse('main:login'))
            response.delete_cookie('last_login')
            return response
    ```
    - `response.setcookie('last_login', str(datetime.datetime.now()))` digunakan untuk menyimpan waktu terakhir user yang bersangkutan login pada cookie
    - Tambahkan `'last_login': request.COOKIES['last_login'],` pada context di views.py untuk mengakses cookie last_login
    - Tambahkan `@login_required(login_url='/login')` di atas function show_main pada views.py untuk memastikan hanya logged in user yang bisa akses
    - Tambahkan potongan kode berikut pada urls.py untuk handle routing:
    ```python
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'), 
    ```
    - Buat template yang akan digunakan untuk masing-masing routing dari views.py (klik untuk mengakses):
        - [register.html](main/templates/register.html)
        - [main.html](main/templates/main.html)
        - [login.html](main/templates/login.html)

- [ ] Membuat dua akun pengguna dengan masing-masing tiga dummy data menggunakan model yang telah dibuat pada aplikasi sebelumnya untuk setiap akun di lokal.
    - Buka `localhost:8000` dan register untuk 3 username dengan username yang berbeda dan password
    - Login ntuk ketiga user tersebut, kemudian buat 2 product/oitem baru dengan klik tombol `Add New Product` dan isi seluruh detail product yang diinginkan
    - Setelah selesai coba cek apakah product yang ditambahkan sudah ada di tabel
    - Apabila sudah benar, seharusnya setiap user memiliki tabel dengan isi product yang berbeda-beda

- [ ] Menghubungkan model Item dengan User.
    - Tambahkan `user = models.ForeignKey(User, on_delete=models.CASCADE)` pada class Product di models.py untuk initiate Many to One relationship (karena menggunakan ForeignKey) pada User dengan Product/Item.
    - Ubah views.py pada bagian:
    ```python
    def create_product(request):
        form = ProductForm(request.POST or None)

        if form.is_valid() and request.method == "POST":
            product = form.save(commit=False)
            product.user = request.user
            product.save()
            return HttpResponseRedirect(reverse('main:show_main'))
    ```
    - Tambahkan `products = Product.objects.filter(user=request.user)` dan ubah context untuk key 'name'
    ```python
    def show_main(request):
        products = Product.objects.filter(user=request.user)

        context = {
            'name': request.user.username,
        ...
        }
    ```
    - Lakukan migration untuk menyimpan perubahan

- [ ] Menampilkan detail informasi pengguna yang sedang logged in seperti username dan menerapkan cookies seperti last login pada halaman utama aplikasi.
    - Untuk menampilkan username dan class user dapat menggunakan potongan kode berikut pada main.html:
    ```html
    <p>Name: {{name}}</p> 
    <p>Class: {{class}}</p>
    ```
    - Untuk menampilkan data last login user dapat memanfaatkan Cookies dengan menggunakan potongan kode berikut pada main.html:
    ```html
    <p>Sesi terakhir login: {{ last_login }}</p>
    ```
    - Untuk mengimplementasikan cookiesnya sebagai berikut:
        - `response.set_cookie('last_login', str(datetime.datetime.now()))` pada function login_user di views.py untuk set cookie kapan user login terakhir kali
        - `response.delete_cookie('last_login')` pada function logout_user di views.py untuk menghapus cookie
        - `'last_login': request.COOKIES['last_login'],` pada context function show_main di views.py 

<hr>

### Cara Pengerjaan Bonus:
- Menambahkan potongan kode berikut pada `vending_machine/vending_machine/main/templates/main.html`:
    ```html
    <a href="edit-amount/{{product.id}}/0">
        <button type="button" class="btn btn-success">
        +1
        </button>
    </a>
    <a href="edit-amount/{{product.id}}/1">
        <button type="button" class="btn btn-warning">
        -1
        </button>
    </a>
    <a href="edit-amount/{{product.id}}/2">
        <button type="button" class="btn btn-danger">
        Delete Product
        </button>
    </a>
    ```
    - Parameter yang saya gunakan adalah 0=increment, 1=decrement, dan 2=delete
- Menambahkan potongan kode berikut ke `vending_machine/vending_machine/main/urls.py` untuk menyesuaikan href yang ada pada anchor tag di `main.html`
    ```python
    urlpatterns = [ 
       ...
       path('edit-amount/<int:id>/<int:amount_change>/', edit_amount, name='edit_amount'),
       ... 
    ]
    ```
- Menambahkan function berikut ke `views.py` pada app `main`
    ```python
    @login_required(login_url='login/')
    def edit_amount(request, id, amount_change):
        product = Product.objects.get(id=id)
        # "+1" Button clicked --> Increment amount by 1
        if amount_change == 0:
            product.amount = product.amount + 1
            product.save()

        # "-1" Button clicked --> Decrement amount by 1
        elif amount_change == 1:
            if (product.amount > 0):
                product.amount = product.amount - 1
                product.save()
            if product.amount == 0: # jika produk sudah habis = delete
                product.delete()
            
        # "Delete Product" Button clicked --> Delete the product
        else:
            product.delete()

        return HttpResponseRedirect(reverse('main:show_main'))
    ```
    - If amount_change=0 increment, amount_change=1 decrement, amount_change=2 delete

<hr>

## References
- [Slide 5 "Form, Authentication, Session, and Cookie"](https://scele.cs.ui.ac.id/mod/resource/view.php?id=151405)
- [Tutorial 3](https://pbp-fasilkom-ui.github.io/ganjil-2024/docs/tutorial-3)
- [Django UserCreationForm | Creating New User](https://www.javatpoint.com/django-usercreationform)
- [Django Cookie](https://www.javatpoint.com/django-cookie)
<hr>
