# Electronics store
The main goal of this project is to create a backend API for store where people can buy electronic devices, fore example
Sulpak, Technodom, Alser and other.
## Apps
* api - application that has a basic structure of the project
* auth_ - authorization and authentication of the project
* cart - order process with profile authorization
## Installation
1. Install Django Project
2. Create virtualenv
3. Install packages
```bash
pip install -r requirements.txt
```
4. Make migrations
```bash
python manage.py makemigrations
python manage.py migrate
```
5. Run the Project
```bash
python manage.py runserver
```