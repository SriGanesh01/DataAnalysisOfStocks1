import pandas as pd
import numpy as np
import time as tm
import random as rd
import matplotlib.pyplot as plt

t=rd.uniform(0,0.5)
#importing datas

aapl=pd.read_csv(r"stock csv\AAPL.csv")
goog=pd.read_csv(r"stock csv\GOOG.csv")
msft=pd.read_csv(r"stock csv\MSFT.csv")
tsla=pd.read_csv(r"stock csv\TSLA.csv")
amzn=pd.read_csv(r"stock csv\AMZN.csv")

##cleaning datas

#converting data types

print("\nConverting the data type of 'Date' to datetime64[ns] in all datas")
aapl['Date']=pd.to_datetime(aapl['Date'])
goog['Date']=pd.to_datetime(goog['Date'])
msft['Date']=pd.to_datetime(msft['Date'])
tsla['Date']=pd.to_datetime(tsla['Date'])
amzn['Date']=pd.to_datetime(amzn['Date'])
tm.sleep(t)
print("Converted the datatype")

#remove unnecessory datas
print("\nFiltering according to year(From 2017 to 2021)")
aapl=aapl[aapl['Date'].dt.year>=2017]
aapl=aapl[aapl['Date'].dt.year<=2021]
goog=goog[goog['Date'].dt.year>=2017]
goog=goog[goog['Date'].dt.year<=2021]
msft=msft[msft['Date'].dt.year>=2017]
msft=msft[msft['Date'].dt.year<=2021]
tsla=tsla[tsla['Date'].dt.year>=2017]
tsla=tsla[tsla['Date'].dt.year<=2021]
amzn=amzn[amzn['Date'].dt.year>=2017]
amzn=amzn[amzn['Date'].dt.year<=2021]
tm.sleep(t)
print("All datas filtered")

#remove duplicated dates

print("\nRemoving Duplicate values")
aapl=aapl.drop_duplicates()
goog=goog.drop_duplicates()
msft=msft.drop_duplicates()
tsla=tsla.drop_duplicates()
amzn=amzn.drop_duplicates()
tm.sleep(t)
print("Duplicated values removed from all datas\n")

#import back into csv

aapl=aapl.to_csv(r"stock csv\AAPLc.csv")
goog=goog.to_csv(r"stock csv\GOOGc.csv")
msft=msft.to_csv(r"stock csv\MSFTc.csv")
tsla=tsla.to_csv(r"stock csv\TSLAc.csv")
amzn=amzn.to_csv(r"stock csv\AMZNc.csv")
tm.sleep(t)
print("All values Exported\n")

aapl1=pd.read_csv(r"stock csv\AAPLc.csv")
goog1=pd.read_csv(r"stock csv\GOOGc.csv")
msft1=pd.read_csv(r"stock csv\MSFTc.csv")
tsla1=pd.read_csv(r"stock csv\TSLAc.csv")
amzn1=pd.read_csv(r"stock csv\AMZNc.csv")
tm.sleep(t)
print("All values imported from the clean dataset\n")

def AllThing():

    def PrintData():

        print("1. AAPL")
        print("2. GOOG")
        print("3. MSFT")
        print("4. TSLA")
        print("5. AMZN")
        print("6. Back")
        
        data_value=input("Print first five data values of all company stocks:")
        if data_value == "1":
            print("Printing AAPL data:")
            print(f'\n{aapl1.head()}')
            while True:
                h=input("1. Back(1 to 1):\n")
                if h == "1":
                    PrintData()
                    break
                else:
                    continue
                    
        elif data_value == "2":
            print("\nPrinting GOOG data:")
            print(f'\n{goog1.head()}')
            while True:
                h=input("1. Back(1 to 1):\n")
                if h == "1":
                    PrintData()
                    break
                else:
                    continue
        elif data_value == "3":
            print("\nPrinting MSFT data:")
            print(f'\n{msft1.head()}')
            while True:
                h=input("1. Back(1 to 1):\n")
                if h == "1":
                    PrintData()
                    break
                else:
                    continue
        elif data_value == "4":
            print("\nPrinting TSLA data:")
            print(f'\n{tsla1.head()}')
            while True:
                h=input("1. Back(1 to 1):\n")
                if h == "1":
                    PrintData()
                    break
                else:
                    continue
        elif data_value == "5":
            print("\nPrinting AMZN data:")
            print(f'\n{amzn1.head()}')
            while True:
                h=input("1. Back(1 to 1):\n")
                if h == "1":
                    PrintData()
                    break
                else:
                    continue
        elif data_value == "6":
            AllThing()
        else:
            print("Invalid Option. Choose one of the given options")
            PrintData()
            
    def DateVolume():
        print("Date vs. Volume Graph")
        print("1. AAPL")
        print("2. GOOG")
        print("3. MSFT")
        print("4. TSLA")
        print("5. AMZN")
        print("6. Back")
        chart1=input("Enter One of the Choices(1 to 6): ")

        if chart1 == "1":
            plt.plot(aapl1['Date'], aapl1['Volume'], linestyle='dashed'
                     , linewidth=2, color='red', marker='.'
                     , markersize=4)
            plt.title('Date vs. Volume')
            plt.xlabel('Date')
            plt.ylabel('Volume')
            plt.xticks(['2017-01-04','2018-01-08','2019-01-03'
                        ,'2020-01-03','2021-01-05'])
            plt.show()
            while True:
                a=input("1. Back(1 to 1):\n")
                if a == "1":
                    DateVolume()
                    break
                else:
                    continue
                
        elif chart1 == "2":
            plt.plot(goog1['Date'], goog1['Volume'], linestyle='dashed'
                     , linewidth=2, color='red', marker='.'
                     , markersize=4)
            plt.title('Date vs. Volume')
            plt.xlabel('Date')
            plt.ylabel('Volume')
            plt.xticks(['2017-01-04','2018-01-08','2019-01-03'
                        ,'2020-01-03','2021-01-05'])
            plt.show()
            while True:
                a=input("1. Back(1 to 1):\n")
                if a == "1":
                    DateVolume()
                    break
                else:
                    continue
                
        elif chart1 == "3":
            plt.plot(msft1['Date'], msft1['Volume'], linestyle='dashed'
                     , linewidth=2, color='red', marker='.'
                     , markersize=4)
            plt.title('Date vs. Volume')
            plt.xlabel('Date')
            plt.ylabel('Volume')
            plt.xticks(['2017-01-04','2018-01-08','2019-01-03'
                        ,'2020-01-03','2021-01-05'])
            plt.show()
            while True:
                a=input("1. Back(1 to 1):\n")
                if a == "1":
                    DateVolume()
                    break
                else:
                    continue
                
        elif chart1 == "4":
            plt.plot(tsla1['Date'], tsla1['Volume'], linestyle='dashed'
                     , linewidth=2, color='red', marker='.'
                     , markersize=4)
            plt.title('Date vs. Volume')
            plt.xlabel('Date')
            plt.ylabel('Volume')
            plt.xticks(['2017-01-04','2018-01-08','2019-01-03'
                        ,'2020-01-03','2021-01-05'])
            plt.show()
            while True:
                a=input("1. Back(1 to 1):\n")
                if a == "1":
                    DateVolume()
                    break
                else:
                    continue

        elif chart1 == "5":
            plt.plot(amzn1['Date'], amzn1['Volume'], linestyle='dashed'
                     , linewidth=2, color='red', marker='.'
                     , markersize=4)
            plt.title('Date vs. Volume')
            plt.xlabel('Date')
            plt.ylabel('Volume')
            plt.xticks(['2017-01-04','2018-01-08','2019-01-03'
                        ,'2020-01-03','2021-01-05'])
            plt.show()
            while True:
                a=input("1. Back(1 to 1):\n")
                if a == "1":
                    DateVolume()
                    break
                else:
                    continue

        elif chart1 == "6":
            AllThing()

        else:
            print("Invalid Option. Choose one of the given options")
            DateVolume()

    def DateOpen():
        print("1. Comparison of Open data of all five compinies:")
        print("2. Back")
        chart2=input("Enter One of the Choices(1 to 2): ")
        if chart2 == "1":
            plt.plot(aapl1['Date'], aapl1['Open'], label='AAPL')
            plt.plot(goog1['Date'], goog1['Open'], label='GOOG')
            plt.plot(msft1['Date'], msft1['Open'], label='MSFT')
            plt.plot(tsla1['Date'], tsla1['Open'], label='TSLA')
            plt.plot(amzn1['Date'], amzn1['Open'], label='AMZN')
            plt.title('Opening Stock Prices')
            plt.xlabel('Date')
            plt.ylabel('Price')
            plt.legend()
            plt.xticks(['2017-01-04','2018-01-08','2019-01-03'
                        ,'2020-01-03','2021-01-05'])
            plt.show()
            
            b=input("1. Back(1 to 1):\n")
            if b == "1":
                AllThing()
            else:
                print("Invalid Option. Choose one of the given options")
                DateOpen()

        elif chart2 == "2":
            AllThing()

        else:
            print("Invalid Option. Choose one of the given options")
            DateOpen()

    def DateClose():
        print("1. Comparison of Close data of all five compinies:")
        print("2. Back")
        chart3=input("Enter One of the Choices(1 to 2): ")
        if chart3 == "1":
            plt.plot(aapl1['Date'], aapl1['Close'], label='AAPL')
            plt.plot(goog1['Date'], goog1['Close'], label='GOOG')
            plt.plot(msft1['Date'], msft1['Close'], label='MSFT')
            plt.plot(tsla1['Date'], tsla1['Close'], label='TSLA')
            plt.plot(amzn1['Date'], amzn1['Close'], label='AMZN')
            plt.title('Closing Stock Prices')
            plt.xlabel('Date')
            plt.ylabel('Price')
            plt.xticks(['2017-01-04','2018-01-08','2019-01-03'
                        ,'2020-01-03','2021-01-05'])
            plt.show()
            c=input("1. Back(1 to 1):\n")
            if c == "1":
                AllThing()
            else:
                print("Invalid Option. Choose one of the given options")
                DateClose()

        elif chart3 == "2":
            AllThing()

        else:
            print("Invalid Option. Choose one of the given options")
            DateClose()      

    def CompanyHigh():
        print("1. Comparison of Highest data of all five compinies:")
        print("2. Back")
        chart4=input("Enter One of the Choices(1 to 2): ")
        if chart4 == "1":
            plt.bar("AAPL", aapl1['High'].max(), color='red'
                    , edgecolor='black')
            plt.bar("GOOG", goog1['High'].max(), color='green'
                    , edgecolor='black')
            plt.bar("MSFT", msft1['High'].max(), color='blue'
                    , edgecolor='black')
            plt.bar("TSLA", tsla1['High'].max(), color='orange'
                    , edgecolor='black')
            plt.bar("AMZN", amzn1['High'].max(), color='purple'
                    , edgecolor='black')
            plt.title('Maximum Stock Prices')
            plt.ylabel('Price')
            plt.show()
            d=input("1. Back(1 to 1):\n")
            if d == "1":
                AllThing()
            else:
                print("Invalid Option. Choose one of the given options")
                CompanyHigh()
        elif chart4 == "2":
            AllThing()
            
        else:
            print("Invalid Option. Choose one of the given options")
            DateClose()

    def CompanyLow():
        print("1. Comparison of Lowest data of all five compinies:")
        print("2. Back")
        chart5=input("Enter One of the Choices(1 to 2): ")
        if chart5 == "1":
            plt.bar("AAPL", aapl1['High'].min(), color='red'
                    , edgecolor='black')
            plt.bar("GOOG", goog1['High'].min(), color='green'
                    , edgecolor='black')
            plt.bar("MSFT", msft1['High'].min(), color='blue'
                    , edgecolor='black')
            plt.bar("TSLA", tsla1['High'].min(), color='orange'
                    , edgecolor='black')
            plt.bar("AMZN", amzn1['High'].min(), color='purple'
                    , edgecolor='black')
            plt.title('Minimum Stock Prices')
            plt.ylabel('Price')
            plt.show()
            e=input("1. Back(1 to 1):\n")
            if e == "1":
                AllThing()
            else:
                print("Invalid Option. Choose one of the given options")
                CompanyHigh()
        elif chart5 == "2":
            AllThing()
            
        else:
            print("Invalid Option. Choose one of the given options")
            DateClose()

    def CompanyVolumeHigh():
        print("1. Comparison of Highest Volume data of all five compinies:")
        print("2. Back")
        chart6=input("Enter One of the Choices(1 to 2): ")
        if chart6 == "1":
            plt.bar("AAPL", aapl1['Volume'].max(), color='red'
                    , edgecolor='black')
            plt.bar("GOOG", goog1['Volume'].max(), color='green'
                    , edgecolor='black')
            plt.bar("MSFT", msft1['Volume'].max(), color='blue'
                    , edgecolor='black')
            plt.bar("TSLA", tsla1['Volume'].max(), color='orange'
                    , edgecolor='black')
            plt.bar("AMZN", amzn1['Volume'].max(), color='purple'
                    , edgecolor='black')
            plt.title('Maximum Trading Volumes')
            plt.ylabel('Volume')
            plt.show()
            f=input("1. Back(1 to 1):\n")
            if f == "1":
                AllThing()
            else:
                print("Invalid Option. Choose one of the given options")
                CompanyHigh()
        elif chart6 == "2":
            AllThing()
            
        else:
            print("Invalid Option. Choose one of the given options")
            DateClose()

    def CompanyVolumeLow():
        print("1. Comparison of Lowest Volume data of all five compinies:")
        print("2. Back")
        chart7=input("Enter One of the Choices(1 to 2): ")
        if chart7 == "1":
            plt.bar("AAPL", aapl1['Volume'].min(), color='red'
                    , edgecolor='black')
            plt.bar("GOOG", goog1['Volume'].min(), color='green'
                    , edgecolor='black')
            plt.bar("MSFT", msft1['Volume'].min(), color='blue'
                    , edgecolor='black')
            plt.bar("TSLA", tsla1['Volume'].min(), color='orange'
                    , edgecolor='black')
            plt.bar("AMZN", amzn1['Volume'].min(), color='purple'
                    , edgecolor='black')
            plt.title('Minimum Trading Volumes')
            plt.ylabel('Volume')
            plt.show()
            g=input("1. Back(1 to 1):\n")
            if g == "1":
                AllThing()
            else:
                print("Invalid Option. Choose one of the given options")
                CompanyHigh()
        elif chart7 == "2":
            AllThing()
            
        else:
            print("Invalid Option. Choose one of the given options")
            DateClose()

    def ScatterOpenVolume():
        print("Open vs. Volume")
        print("1. AAPL")
        print("2. GOOG")
        print("3. MSFT")
        print("4. TSLA")
        print("5. AMZN")
        print("6. Back")
        chart7=input("Enter One of the Choices(1 to 6): ")
        if chart7 == "1":
            plt.scatter(aapl1['Open'], aapl1['Volume'], c='red'
                        , s=50, marker='.')
            plt.title('Open vs. Volume')
            plt.xlabel('Open')
            plt.ylabel('Volume')
            plt.show()
            while True:
                h=input("1. Back(1 to 1):\n")
                if h == "1":
                    ScatterOpenVolume()
                    break
                else:
                    continue
        elif chart7 == "2":
            plt.scatter(goog1['Open'], goog1['Volume'], c='red'
                        , s=50, marker='.')
            plt.title('Open vs. Volume')
            plt.xlabel('Open')
            plt.ylabel('Volume')
            plt.show()
            while True:
                h=input("1. Back(1 to 1):\n")
                if h == "1":
                    ScatterOpenVolume()
                    break
                else:
                    continue
        elif chart7 == "3":
            plt.scatter(msft1['Open'], msft1['Volume'], c='red'
                        , s=50, marker='.')
            plt.title('Open vs. Volume')
            plt.xlabel('Open')
            plt.ylabel('Volume')
            plt.show()
            while True:
                h=input("1. Back(1 to 1):\n")
                if h == "1":
                    ScatterOpenVolume()
                    break
                else:
                    continue
        elif chart7 == "4":
            plt.scatter(tsla1['Open'], tsla1['Volume'], c='red'
                        , s=50, marker='.')
            plt.title('Open vs. Volume')
            plt.xlabel('Open')
            plt.ylabel('Volume')
            plt.show()
            while True:
                h=input("1. Back(1 to 1):\n")
                if h == "1":
                    ScatterOpenVolume()
                    break
                else:
                    continue
        elif chart7 == "5":
            plt.scatter(amzn1['Open'], amzn1['Volume'], c='red'
                        , s=50, marker='.')
            plt.title('Open vs. Volume')
            plt.xlabel('Open')
            plt.ylabel('Volume')
            plt.show()
            while True:
                h=input("1. Back(1 to 1):\n")
                if h == "1":
                    ScatterOpenVolume()
                    break
                else:
                    continue
        elif chart7 == "6":
            AllThing()
        else:
            print("Invalid Option. Choose one of the given options")
            ScatterOpenVolume()

    def ScatterVolumeClose():
        print("Close vs. Volume")
        print("1. AAPL")
        print("2. GOOG")
        print("3. MSFT")
        print("4. TSLA")
        print("5. AMZN")
        print("6. Back")
        chart8=input("Enter One of the Choices(1 to 6): ")
        if chart8 == "1":
            plt.scatter(aapl1['Close'],aapl1['Volume'], c='red', s=50
                        , marker='.')
            plt.title('Close vs. Volume')
            plt.xlabel('Close')
            plt.ylabel('Volume')
            plt.show()
            while True:
                i=input("1. Back(1 to 1):\n")
                if i == "1":
                    ScatterVolumeClose()
                    break
                else:
                    continue
        elif chart8 == "2":
            plt.scatter(goog1['Close'],goog1['Volume'], c='red', s=50
                        , marker='.')
            plt.title('Close vs. Volume')
            plt.xlabel('Close')
            plt.ylabel('Volume')
            plt.show()
            while True:
                i=input("1. Back(1 to 1):\n")
                if i == "1":
                    ScatterVolumeClose()
                    break
                else:
                    continue
        elif chart8 == "3":
            plt.scatter(msft1['Close'],msft1['Volume'], c='red', s=50
                        , marker='.')
            plt.title('Close vs. Volume')
            plt.xlabel('Close')
            plt.ylabel('Volume')
            plt.show()
            while True:
                i=input("1. Back(1 to 1):\n")
                if i == "1":
                    ScatterVolumeClose()
                    break
                else:
                    continue
        elif chart8 == "4":
            plt.scatter(tsla1['Close'],tsla1['Volume'], c='red', s=50
                        , marker='.')
            plt.title('Close vs. Volume')
            plt.xlabel('Close')
            plt.ylabel('Volume')
            plt.show()
            while True:
                i=input("1. Back(1 to 1):\n")
                if i == "1":
                    ScatterVolumeClose()
                    break
                else:
                    continue
        elif chart8 == "5":
            plt.scatter(amzn1['Close'],amzn1['Volume'], c='red', s=50
                        , marker='.')
            plt.title('Close vs. Volume')
            plt.xlabel('Close')
            plt.ylabel('Volume')
            plt.show()
            while True:
                i=input("1. Back(1 to 1):\n")
                if i == "1":
                    ScatterVolumeClose()
                    break
                else:
                    continue
        elif chart8 == "6":
            AllThing()
        else:
            print("Invalid Option. Choose one of the given options")
            ScatterOpenVolume()

    def Pie():
        print("1. Percentage of Days with Positive Returns")
        print("2. Back")
        chart9=input("Enter One of the Choices(1 to 2): ")
        if chart9 == "1":
            import matplotlib.pyplot as plt

            aapl_pos = aapl1[aapl1['Close'] > aapl1['Open']]['Date'].count()
            goog_pos = goog1[goog1['Close'] > goog1['Open']]['Date'].count()
            msft_pos = msft1[msft1['Close'] > msft1['Open']]['Date'].count()
            tsla_pos = tsla1[tsla1['Close'] > tsla1['Open']]['Date'].count()
            amzn_pos = amzn1[amzn1['Close'] > amzn1['Open']]['Date'].count()

            positives = [aapl_pos, goog_pos, msft_pos
                         , tsla_pos, amzn_pos]

            aapl_total = aapl1['Date'].count()
            goog_total = goog1['Date'].count()
            msft_total = msft1['Date'].count()
            tsla_total = tsla1['Date'].count()
            amzn_total = amzn1['Date'].count()

            totals = [aapl_total, goog_total, msft_total
                      , tsla_total, amzn_total]

            aapl_percent = (positives[0]/totals[0])*100
            goog_percent = (positives[1]/totals[1])*100
            msft_percent = (positives[2]/totals[2])*100
            tsla_percent = (positives[3]/totals[3])*100
            amzn_percent = (positives[4]/totals[4])*100
            
            percents = [aapl_percent, goog_percent, msft_percent
                        , tsla_percent, amzn_percent]
            labels = ['AAPL', 'GOOG', 'MSFT', 'TSLA', 'AMZN']
            plt.pie(percents,labels=labels)
            plt.title('Percentage of Days with Positive Returns')
            plt.show()
            j=input("1. Back(1 to 1):\n")
            if j == "1":
                AllThing()
            else:
                print("Invalid Option. Choose one of the given options")
                Pie()

        elif chart9 == "2":
            AllThing()
            
        else:
            print("Invalid Option. Choose one of the given options")
            Pie()

    def Stop():
        tm.sleep(t)
        print("Ending...")
        tm.sleep(t)
        print("Ended")
        pass

            
    tm.sleep(t)
    print()
    print("Main Menus")
    print("1. Print first five data values of all company stocks")
    print("2. Date vs. Volume Graph")
    print("3. Opening Stock Prices")
    print("4. Closing Stock Prices")
    print("5. Maximum Stock Prices")
    print("6. Minimum Stock Prices")
    print("7. Maximum Trading Volumes")
    print("8. Minimum Trading Volumes")
    print("9. Open vs. Volume")
    print("10. Close vs. Volume")
    print("11. Percentage of Days with Positive Returns")
    print("12. End")
    alpha=input("Enter One of the Choices(1 to 12): ")
    if alpha == "1":
        print()
        PrintData()
        
    elif alpha == "2":
        print()
        DateVolume()
        
    elif alpha == "3":
        print()
        DateOpen()

    elif alpha == "4":
        print()
        DateClose()

    elif alpha == "5":
        print()
        CompanyHigh()

    elif alpha == "6":
        print()
        CompanyLow()

    elif alpha == "7":
        print()
        CompanyVolumeHigh()

    elif alpha == "8":
        print()
        CompanyVolumeLow()

    elif alpha == "9":
        print()
        ScatterOpenVolume()

    elif alpha == "10":
        print()
        ScatterVolumeClose()

    elif alpha == "11":
        print()
        Pie()

    elif alpha == "12":
        print()
        Stop()

    else:
        print("\nInvalid Option. Choose one of the given options\n")
        AllThing()
        
AllThing()
