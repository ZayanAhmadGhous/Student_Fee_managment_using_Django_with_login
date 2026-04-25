# 🎓 Student Management System (Django)

## 📌 Overview

This is a simple **Student Management System** built with Django.
It allows you to manage student records, including their **names and fees**, through a web-based interface.

The project includes an **admin panel** with secure login using a superuser account.

---

## ⚙️ Features

* Add, update, and delete student records
* Store student **name and fee details**
* Admin dashboard for management
* Secure login system (superuser authentication)
* Simple and clean UI built with Django templates

---

## 🛠️ Technologies Used

* Python
* Django
* SQLite (default database)

---

## 🚀 Installation & Setup

### 1. Clone the repository

```bash
git clone https://github.com/ZayanAhmadGhous/tudent_Fee_managment_using_Django_with_login.git
cd tudent_Fee_managment_using_Django_with_login
```

### 2. Create virtual environment (optional but recommended)

```bash
python -m venv venv
source venv/Scripts/activate   # On Windows (Git Bash)
# or
source venv/bin/activate       # On Linux/Mac
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Apply migrations

```bash
python manage.py migrate
```

### 5. Create superuser

```bash
python manage.py createsuperuser
```

Enter username, email, and password when prompted.

### 6. Run the server

```bash
python manage.py runserver
```

---

## 🌐 Usage

* Open your browser and go to:
  `http://127.0.0.1:8000/`

* Admin panel:
  `http://127.0.0.1:8000/admin/`

* Login using your **superuser credentials** to manage student data.

---

## 📂 Project Structure (Simplified)

```
project/
│── app/
│── templates/
│── db.sqlite3
│── manage.py
```

---

## 🔐 Authentication

* Only authorized users (superuser) can access the admin panel
* Login requires **username and password**

---

## 📈 Future Improvements

* Add student search functionality
* Add fee payment tracking system
* Improve UI with Bootstrap
* Role-based user access

---

## 👨‍💻 Author

Name: ZAYAN AHMAD GHOUS
Email: [Gmail](zayanahmad.ghous@gmail.com)
LinkedIn: [LinkedIn](https://www.linkedin.com/in/zayan-ahmad-23863625b/)

---

## 📄 License

This project is open-source and available under the MIT License.
