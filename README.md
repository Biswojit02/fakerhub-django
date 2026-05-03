# FakerHub - Realistic Test Data Generator for Django

<div align="center">

![GitHub license](https://img.shields.io/badge/license-MIT-blue.svg)
![Python Version](https://img.shields.io/badge/python-3.8%2B-brightgreen)
![Django Version](https://img.shields.io/badge/django-3.2%2B-darkgreen)
![Status](https://img.shields.io/badge/status-active-success)
![Faker Library](https://img.shields.io/badge/faker-latest-orange)

**A Django web application for generating, customizing, and managing realistic test data using the Faker library. Perfect for development, testing, and database seeding.**

</div>

---

## 🎯 Overview

**FakerHub** is a powerful Django-based web application that simplifies the process of generating realistic fake data for testing and development purposes.

Whether you're building a test database, populating a staging environment, or learning Django, FakerHub provides a user-friendly solution with customizable data generation options and multiple export formats.

The project demonstrates how to:
- Populate a database with fake data
- Retrieve records using Django ORM
- Apply filtering and ordering
- Display data dynamically on a web page

This project is useful for understanding **backend development**, **ORM queries**, and **data handling in Django**.

---

## ✨ Features

- Generate fake student records using Faker
- Store student data in a MySQL database
- Display student records in a styled HTML table
- Manage records through Django admin
- Sort students by name in the student list view
- Practice Django ORM filtering and ordering queries
- Organized template and static file structure

---

## 🎬 Quick Start

### Prerequisites

- Python 3.8+
- pip or conda
- Virtual environment (recommended)
- 2GB disk space

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/Biswojit02/fakerhub-django.git
   cd fakerhub-django
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure Django settings**
   ```bash
   # Update database settings in settings.py if needed
   ```
4. **MySQL Database Setup**

    Create a MySQL database:
    
    ```sql
    CREATE DATABASE DBName;
    ```
    
    Update `fakerproject/settings.py` with your local MySQL credentials:
    
    ```python
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'DBName',
            'USER': 'root',
            'PASSWORD': 'password',
        }
    }
    ```
    
    Replace these values with your actual database details:
    
    | Setting | Description |
    | --- | --- |
    | `NAME` | MySQL database name |
    | `USER` | MySQL username |
    | `PASSWORD` | MySQL password |


5. **Apply database migrations**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

6. **Create superuser (admin account)**
   ```bash
   python manage.py createsuperuser
   ```
   Then open:
    ```bash
    http://127.0.0.1:8000/admin/
    ```

7. **Generate Fake Data**

    Run the data generation script:
    
    ```bash
    python populate.py
    ```
    
    Enter the number of records you want to insert:
    
    ```text
    Enter the number of records to be inserted: 50
    ```
    
    Example generated student data includes:
    
    - Roll number
    - Full name
    - Date of birth
    - Marks
    - Email address
    - Phone number
    - Address

8. **Run development server**
   ```bash
   python manage.py runserver
   ```

9. **Access the application**
   - Admin panel: `http://127.0.0.1:8000/admin`
   - Faker dashboard: `http://127.0.0.1:8000/students`

---

## Application Flow

```text
populate.py
    |
    v
Faker generates student records
    |
    v
Student model saves data to MySQL
    |
    v
student_data_view fetches records
    |
    v
student.html renders the table
    |
    v
student.css styles the page
```

---

## 📚 Documentation

### Project Structure

```
fakerhub-django/
|
├── fakerproject/               # Main Django project config
|   ├── __init__.py
|   ├── asgi.py                 # ASGI config for production
|   ├── settings.py             # Database, apps, middleware config 
|   ├── urls.py                 # Main URL routing
|   └── wsgi.py                 # WSGI config for production
│
├── fakerapp                    # Core Django application
|   ├── migrations/             # Database migration files      
|   |   ├── 0001_initial.py
|   |   └── __init__.py
|   ├── admin.py                # Django admin configuration
|   ├── apps.py                 # App configuration
|   ├── models.py               # Database models
|   ├── tests.py                # Unit tests
|   └── views.py                # View functions (controllers)
|
├── templates/
|   └── fakerapp/               # App-specific templates
|       └── student.html        # Home/dashboard
|
├── static/
|   └── css/
|       └── student.css         # Custom styling
|
├── manage.py                   # Django CLI
├── populate.py
├── .gitignore                  # Git ignore rules
├── requirements.txt            # Python dependencies
├── LICENSE
└── README.md                   # Documentation
```

---

## 🛠️ Technology Stack

| Technology | Purpose |
| --- | --- |
| Python 3.12 | Backend programming language |
| Django 5.x | Web framework |
| MySQL | Database |
| Faker | Fake data generation |
| HTML | Page structure |
| CSS | Page styling |

---

## 📊 Supported Data Types

### Student Data
- ✅ Rollno
- ✅ Names (first, last, full)
- ✅ Dates of birth
- ✅ Marks
- ✅ Emails
- ✅ Phone numbers
- ✅ Addresses

---

## URL Routes

| Route | View | Description |
| --- | --- | --- |
| `/admin/` | Django admin | Manage project data |
| `/students/` | `student_data_view` | Display all student records |

## Student Model

The `Student` model is defined in `fakerapp/models.py`.

| Field | Type | Description |
| --- | --- | --- |
| `rollno` | `IntegerField` | Student roll number |
| `name` | `CharField` | Student full name |
| `dob` | `DateField` | Date of birth |
| `marks` | `IntegerField` | Student marks |
| `email` | `EmailField` | Student email address |
| `phonenumber` | `BigIntegerField` | Student phone number |
| `address` | `TextField` | Student address |

## Django ORM Practice

The view file includes useful commented examples for learning Django ORM queries.

```python
Student.objects.all().order_by('name')
Student.objects.all().order_by('-marks')
Student.objects.filter(marks__gt=80)
Student.objects.filter(marks__lt=50)
Student.objects.filter(marks__range=(60, 100))
Student.objects.filter(name__startswith='A')
Student.objects.filter(address__icontains='p')
```

## Admin Configuration

The `Student` model is registered in `fakerapp/admin.py` with these columns visible in the admin list page:

```python
list_display = ['rollno', 'name', 'dob', 'marks', 'email', 'phonenumber', 'address']
```

This makes it easier to inspect and manage generated records from the Django admin panel.

## Troubleshooting

### MySQL Connection Error

Check the following:

- MySQL server is running
- Database name exists
- Username and password are correct
- `mysqlclient` is installed
- Database settings in `settings.py` match your local MySQL setup

### No Student Data Found

Run the Faker seed script:

```bash
python populate.py
```

Then refresh:

```text
http://127.0.0.1:8000/students/
```

### Static CSS Not Loading

Confirm that `django.contrib.staticfiles` is available in `INSTALLED_APPS` and that `STATICFILES_DIRS` points to the `static` folder.

### `mysqlclient` Installation Fails

On Windows, make sure your Python version and MySQL client build are compatible. You may need MySQL development headers or a compatible prebuilt wheel.

---

## 📚 Learning Resources

- [Faker Documentation](https://faker.readthedocs.io/)
- [Django Official Docs](https://docs.djangoproject.com/)
- [Bulk Operations in Django](https://docs.djangoproject.com/en/stable/ref/models/querysets/#bulk-create)
- [Django Management Commands](https://docs.djangoproject.com/en/stable/howto/custom-management-commands/)

---

## 🤝 Contributing

Contributions are welcome! Here's how to help:

1. **Fork** the repository
2. **Create** feature branch (`git checkout -b feature/AmazingFeature`)
3. **Commit** changes (`git commit -m 'Add AmazingFeature'`)
4. **Push** to branch (`git push origin feature/AmazingFeature`)
5. **Open** Pull Request

---

## 📝 License

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

---

## 📞 Support & Contact

- 📧 **Email:** biswojitpradhan02@gmail.com
- 💬 **GitHub Issues:** [Report bugs](https://github.com/Biswojit02/fakerhub-django/issues)
- 🔗 **LinkedIn:** [linkedin.com/in/biswojit-pradhan](https://www.linkedin.com/in/biswojit-pradhan)
- 🐙 **GitHub:** [@Biswojit02](https://github.com/Biswojit02)

---

## 🙏 Acknowledgments

- **Faker Library** - For the incredible fake data generation
- **Django Community** - For excellent framework and documentation
- **Bootstrap** - For beautiful responsive UI
- **Contributors** - Everyone who helped improve this project

---

<div align="center">

### Made with ❤️ by Biswojit Pradhan

⭐ **If you found this project helpful, please give it a star!**

[⬆ Back to top](#-overview)

</div>
