# Python Appium Framework (Mobile Automation)
## Overview
This solution has been designed to test native android applications using Appium with Python. In the interest of time and already have the hands-on expertise, I have selected the Python as the Programming languages.  In this challenge, my focus was on designing the scalable solution rather than automating more scenarios so that more test cases can be added in future with minimal amount of development effort. The test case has been written on the login functionality of the provided APK
## Installation
1.	Download and Install the Java JDK and set JAVA_HOME to your JDK folder
2.	Download and Install the Android Studio mark the AVD Manager is further installed as we are moving to drive our tests on an emulator. Set ANDROID_HOME to be your Android SDK path and put in the tools and platform-tools folders to your PATH variable 
3.	Download and Install Appium Server
4.	Download and Install Appium Inspector
5.	Download and install PyCharm
6.	Download and install Python
7.	Make sure that while installing python you make sure that python is added to System’s env variables (Setup will give you option to choose).
8.	Once done please execute the following commands one by one to install the required packages:
    * **pip install pytest**
    * **pip install Appium-Python-Client**
## Frameworks/Tools/Patterns used
1.  Language: Python
2. 	Driver: Appium WebDriver - enables user to write tests for multiple platforms (Android/IOS) using the same WebDriver API
3.	Test runner: Pytest
4.	IDE: PyCharm
5.	Design Pattern: Page Object Model – To reducing duplication and minimization of the efforts involved in code
6.	Android Studio: To Launch an emulator
7.	Appium Server
8.	Appium Inspector: To identify objects
## Set up Test Environment
1.	Clone the Repository https://github.com/MuhammadWaleed14/Python_Appium_Framework
2.	Checkout branch develop if isn’t already checked out.
Execute Tests 
1.	Start Android Emulator
2.	Start Appium Server
3.	Set Python Interpreter in PyCharm
4.	To run tests in PyCharm:
i.	Click on Add Configuration
ii.	Click on ‘+’ icon to create new configuration
iii.	Select Python tests > Pytest
iv.	Set Working Directory path till Tests Folder
v.	Set Target path till test case file
vi.	Click on the Apply button
5.	Click on Run button

