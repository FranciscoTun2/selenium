# Cryptoloteria Test

The main objective of this project is to test the cryptopoloteria site

## Requirements

Install selenium:
```
pip install selenium
```

## Configure Settings
On settings.py file, change line 3 and line 11
```
HOST = "https://staging.cryptoloteria.mx"
METAMASK_MNEMONIC = "your have to insert your twelve words in this little space please"
```
For the url to test, and your metamask mnemonir (Twelve words of your wallet) Example:
```
HOST = "https://www.google.com/"
METAMASK_MNEMONIC = "this are my twelve words of my own wallet it needs yours"
```

## Start the test

You only need run with python like:
```
python start_test.py
```
