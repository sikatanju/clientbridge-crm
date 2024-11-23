ClientBridge CRM

ClientBridge CRM is a simple Customer Relationship Management (CRM) system built with Django, designed to streamline client management for small to medium-sized businesses. This application helps organize and track customer data, interactions, and relationships, making it easy to manage client information and enhance engagement.

Key Features

User Authentication: Secure login system using Django's built-in authentication. Users are categorized as organizations by default.
Lead Management: Create, track, and manage leads effectively.
Agent Assignment: Assign agents to leads for streamlined client relationship management.
Progress Updates: Keep tabs on lead progress with easy updates.
CRUD Operations: Comprehensive Create, Read, Update, Delete support for efficient data management.

Tech Stack
Frontend: Django templates + Tailwind CSS 🌐 for a modern, responsive UI.
Backend: Powered by Django ⚙️ for fast and scalable development.
Database: PostgreSQL 🗄️ for reliable and robust data storage.
Deployment: Hosted on DigitalOcean ☁️ for scalability and reliability.

Project Structure

The codebase is well-structured with dedicated applications for managing agents and leads, organized static files and templates, and environment-based configurations for database and security settings.

Directory Overview

clientbridge-crm/
│
├── djangocrm/                 # Main Django project directory
│   ├── settings.py            # Project settings
│   ├── urls.py                # URL routing configuration
│   ├── wsgi.py                # WSGI configuration
│   ├── asgi.py                # ASGI configuration
│   ├── .env                   # Environment variables file
│   └── ...
│
├── agents/                    # Application for managing agents
│   └── ...
│
├── leads/                     # Application for managing leads
│   └── ...
│
├── static/                    # Static files directory
├── templates/                 # HTML templates directory
├── migrations/                # Database migration files
├── manage.py                  # Command-line utility for administrative tasks
└── requirements.txt           # Project dependencies

Installation
To set up the project locally:
Clone the repository:
bash
git clone https://github.com/sikatanju/clientbridge-crm.git
cd clientbridge-crm

Create a virtual environment:
bash
python -m venv env
source env/bin/activate  # On Windows use `env\Scripts\activate`

Install dependencies: pip install -r requirements.txt

Set up your database in PostgreSQL and configure the .env file with your database credentials.

Run migrations: python manage.py migrate

Start the development server: python manage.py runserver

Access the application at http://127.0.0.1:8000.

Live Application
You can check out the live application here: [ClientBridge CRM on DigitalOcean](https://urchin-app-butz5.ondigitalocean.app/)

Contribution
Contributions are welcome! Please feel free to submit issues or pull requests on GitHub.

License
This project is licensed under the MIT License - see the LICENSE file for details. Feel free to modify any sections as needed or add more specific details relevant to your project!
