import datetime

if __name__=='__main__':
    print(datetime.date.today().strftime('%d/%m/%Y'))

mi=datetime.date(1999,9,9)
print(mi.strftime('%d/%m/%Y'))
mi=mi+datetime.timedelta(days=10)
print(mi.strftime('%d/%m/%Y'))
mi=mi.replace(year=mi.year+1)
print(mi.strftime('%d/%m/%Y'))
