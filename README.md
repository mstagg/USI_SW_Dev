PRODUCTION BRANCH

Evansville Day School webapp for USI software development class. Powered by Django, ran on Apache2.

To convert PRODUCTION BRANCH to DEV BRANCH:
	1. Move wsgi.py file from USI_SW_Dev/evvdayschool/apache to USI_SW_Dev/evvdayschool/
	2. In USI_SW_Dev/evvdayschool/settings.py, change the database name and password to the corresponding credentials you have stored on your local machine.

To run development server on your local machine:
	1. Navigate to USI_SW_Dev
	2. After mysql is installed, in terminal run 'python manage.py migrate'. This will automatically create all the tables in the databse that you need.
	3. In terminal run 'python manage.py runserver'

To install and access mysql:
	1. In terminal run 'sudo apt-get install mysql-server'
	2. In terminal type 'mysql -u root -p'
	3. Enter password when asked
	4. Create a database called 'classprogram'
