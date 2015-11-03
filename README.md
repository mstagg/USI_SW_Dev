DEV-STABLE BRANCH

Evansville Day School webapp for USI software development class. Powered by Django, ran on Apache2.

To convert DEV BRANCH to PRODUCTION BRANCH:
	1. Move wsgi.py file from USI_SW_Dev/evvdayschool/ to USI_SW_Dev/evvdayschool/apache
	2. In USI_SW_Dev/evvdayschool/settings.py, change the database name and password to the corresponding credentials you have stored on the server
