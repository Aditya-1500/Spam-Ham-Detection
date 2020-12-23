# Tweet Spam-Ham-Detection
This is an ensemble based spam detection web-application that uses probablistic data-structures based on the paper: A. Singh, S. Batra, Ensemble based spam detection in social IoT using probabilistic data structures, Future Generation Computer Systems (2017), https://doi.org/10.1016/j.future.2017.09.072.

## Features of the Project

### Users can:
1. Test whether a tweet is spam or ham using the ensemble based spam detection classifier.
2. Type/Paste a single tweet or upload a file to test multiple tweets.
3. Sign-up to create an account and add custom files as database for the classifier model.
4. Login and add/update files from their profile.
5. Classify tweet(s) using model trained from their custom files (Login Required).

### The ensemble-based spam detection classifier uses the following models:
1. Quotient filter to quickly and efficiently search the parts of tweet from a list of spam urls, spam users and spam words stored in database.
2. Locally sensitive hashing using MinHash is used to get the jaccard similarity of the input tweet from a set of ham and spam tweets in the database.
3. A Machine Learning model trained on a large dataset of spam and ham tweets. The model uses a pipeline where the tweet goes through CountVectorizer, TfidfTransformer and then using Multinomial Naive Bayes from sklearn library, the model gives the prediction.

## How to Install and Run this project?

### Pre-Requisites:
1. Install Git Version Control
[ https://git-scm.com/ ]

2. Install Python Latest Version
[ https://www.python.org/downloads/ ]

3. Install Pip (Package Manager)
[ https://pip.pypa.io/en/stable/installing/ ]


### Installation
**1. Create a Folder where you want to save the project**

**2. Create a Virtual Environment and Activate**

Install Virtual Environment First
```
$  pip install virtualenv
```

Create Virtual Environment

For Windows
```
$  python -m venv env
```
For Mac/Linux
```
$  python3 -m venv env
```

Activate Virtual Environment

For Windows
```
$  .\env\scripts\activate
```

For Mac/Linux
```
$  source env/bin/activate
```

**3. Clone this project**
```
$  git clone https://github.com/Aditya-1500/Spam-Ham-Detection.git
```

Then, Enter the project
```
$ cd Spam-Ham-Detection\SMSSpamHam
```

**4. Install Requirements from 'requirements.txt'**
```python
$  pip install -r requirements.txt
```

**5. Set Allowed Hosts**

- Go to settings.py.
- Add '\*' to allowed hosts.
```python
ALLOWED_HOSTS = ['*']
```
No need to change in Mac

**6. Now Run Server**

Command for Windows:
```python
$ python manage.py runserver
```

Command for Mac/Linux:
```python
$ python3 manage.py runserver
```

## Default Credentials 

**Admin**

Username: admin<br>
Password: password

**User**

Username: user<br>
Password: user_password

## Developed By:

[**Aditya Manchanda**](https://github.com/Aditya-1500/)<br>
under the guidance of<br>
**Dr. Amritpal Singh**, Assistant Professor, CSE Department, NIT Jalandhar
