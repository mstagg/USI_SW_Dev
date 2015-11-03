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

3. Install mysql: http://dev.mysql.com/downloads/installer/

4. Set the mysql password to 'password' for now

5. Add the following to your system PATH: 'C:\Program Files\MySQL\MySQL Server 5.7\bin'

6. Run 'mysql -u root -p' and enter the password

7. Create a database called 'classprogram'

8. Download and install mysql-connector (x86-64): http://dev.mysql.com/downloads/connector/c/6.0.html#downloads

9. Copy 'C:\Program Files (x86)\MySQL\MySQL Connector C 6.0.2' to 'C:\Program Files\MySQL'

10. Navigate to USI_SW_Dev folder and run 'python manage.py migrate'

11. You can now start the serve by running 'python manage.py runserver' in the USI_SW_Dev folder

