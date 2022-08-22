# Python Appium Framework (Mobile Automation)
## Overview
This solution has been designed to test native android application using Appium with Python. In the interest of time and having hands-on expertise, I have selected Python as the Programming language.  In this challenge, my focus was on designing the scalable solution rather than automating more scenarios so that more test cases can be added in future with minimal amount of development effort. The test case has been automated to verify the login functionality of the provided APK
## Installation
1.	Download and Install the Java JDK and set JAVA_HOME env variable to your JDK folder
2.	Download and Install the Android Studio, Mark the AVD Manager to further installed to run tests on an emulator. Set ANDROID_HOME env variable to your Android SDK folder
3.	Download and Install Appium Server
4.	Download and Install Appium Inspector
5.	Download and Install PyCharm
6.	Download and Install Python. While installing python you make sure that python is added to System’s env variables (Setup will give you option to choose).
7.	Once done please execute the following commands one by one to install the required packages:
    * **pip install pytest**
    * **pip install Appium-Python-Client**
## Frameworks/Tools/Patterns used
1. Language: Python
2. Driver: Appium WebDriver - Enables user to write tests for multiple platforms (Android/IOS) using the same WebDriver API
3.	Test runner: Pytest - It is a testing framework that helps you to write simple and scalable test cases for databases, APIs, or UI. It also allows you to run tests in Parallel
4.	IDE: PyCharm
5.	Design Pattern: Page Object Model – To reducing duplication and minimization of the efforts involved in code maintenance, increase reusability, makes code more modular
6.	Android Studio: To Launch an Emulator
7.	Appium Server and Appium Inspector
## Set up Test Environment
1.	Clone the Repository https://github.com/MuhammadWaleed14/Python_Appium_Framework
2.	Checkout branch develop if isn’t already checked out.
## Execute Tests 
1.	Start Android Emulator
2.	Start Appium Server
3.	Set **Python Interpreter** in PyCharm
4.	To run tests in PyCharm:
     * Click on **Add Configuration** option
     * Click on **"+"** icon to create new configuration
     * Select **Python tests** > **Pytest**
     * Set **Working Directory** path to Tests Folder
     * Set **Target** path to test case file
     * Click on the Apply button
5.	Click on Run button

