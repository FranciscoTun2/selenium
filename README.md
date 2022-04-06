# Cryptoloteria_test

The main objective of this project is to test the cryptopoloteria site

## Getting started

To make it easy for you to get started with GitLab, here's a list of recommended next steps.

Already a pro? Just edit this README.md and make it your own. Want to make it easy? [Use the template at the bottom](#editing-this-readme)!

## Requeriments

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
 for the url to test, and your metamask mnemonir (Twelve words of your wallet) Example:
```
HOST = "https://www.google.com/"
METAMASK_MNEMONIC = "this are my twelve words of my own wallet it needs yours"
```

## start the test

You only need run eith python like:
```
python start_test.py
```
