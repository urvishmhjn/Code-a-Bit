%matplotlib notebook
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from ipywidgets import interact, interactive, fixed, interact_manual
import ipywidgets as widgets
plt.style.use('seaborn')


df = pd.read_csv('Dataset.csv')
df.drop(['Unnamed: 0'], 1, inplace=True)
df['Time Serie'] = pd.to_datetime(df['Time Serie'])
df = df.replace('ND', np.NaN)
df.dropna(inplace=True)

df[[ 'AUSTRALIA - AUSTRALIAN DOLLAR/US$','EURO AREA - EURO/US$', 'NEW ZEALAND - NEW ZELAND DOLLAR/US$','UNITED KINGDOM - UNITED KINGDOM POUND/US$', 'BRAZIL - REAL/US$','CANADA - CANADIAN DOLLAR/US$', 'CHINA - YUAN/US$','HONG KONG - HONG KONG DOLLAR/US$', 'INDIA - INDIAN RUPEE/US$','KOREA - WON/US$', 'MEXICO - MEXICAN PESO/US$','SOUTH AFRICA - RAND/US$', 'SINGAPORE - SINGAPORE DOLLAR/US$','DENMARK - DANISH KRONE/US$', 'JAPAN - YEN/US$','MALAYSIA - RINGGIT/US$', 'NORWAY - NORWEGIAN KRONE/US$','SWEDEN - KRONA/US$', 
	'SRI LANKA - SRI LANKAN RUPEE/US$','SWITZERLAND - FRANC/US$', 'TAIWAN - NEW TAIWAN DOLLAR/US$','THAILAND - BAHT/US$']] = (
	df[['AUSTRALIA - AUSTRALIAN DOLLAR/US$','EURO AREA - EURO/US$', 'NEW ZEALAND - NEW ZELAND DOLLAR/US$','UNITED KINGDOM - UNITED KINGDOM POUND/US$', 'BRAZIL - REAL/US$','CANADA - CANADIAN DOLLAR/US$', 'CHINA - YUAN/US$','HONG KONG - HONG KONG DOLLAR/US$', 'INDIA - INDIAN RUPEE/US$','KOREA - WON/US$', 'MEXICO - MEXICAN PESO/US$',
	'SOUTH AFRICA - RAND/US$', 'SINGAPORE - SINGAPORE DOLLAR/US$','DENMARK - DANISH KRONE/US$', 'JAPAN - YEN/US$','MALAYSIA - RINGGIT/US$', 'NORWAY - NORWEGIAN KRONE/US$','SWEDEN - KRONA/US$', 'SRI LANKA - SRI LANKAN RUPEE/US$','SWITZERLAND - FRANC/US$', 'TAIWAN - NEW TAIWAN DOLLAR/US$','THAILAND - BAHT/US$']]
	.apply(pd.to_numeric))

dollars = []
for d in df.columns:
    if ' - ' in d:
        dollars.append(d[((d.find(' - ')+3)):])
    else:
        dollars.append(d)
dollars = dollars[1:]
lst = []
for data in df.columns:
    lst.append(data[:(data.find(' - '))])
lst[0] = 'Time'
df.columns = lst
df = df.set_index(df['Time'])

print(df.head(3))


df_developed = df[['AUSTRALIA', 'NEW ZEALAND', 'UNITED KINGDOM', 'CANADA', 'HONG KONG', 'DENMARK' ,'JAPAN' ,'NORWAY', 'SWEDEN', 'SWITZERLAND', 'TAIWAN']]
# KOREA IS REMOVED
df_undeveloped = df[['EURO AREA', 'BRAZIL', 'CHINA', 'INDIA', 'MEXICO', 'SOUTH AFRICA', 'SINGAPORE', 'MALAYSIA', 'SRI LANKA', 'THAILAND']]

def korea(Include_Korea):
    if Include_Korea == True:
        df_developed = df[['AUSTRALIA', 'NEW ZEALAND', 'UNITED KINGDOM', 'CANADA','KOREA', 'HONG KONG', 'DENMARK' ,'JAPAN' ,'NORWAY', 'SWEDEN', 'SWITZERLAND', 'TAIWAN']]

        plt.figure(figsize=(9.5, 6))
        plt.plot(df.index, df_developed.mean(axis=1), label='Developed Countries')
        plt.plot(df.index, df_undeveloped.mean(axis=1), label='Developing Countries')
        plt.xlabel('Date')
        plt.ylabel('Mean Exchange Rate')
        plt.title('Difference Exchange Rate per US$ between Developed and Developing Countries')
        plt.legend();
        
    else:
        df_developed = df[['AUSTRALIA', 'NEW ZEALAND', 'UNITED KINGDOM', 'CANADA', 'HONG KONG', 'DENMARK' ,'JAPAN' ,'NORWAY', 'SWEDEN', 'SWITZERLAND', 'TAIWAN']]

        plt.figure(figsize=(9.5, 6))
        plt.plot(df.index, df_developed.mean(axis=1), label='Developed Countries')
        plt.plot(df.index, df_undeveloped.mean(axis=1), label='Developing Countries')
        plt.xlabel('Date')
        plt.ylabel('Mean Exchange Rate')
        plt.title('Difference in Exchange Rates per US$ between Developed and Developing Countries')
        plt.legend();

interact(korea, Include_Korea=False);

dic = {}
for d in [ 'AUSTRALIA - AUSTRALIAN DOLLAR/US$','EURO AREA - EURO/US$', 'NEW ZEALAND - NEW ZELAND DOLLAR/US$','UNITED KINGDOM - UNITED KINGDOM POUND/US$', 'BRAZIL - REAL/US$','CANADA - CANADIAN DOLLAR/US$', 'CHINA - YUAN/US$','HONG KONG - HONG KONG DOLLAR/US$', 'INDIA - INDIAN RUPEE/US$','KOREA - WON/US$', 'MEXICO - MEXICAN PESO/US$','SOUTH AFRICA - RAND/US$', 'SINGAPORE - SINGAPORE DOLLAR/US$','DENMARK - DANISH KRONE/US$', 'JAPAN - YEN/US$','MALAYSIA - RINGGIT/US$', 'NORWAY - NORWEGIAN KRONE/US$','SWEDEN - KRONA/US$', 'SRI LANKA - SRI LANKAN RUPEE/US$','SWITZERLAND - FRANC/US$', 'TAIWAN - NEW TAIWAN DOLLAR/US$','THAILAND - BAHT/US$']:
    dic[d[:d.find(' - ')]] = d[d.find(' - ')+3:]

# sns.set_style('darkgrid')
colors1 = ['#ebba34', '#20e8a9', '#208ee8', '#f50035', '#07e03d', '#f7e628', '#cc190c', '#3ac912', '#126ac9']
colors2 = ['#5bc404', '#9B2335', '#DFCFBE', '#55B4B0', '#E15D44', '#7FCDCD', '#BC243C', '#C3447A', '#98B4D4']

def interactives(Years, Country1='AUSTRALIA', Country2='NEW ZEALAND'):
    plt.figure(figsize=(9.5,6));
    
    if Years=='ALL' and Country2 != 'NULL':
        plt.plot(df.index, df[Country1], picker=2, alpha=0.75, color=np.random.choice(colors1), label='{}'.format(Country1));
        plt.plot(df.index, df[Country2], picker=2, alpha=0.75, color=np.random.choice(colors2), label='{}'.format(Country2));
        plt.title('Comparison Between Two Countries (Interactive Plot)');
        plt.xlabel('Date')
        plt.ylabel('{}\n{}'.format(dic[Country1], dic[Country2]))
        plt.legend()
        
    elif Years == 'ALL' and Country2 == 'NULL':
        plt.plot(df.index, df[Country1], picker=2, alpha=0.75, color=np.random.choice(colors1), label='{}'.format(Country1));
        plt.title('Exchange Rate V/S Years')
        plt.xlabel('Date')
        plt.ylabel('Exchange Rate')
        plt.legend()
    elif Years !='ALL' and Country2 != 'NULL':
        plt.plot(df[Years].index, df[Years][Country1], picker=2, alpha=0.75, color=np.random.choice(colors1), label='{}'.format(Country1));
        plt.plot(df[Years].index, df[Years][Country2], picker=2, alpha=0.75, color=np.random.choice(colors2), label='{}'.format(Country2));
        plt.legend()
        plt.title('Comparison Between Two Countries (Interactive Plot)');
        plt.xlabel('Year {}'.format(Years))
        plt.ylabel('{}\n{}'.format(dic[Country1], dic[Country2]))
        
    else:
        plt.plot(df[Years].index, df[Years][Country1], picker=2, alpha=0.75, color=np.random.choice(colors1), label='{}'.format(Country1));
        plt.xlabel('Year {}'.format(Years))
        plt.ylabel('Exchange Rate')
        plt.legend()
        plt.title('Exchange Rate in {}',format(Years))
   
    
drop_down_menu = ['AUSTRALIA', 'EURO AREA', 'NEW ZEALAND', 'UNITED KINGDOM', 'BRAZIL','CANADA', 'CHINA', 'HONG KONG', 'INDIA', 'KOREA', 'MEXICO', 'SOUTH AFRICA', 'SINGAPORE', 'DENMARK','JAPAN','MALAYSIA', 'NORWAY','SWEDEN','SRI LANKA','SWITZERLAND','TAIWAN','THAILAND']
drop_down_menu1 = ['NULL', 'AUSTRALIA', 'EURO AREA', 'NEW ZEALAND', 'UNITED KINGDOM', 'BRAZIL','CANADA', 'CHINA', 'HONG KONG', 'INDIA', 'KOREA', 'MEXICO', 'SOUTH AFRICA', 'SINGAPORE', 'DENMARK','JAPAN','MALAYSIA', 'NORWAY','SWEDEN','SRI LANKA','SWITZERLAND','TAIWAN','THAILAND']
year_menu = ['ALL', '2000', '2001', '2002', '2003', '2004', '2005', '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019']

plt.tight_layout()
interact(interactives, Country1=drop_down_menu, Years=year_menu, Country2=drop_down_menu1);


