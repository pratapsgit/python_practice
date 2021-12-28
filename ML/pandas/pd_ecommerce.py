import numpy as np
import pandas as pd


def operations():
    # Read eCommerce -purchases csv file and set it to a dataframe called ecom
    ecom = pd.read_csv('/home/pratap/MyWorks/python_prog/python_practice/ML/pandas/Ecommerce Purchases')
    print(ecom)

    # Check the head of the dataframe
    print("head of dataframe")
    print(ecom.head())

    # How many rows and columns are there?
    print(ecom.info())

    print("Columns")
    print(ecom.columns)

    print("Indexes")
    print(ecom.index)

    # What is the average purchase price
    print("Average purchase price")
    print(ecom['Purchase Price'].mean())

    # What were the highest and lowest purchase prices?
    print("Highest and lowest purchase prices")
    print(ecom['Purchase Price'].max())
    print(ecom['Purchase Price'].min())

    # How many people have English 'en' as their Language of choice on the website ?
    print(ecom[ecom['Language'] == 'en']['Language'].value_counts())

    # How many people have the job title of "Lawyer" ?
    print("people with job title as Lawyer")
    print(ecom[ecom['Job'] == 'Lawyer']['Job'].value_counts())

    # How many people made the purchase during the AM and how many people made the purchase during PM?
    print("people made purchase during AM are")
    print(len(ecom[ecom['AM or PM'] == 'AM'].index))

    print("people made purchase during PM are")
    print(ecom[ecom['AM or PM'] == 'PM']['AM or PM'].count())

    # What are the 5 most common job titles?
    print("5 most common Job counts")
    print(ecom['Job'].value_counts().head())

    # Someone made a purchase  that came from Lot: "90 WT", What was the purchase price for this transaction ?
    print("90 WT purchase price")
    print(ecom[ecom['Lot'] == "90 WT"]['Purchase Price'])

    # What is the email of the person with the following Credit card number 4926535242672853
    print("email id of the person with credit card number 4926535242672853")
    print(ecom[ecom['Credit Card'] == 4926535242672853]['Email'])

    # How many people have American Express as their Credit Card Provider and made a purchase above $95 ?
    print("American Express credit card purchase abobe $95")
    print(len(ecom[(ecom['CC Provider'] == 'American Express') & (ecom['Purchase Price'] > 95)].index))

    # How many people have a credit card that expires in 2025 ?
    print("People with creedit card that expires in 2025")
    print(len(ecom[ecom['CC Exp Date'].apply(lambda x : (x.split('/'))[1] == '25')].index))

    # What are the top 5 most popular email providers/hosts?
    print("most popular email providers/ hosts?")
    ecom['Domains'] = ecom['Email'].apply(lambda x : (x.split('@'))[1])
    print(ecom['Domains'].value_counts().head())

if __name__ == "__main__":
    operations()