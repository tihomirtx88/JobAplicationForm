# 🧾 Job Application Form (Flask Project)

A feature-rich **Flask web application** for managing job applications, user authentication, and contact messages.  
Built with **Flask**, **SQLAlchemy**, **Flask-Login**, and **Bootstrap**, this project follows clean architecture principles using **Blueprints**, **OOP**, and **environment variables** for secure and maintainable development.

---

## 🚀 Features

### 🧍‍♂️ User Management
- 🔑 **User Registration** – Create an account securely (with password hashing).
- 🔐 **Login & Logout** – Authentication powered by Flask-Login.
- 👤 **Session Management** – Stay logged in between pages.
- 🚫 **Access Protection** – Certain routes are available only to authenticated users.

### 📋 Application Management
- 📝 Submit job applications (Name, Email, Date, Occupation, etc.)
- 📂 View all submitted applications (admin-style view)
- 👁️ View individual submission details

### ✉️ Contact Form
- 📬 Send contact messages through an integrated email system using Flask-Mail.
- 💌 Automatic notifications to the configured admin email.

### 🎨 UI & Frontend
- 💻 Responsive design built with **Bootstrap 5**
- 🧭 Clean navigation bar with authentication state awareness
- 🌈 Flash messages for success/error notifications
- 🎨 Custom CSS styling (`static/style.css`)

### 🧱 Architecture
- Modularized using **Blueprints**:
  - `main/` – core routes (home, about, submissions)
  - `auth/` – authentication and user routes
  - `models/` – SQLAlchemy ORM models
  - `templates/` – Jinja2 templates
  - `static/` – CSS, JS, and assets
- Organized for scalability using **OOP and clean separation of concerns**

### ⚙️ Configuration
- Uses **environment variables (`.env`)** for:
  - Database URL
  - Secret key
  - Mail server credentials

### 💾 Database
- Powered by **SQLAlchemy ORM**
- Supports **SQLite** by default (easily replaceable with PostgreSQL or MySQL)
- Automatic migrations with `Flask-Migrate` (optional)

---
