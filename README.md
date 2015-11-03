DEV BRANCH
CURRENT URL: 127.0.0.1:8000

Evansville Day School text relay web-app for USI software development class.
This is a django powered web application running on a LAMP server. The app sends text messages to various different lists of users.


To convert DEV BRANCH to PRODUCTION BRANCH:

1. Move wsgi.py file from USI_SW_Dev/evvdayschool/ to USI_SW_Dev/evvdayschool/apache

2. In USI_SW_Dev/evvdayschool/settings.py, change the database name and password to the corresponding credentials that are stored on the server


To run on windows:

1. Download and install git: https://git-scm.com/download/win. Make sure to select the option that allows git to be used in the command prompt during installation!

2. Download and install python 2.X: https://www.python.org/downloads/release/python-2710/

3. Add the following to your system PATH: 'C:\python27' and 'C:\python27\scripts'

4. Run the command 'pip install django'

5. Install mysql: http://dev.mysql.com/downloads/installer/

6. Set the mysql password to 'password' for now

7. Add the following to your system PATH: 'C:\Program Files\MySQL\MySQL Server 5.7\bin'

8. Run 'mysql -u root -p' and enter the password

9. Create a database called 'classprogram'

10. Download and install mysql-connector (x86-64): http://dev.mysql.com/downloads/connector/c/6.0.html#downloads

11. Copy 'C:\Program Files (x86)\MySQL\MySQL Connector C 6.0.2' to 'C:\Program Files\MySQL'

12. Run 'pip install MySQL-python'

13. Navigate to USI_SW_Dev folder and run 'python manage.py migrate'

14. You can now start the serve by running 'python manage.py runserver' in the USI_SW_Dev folder


Quick Git Setup:
1. git config --global user.name "[JOHN DOE]"
2. git config --global user.name "[JDOE@EMAIL.COM]"

Quick Git Use Tutorial (This is not best practice!):

1. To download the project: git clone https://github.com/mstagg/USI_SW_Dev.git

2. To check status of tracked files: git status

3. To track changes on files: git add [FILE_NAME_TO_ADD] or *.[FILE_EXTENSION_TO_ADD]

4. To commit and save current changes as a 'bookmark': git commit -m "[COMMIT_MESSAGE]"

5. When ready to push changes up to github: git push
