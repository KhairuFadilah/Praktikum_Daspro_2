# Praktikum Daspro 2 SI Unmul 2023
Assalamualaikum Warahmatullahi Wabarakatuh,
Perkenalkan saya Muhammad Khairu Fadilah dari Sistem Informasi 2023, NIM 2309116025.
Sebelumnya, mohon maaf saya telat mengumpulkan posttest kali ini dikarenakan adanya kendala dari laptop saya.
Saya akan menjelaskan program tentang toko topup game saya (yang saya ambil referensinya dari pekerjaan asli saya). Flowchart terdapat di akhir penjelasan

Jadi, sebelum masuk ke program Python, disini saya menyiapkan satu file tambahan, yaitu file "list_diamond.csv"

![Persiapan](https://github.com/KhairuFadilah/Praktikum_Daspro_2/assets/144750627/f1924455-badc-461f-8cd3-779322e37454)

File ini akan dijadikan sebagai database dari semua input list dan prettytable.

Selanjutnya saya membuat 2 role, yaitu Customer dan Admin

![Role](https://github.com/KhairuFadilah/Praktikum_Daspro_2/assets/144750627/0c8a08cb-c8a8-4362-a28f-f028ece0d3fb)

Untuk Admin bisa melakukan CRUD (Create, Read, Update, Delete) terhadap data list, sedangkan Customer cuma bisa read data list.
Selanjutnya saya menambahkan login berdasarkan role.

![Login role](https://github.com/KhairuFadilah/Praktikum_Daspro_2/assets/144750627/d261c6b1-ec15-4abf-8fd1-4fcbbd00bf7b)

Untuk di bagian ini, saya membedakan tampilan login agar kedua role tidak salah memilih role. Untuk admin menggunakan ID Admin, sedangkan customer menggunakan Username.

![List role](https://github.com/KhairuFadilah/Praktikum_Daspro_2/assets/144750627/54cee9dc-ca39-431a-9e9e-d56aeee037b6)

Di bagian ini merupakan salah satu bukti bahwa hanya admin yang bisa melakukan CRUD. Nah, setelah admin melakukan CRUD, data tersebut tersimpan di dalam file .csv tadi. Contohnya:

a. Sebelum

![Contoh_sebelum](https://github.com/KhairuFadilah/Praktikum_Daspro_2/assets/144750627/fade8c4b-7413-4d83-b262-da4dece4b10b)

b. Create

![Contoh_create](https://github.com/KhairuFadilah/Praktikum_Daspro_2/assets/144750627/631124a3-0055-4b9f-af94-a54471b4b28b)


c. Sesudah

![Contoh_sesudah](https://github.com/KhairuFadilah/Praktikum_Daspro_2/assets/144750627/8e4e7359-da49-4a0d-9d5b-bd491fa63537)


Selanjutnya adalah fungsi utama. Anda bisa melihat hasil ss dari fungsi utama:

![Utama (cust)](https://github.com/KhairuFadilah/Praktikum_Daspro_2/assets/144750627/4c37d48d-a5ce-4c1a-bd85-86c06d8217fe)

![Utama (admin_1)](https://github.com/KhairuFadilah/Praktikum_Daspro_2/assets/144750627/68dd6aab-5352-47db-afee-12db655299dc)

![Utama (admin_2)](https://github.com/KhairuFadilah/Praktikum_Daspro_2/assets/144750627/cd4426b4-e9cb-408c-811b-4d12faa54577)

Di bagian fungsi utama, terdapat semacam login yang dikhususkan oleh masing-masing role. Apabila berhasil login, akan dimunculkan fungsi list_menu() dan meminta user untuk menginput angka yang telah ada di fungsi tersebut.
Customer bisa membaca list yang telah ditambah ataupun diedit oleh admin, namun hanya terbatas disitu saja. 

![Rincian role admin](https://github.com/KhairuFadilah/Praktikum_Daspro_2/assets/144750627/694e00d5-a046-4864-86a1-9fb1ff65d438)

Ini adalah rincian dari role admin. Di role admin lah yang menghubungkan file.csv menjadi prettytable dgn cara mengimpor file .csv ke prettytable.

![Rincian role cust](https://github.com/KhairuFadilah/Praktikum_Daspro_2/assets/144750627/f881414d-12f6-48dd-9850-7d05008e64d9)

Ini adalah rincian dari role customer. Memang tidak banyak fungsi yang diberikan, namun sudah cukup untuk membuat program berjalan.

Dibawan ini merupakan Flowchart dari codingan saya:

![Posttest 2 Daspro-Home](https://github.com/KhairuFadilah/Praktikum_Daspro_2/assets/144750627/0a3a64a4-52f8-4476-a8fc-8dd37f8fe144)

![Posttest 2 Daspro-Admin Only](https://github.com/KhairuFadilah/Praktikum_Daspro_2/assets/144750627/844e4c37-5beb-463e-8d14-efa843f9906d)

![Posttest 2 Daspro-Customer](https://github.com/KhairuFadilah/Praktikum_Daspro_2/assets/144750627/3becbf83-9126-47ad-9908-12bd5ee8314c)


Cukup sekian dari saya, apabila terdapat kekurangan mohon dimaafkan. Wassalamualaikum Warahmatullahi Wabarakatuh.

