DEV BRANCH
CURRENT URL: 50.4.179.220

Evansville Day School text relay web-app for USI software development class.
This is a django powered web application running on a LAMP server. The app sends text messages to various different lists of users.

To convert DEV BRANCH to PRODUCTION BRANCH:

1. Move wsgi.py file from USI_SW_Dev/evvdayschool/ to USI_SW_Dev/evvdayschool/apache

2. In USI_SW_Dev/evvdayschool/settings.py, change the database name and password to the corresponding credentials that are stored on the server

To run on windows:

1. Download and install python 2.X: https://www.python.org/downloads/release/python-2710/

2. Add the following to your system PATH: 'C:\python27' and 'C:\python27\scripts'

3. Run the command 'pip install django'

4. Install mysql: http://dev.mysql.com/downloads/installer/

5. Set the mysql password to 'password' for now

6. Add the following to your system PATH: 'C:\Program Files\MySQL\MySQL Server 5.7\bin'

7. Run 'mysql -u root -p' and enter the password

8. Create a database called 'classprogram'

9. Download and install mysql-connector (x86-64): http://dev.mysql.com/downloads/connector/c/6.0.html#downloads

10. Copy 'C:\Program Files (x86)\MySQL\MySQL Connector C 6.0.2' to 'C:\Program Files\MySQL'

11. Run 'pip install MySQL-python'

12. Navigate to USI_SW_Dev folder and run 'python manage.py migrate'

13. You can now start the serve by running 'python manage.py runserver' in the USI_SW_Dev folder

