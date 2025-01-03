# ClientBridge CRM

![chrome_9VT7BIFxnP](https://github.com/user-attachments/assets/de5d3f17-4322-4581-823a-de1198f43271)

## Introduction
ClientBridge-CRM is a streamlined customer relationship management (CRM) application designed to simplify the process of managing leads and the agents responsible for handling them. Built for organizations aiming to enhance their client interaction workflow, this tool provides an intuitive platform for tracking and organizing leads efficiently.

<br />

## Key Features
- **User Authentication:** Secure login system using Django's built-in authentication...
- **Lead Management:** Create, track, and manage leads effectively...
- **Agent Assignment:** Assign agents to leads for streamlined client relationship...
- **Progress Updates:** Keep tabs on lead progress with easy updates...
- **CRUD Operations:** Comprehensive Create, Read, Update, Delete support...

<br />

## Tech Stack
[![Python](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=fff)](#)
[![Django](https://img.shields.io/badge/Django-%23092E20.svg?logo=django&logoColor=white)](#)
[![TailwindCSS](https://img.shields.io/badge/Tailwind%20CSS-%2338B2AC.svg?logo=tailwind-css&logoColor=white)](#)
[![Postgres](https://img.shields.io/badge/Postgres-%23316192.svg?logo=postgresql&logoColor=white)](#)
[![DigitalOcean](https://img.shields.io/badge/DigitalOcean-%230167ff.svg?logo=digitalOcean&logoColor=white)](#)

- **Frontend:** Django templates + Tailwind CSS 🌐...
- **Backend:** Powered by Django ⚙️...
- **Database:** PostgreSQL 🗄️...
- **Deployment:** Hosted on DigitalOcean ☁️...

<br />

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/sikatanju/clientbridge-crm.git
   ```

2. Navigate to the project directory:
   ```bash
   cd clientbridge-crm
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Set up the database:
   ```bash
   python manage.py migrate
   ```
5. Run the development server:
      ```bash
   python manage.py runserver
   ```

<br />

## Usage

1. Log In to the System
Use your credentials to securely log in.
New users can register if the system allows self-registration or contact the admin to create an account.

2. Manage Leads
Create a New Lead: Navigate to the "Leads" section and add details like name, contact information, and status.
Update Lead Information: Edit existing lead details to reflect progress or changes.
Delete Leads: Remove outdated or irrelevant leads to keep your data clean and organized.
View and Filter Leads: Use filters or search functionality to quickly find specific leads.

3. Manage Agents
Add Agents: Go to the "Agents" section and create profiles for team members who handle leads.
Assign Agents to Leads: Allocate leads to agents based on availability or expertise.
Edit Agent Details: Update agent profiles when necessary.
Reassign Leads: Change lead assignments to ensure optimal workflow.

4. Monitor Progress
Use the dashboard to track the status of leads and agent activity.
Visual indicators or reports provide insights into overall performance.

5. Log Out
End your session securely by logging out of the system.

<br />

## License
This project is licensed under the MIT License...
