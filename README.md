# 📝 NoteSpace

> **A modern Django-based Blog Management System for creating, managing, and sharing ideas with an elegant and responsive user experience.**

![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python)
![Django](https://img.shields.io/badge/Django-5.x-green?style=for-the-badge&logo=django)
![SQLite](https://img.shields.io/badge/SQLite-Database-blue?style=for-the-badge&logo=sqlite)

---

# 📖 Overview

**NoteSpace** is a feature-rich **Blog Application** developed using **Django**. It enables users to create, edit, organize, and publish blog posts while providing an intuitive interface for readers.

The project focuses on clean architecture, scalability, and maintainability, making it suitable for learning Django as well as building production-ready blogging platforms.

---

# ✨ Features

## 👤 User Features

- User Registration & Login
- Secure Authentication
- User Profile Management
- Create Blog Posts
- Edit Existing Posts
- Delete Posts
- View All Blogs
- View Individual Blog Details
- Category-based Filtering
- Tag Support
- Search Functionality
- Responsive Design
- Rich Text Content Support
- Image Upload for Posts
- Mobile Friendly Interface

---

## 🔐 Authentication

- Django Authentication System
- Login & Logout
- Password Hashing
- Session Management
- Protected Routes
- CSRF Protection

---

## 🛠️ Admin Features

- Django Admin Dashboard
- Manage Users
- Manage Categories
- Manage Tags
- Manage Blog Posts
- Manage Uploaded Images
- Content Moderation

---

# 🏗️ Tech Stack

| Technology | Usage |
|------------|-------|
| Python | Backend Language |
| Django | Web Framework |
| HTML5 | Frontend Structure |
| CSS3 | Styling |
| Bootstrap / Tailwind CSS | Responsive UI |
| JavaScript | Client-side Functionality |
| SQLite | Development Database |
| Cloudinary (Optional) | Image Storage |
| Supabase (Optional) | Cloud Services |

---

# 📂 Project Structure

```
NoteSpace/
│
├── blog/
│   ├── migrations/
│   ├── templates/
│   ├── static/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   ├── forms.py
│   └── admin.py
│
├── NoteSpace/
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
│
├── media/
├── static/
├── templates/
├── manage.py
├── requirements.txt
└── README.md
```

---

# 🚀 Installation

## 1️⃣ Clone the Repository

```bash
git clone https://github.com/your-username/NoteSpace.git

cd NoteSpace
```

---

## 2️⃣ Create Virtual Environment

### Windows

```bash
python -m venv venv

venv\Scripts\activate
```

### Linux / macOS

```bash
python3 -m venv venv

source venv/bin/activate
```

---

## 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 4️⃣ Apply Migrations

```bash
python manage.py makemigrations

python manage.py migrate
```

---

## 5️⃣ Create Superuser

```bash
python manage.py createsuperuser
```

---

## 6️⃣ Run Development Server

```bash
python manage.py runserver
```

Open:

```
http://127.0.0.1:8000/
```

Admin Panel:

```
http://127.0.0.1:8000/admin/
```

---

# ⚙️ Environment Variables

Create a `.env` file in the project root.

```env
SECRET_KEY=your_secret_key

DEBUG=True

ALLOWED_HOSTS=localhost,127.0.0.1
```

If using Cloudinary:

```env
CLOUDINARY_CLOUD_NAME=your_cloud_name

CLOUDINARY_API_KEY=your_api_key

CLOUDINARY_API_SECRET=your_api_secret
```

---

# 🗄️ Database

Default database:

```
SQLite3
```

Can be easily migrated to:

- PostgreSQL
- MySQL
- MariaDB

---

# 📌 Main Models

## User

- Username
- Email
- Password

---

## Category

- Name
- Slug

---

## Tag

- Name

---

## Post

- Title
- Slug
- Content
- Featured Image
- Author
- Category
- Tags
- Created At
- Updated At
- Published Status

---

# 🎯 Future Improvements

- ❤️ Like System
- 💬 Comment System
- 🔖 Bookmark Blogs
- 📈 Blog Analytics
- 🌙 Dark Mode
- 🔔 Notifications
- 📤 Social Sharing
- 📧 Email Verification
- 🔍 Advanced Search
- 🤖 AI-powered Content Suggestions

---

# 📷 Screenshots

Add project screenshots here.

```
screenshots/
│
├── home.png
├── blog-list.png
├── blog-detail.png
├── dashboard.png
└── admin-panel.png
```

---

# 🤝 Contributing

Contributions are welcome!

1. Fork the repository

2. Create a new branch

```bash
git checkout -b feature/new-feature
```

3. Commit your changes

```bash
git commit -m "Added new feature"
```

4. Push to your branch

```bash
git push origin feature/new-feature
```

5. Open a Pull Request

---

# 📄 License

This project is licensed under the **MIT License**.

---

# 👨‍💻 Author

## Kushal Vaghela

**Software Developer | Django | MERN Stack | Java | Next.js**

If you found this project helpful, consider giving it a ⭐ on GitHub.

---

## ⭐ Show Your Support

If you like this project:

- ⭐ Star this repository
- 🍴 Fork it
- 📢 Share it with others
- 💡 Contribute to improve it

---

> **"Write your thoughts. Share your knowledge. Inspire the world with NoteSpace."**