# 🦅 Python-Quine
  A python code that duplicates itself so much

## **⚠️ Caution**
  Do not run this code on any device that you do not have permission from the owner of.<br>
  All consequences are the responsibility of the user.

## **⛏️ Requirements**
  The code needs [subprocess](https://pypi.org/project/subprocess.run/), sys & os libraries installed in order to work.

## **📥 Installing**

  You can install the project using these methods:

### **1️⃣ First Method**
  Downloading by github website
  Look at the top of the project files, there is a button labeled <>Code, click on it and select the last option, "Download Zip", to download the file for you.

### **2️⃣ Second Method**
  Download using git
  Download the project on the command prompt using the code below.
```cmd
  git clone https://github.com/soodi592/python-quine
```

## **🔄 Running**

First open command prompt and head to the project directory where you downloaded the project and then Run the project using python3.

```cmd
  python3 0001quine.py
```

When the code is successfully runned, you can see 0002quine.py, 0003quine.py and up to 9999quine.py.<br>
(The code must run about 2 mins to generate 9999 files, so don't close it fast.)

## **⬆️ Upgrading The Code**

In order to upgrade the code, first you need to rename the file from 0001quine.py to [how many numbers you want]quine.py, for example: 0000001quine.py.
Then go to the code file and change the numbers "4" from 10th and 14th line to The sum of the numbers you entered in the previous step, for example 000001, is 6.

### 🍫 Example

Main 10th & 14th Lines:
```
10      number = num[:4]  # Get the first four characters of the filename
11      ...
12      ...
13      ...
14      new_number = str(int(number) + 1).zfill(4)  # Increment and ensure it's 4 digits (e.g., '0002' from '0001')
```

Updated Version 10th & 14th Lines:
```
10      number = num[:6]  # Get the first sixth characters of the filename
11      ...
12      ...
13      ...
14      new_number = str(int(number) + 1).zfill(6)  # Increment and ensure it's 6 digits (e.g., '000002' from '000001')
```

Tip : it isn't mandatory to change the comments.