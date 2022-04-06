# Cryptoloteria Test

The main objective of this project is to test the cryptopoloteria site

## Requirements

Install selenium:
```
pip install selenium
```

## Configure settings.py
On settings.py file, change line 3 and line 11
```
 3|HOST = "https://staging.cryptoloteria.mx"
...
11|METAMASK_MNEMONIC = "your have to insert your twelve words in this little space please"
```
For the url to test, and your metamask mnemonir (Twelve words of your wallet) Example:
```
 3|HOST = "https://www.google.com/"
 ...
11|METAMASK_MNEMONIC = "this are my twelve words of my own wallet it needs yours"
```

## Start the test

You only need run with python like:
```
python start_test.py
```

## Notes
Make sure that the version of your webdriver (cromedriver file) is compatible with the version of your chrome browser, if not, you can download it at the following link:
https://chromedriver.storage.googleapis.com/index.html
