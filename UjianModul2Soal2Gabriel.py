import mysql.connector
import matplotlib.pyplot as plt
import numpy as np


# Nomor 1
""" db = mysql.connector.connect(
    host='localhost',
    user='root',
    password='Th_697203',
    database='World'
)
kursor = db.cursor()
qry = '''
    select d.Name as Negara, d.Population as Populasi_Negara
    from city c, country d
    where d.Name like '%Brunei%' and d.Capital = c.ID
    or d.Name like'%Cambodia%' and d.Capital = c.ID
    or d.Name like'%East Timor%' and d.Capital = c.ID
    or d.Name like'%Indonesia%' and d.Capital = c.ID
    or d.Name like'%Laos%' and d.Capital = c.ID
    or d.Name like'%Malaysia%' and d.Capital = c.ID
    or d.Name like'%Myanmar%' and d.Capital = c.ID
    or d.Name like'%Philippines%' and d.Capital = c.ID
    or d.Name like'%Singapore%' and d.Capital = c.ID
    or d.Name like'%Thailand%' and d.Capital = c.ID
    or d.Name like'%Vietnam%' and d.Capital = c.ID
    order by d.Name;
'''
x = []
y = []
kursor.execute(qry)
data = kursor.fetchall()

for d in data:
    x.append(d[0])
    y.append(d[1])
arrx = np.array(x)
arry = np.array(y)
arrx2 = np.array([1,2,3,4,5,6,7,8,9,10,11])
warna = ['Cyan', 'Orange', 'Green', 'Red', 'Purple', 'Brown', 'Pink', 'Grey', 'Yellow', 'Cyan', 'Blue']

plt.style.use('seaborn')
plt.bar(arrx2, arry, color=warna)
i = 0.75
for d in data:  
    plt.text(i, d[1] + 1000000, str(d[1]))
    i += 1
plt.xticks(arrx2, arrx, rotation=45)
plt.xlabel('Negara')
plt.ylabel('Populasi(x100jt jiwa)')
plt.title('Populasi Negara ASEAN')
plt.grid(True)
plt.show() """
# ===========================================================================

# Nomor 2
""" db = mysql.connector.connect(
    host='localhost',
    user='root',
    password='Th_697203',
    database='World'
)
kursor = db.cursor()
qry = '''
    select d.Name as Negara, d.Population as Populasi_Negara
    from city c, country d
    where d.Name like '%Brunei%' and d.Capital = c.ID
    or d.Name like'%Cambodia%' and d.Capital = c.ID
    or d.Name like'%East Timor%' and d.Capital = c.ID
    or d.Name like'%Indonesia%' and d.Capital = c.ID
    or d.Name like'%Laos%' and d.Capital = c.ID
    or d.Name like'%Malaysia%' and d.Capital = c.ID
    or d.Name like'%Myanmar%' and d.Capital = c.ID
    or d.Name like'%Philippines%' and d.Capital = c.ID
    or d.Name like'%Singapore%' and d.Capital = c.ID
    or d.Name like'%Thailand%' and d.Capital = c.ID
    or d.Name like'%Vietnam%' and d.Capital = c.ID
    order by d.Name;
'''
x = []
y = []
kursor.execute(qry)
data = kursor.fetchall()

for d in data:
    x.append(d[0])
    y.append(d[1])
arrx = np.array(x)
arry = np.array(y)

warna = ['Cyan', 'Orange', 'Green', 'Red', 'Purple', 'Brown', 'Pink', 'Grey', 'Yellow', 'Cyan', 'Blue']

labels = arrx
sizes = arry
plt.title('Persentase Penduduk ASEAN')
plt.pie(sizes, labels=labels, autopct='%1.1f%%',
        shadow=False, startangle=0)
plt.xticks(rotation=70)
plt.show() """
# ============================================================================================
# Nomor 3
db = mysql.connector.connect(
    host='localhost',
    user='root',
    password='Th_697203',
    database='World'
)
kursor = db.cursor()
qry = '''
    select d.Name as Negara, d.GNP as Populasi_Negara
    from city c, country d
    where d.Name like '%Brunei%' and d.Capital = c.ID
    or d.Name like'%Cambodia%' and d.Capital = c.ID
    or d.Name like'%East Timor%' and d.Capital = c.ID
    or d.Name like'%Indonesia%' and d.Capital = c.ID
    or d.Name like'%Laos%' and d.Capital = c.ID
    or d.Name like'%Malaysia%' and d.Capital = c.ID
    or d.Name like'%Myanmar%' and d.Capital = c.ID
    or d.Name like'%Philippines%' and d.Capital = c.ID
    or d.Name like'%Singapore%' and d.Capital = c.ID
    or d.Name like'%Thailand%' and d.Capital = c.ID
    or d.Name like'%Vietnam%' and d.Capital = c.ID
    order by d.Name;
'''
x = []
y = []
kursor.execute(qry)
data = kursor.fetchall()

for d in data:
    x.append(d[0])
    y.append(d[1])
arrx = np.array(x)
arry = np.array(y)
arrx2 = np.array([1,2,3,4,5,6,7,8,9,10,11])
warna = ['Cyan', 'Orange', 'Green', 'Red', 'Purple', 'Brown', 'Pink', 'Grey', 'Yellow', 'Cyan', 'Blue']

plt.style.use('seaborn')
plt.bar(arrx2, arry, color=warna)
i = 0.75
for d in data:  
    plt.text(i, d[1]+1000, str(d[1]))
    i += 1
plt.xticks(arrx2, arrx, rotation=45)
plt.xlabel('Negara')
plt.ylabel('Populasi(x100jt jiwa)')
plt.title('Pendapatan Bruto Nasional ASEAN')
plt.grid(True)
plt.show()
# ============================================================================================
# Nomor 4
""" db = mysql.connector.connect(
    host='localhost',
    user='root',
    password='Th_697203',
    database='World'
)
kursor = db.cursor()
qry = '''
    select d.Name as Negara, d.SurfaceArea
    from city c, country d
    where d.Name like '%Brunei%' and d.Capital = c.ID
    or d.Name like'%Cambodia%' and d.Capital = c.ID
    or d.Name like'%East Timor%' and d.Capital = c.ID
    or d.Name like'%Indonesia%' and d.Capital = c.ID
    or d.Name like'%Laos%' and d.Capital = c.ID
    or d.Name like'%Malaysia%' and d.Capital = c.ID
    or d.Name like'%Myanmar%' and d.Capital = c.ID
    or d.Name like'%Philippines%' and d.Capital = c.ID
    or d.Name like'%Singapore%' and d.Capital = c.ID
    or d.Name like'%Thailand%' and d.Capital = c.ID
    or d.Name like'%Vietnam%' and d.Capital = c.ID
    order by d.Name;
'''
x = []
y = []
kursor.execute(qry)
data = kursor.fetchall()

for d in data:
    x.append(d[0])
    y.append(d[1])
arrx = np.array(x)
arry = np.array(y)

warna = ['Cyan', 'Orange', 'Green', 'Red', 'Purple', 'Brown', 'Pink', 'Grey', 'Yellow', 'Cyan', 'Blue']

labels = arrx
sizes = arry
plt.title('Persentase Luas Daratan ASEAN')
plt.pie(sizes, labels=labels, autopct='%1.1f%%',
        shadow=False, startangle=0)
plt.show() """