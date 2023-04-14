import requests
from bs4 import BeautifulSoup
import json
import datetime
import threading


from model_panchang import DB, SunRiseAndMoonRise, Panchang, LunarMonthAndSamvat, RashiAndNakshatra, RituAndAyana, AuspiciousTimings, InauspiciousTimings, AnandadiAndTamilYoga, NivasAndShool, OtherCalendarsAndEpoch

table_dictionary = {'sunrise_and_moonrise': SunRiseAndMoonRise, 'panchang': Panchang, 'lunar_month_and_samvat': LunarMonthAndSamvat, 'rashi_and_nakshatra': RashiAndNakshatra, 'ritu_and_ayana': RituAndAyana,
                    'auspicious_timings': AuspiciousTimings, 'inauspicious_timings': InauspiciousTimings, 'anandadi_and_tamil_yoga': AnandadiAndTamilYoga, 'nivas_and_shool': NivasAndShool, 'other_calendars_and_epoch': OtherCalendarsAndEpoch}


DB.connect()
DB.create_tables([SunRiseAndMoonRise, Panchang, LunarMonthAndSamvat, RashiAndNakshatra, RituAndAyana,
                     AuspiciousTimings, InauspiciousTimings, AnandadiAndTamilYoga, NivasAndShool, OtherCalendarsAndEpoch])

def save_data_database(given_date,dict_data):
    for item in dict_data:
        date = [int(i) for i in given_date.split('/')]
        dict_data[item].update({'date':datetime.date(day=date[0],month=date[1],year=date[2])})

        table_dictionary.get(item).create(**dict_data[item])

def make_dictionary(list):
    a = []
    b = []
    for value in list:
        a.append(value[0])
        b.append(value[1])
    return dict(zip(a, b))
    
def grab_data(date):
    geo_name = '1259229'
    date = date
    base_url = 'https://www.drikpanchang.com/panchang/day-panchang.html'
    geo_name_id_param = f'geoname-id={geo_name}'
    date_param = f'date={date}'

    url = f'{base_url}?{geo_name_id_param}&{date_param}'
    # print(url)
    rget = requests.get(url)

    soup = BeautifulSoup(rget.content, 'html.parser')

    data_write_to_file = soup.find('div', {'class', 'dpTableCardWrapper'})

    collected_data = dict()
    try:
        for index, cont in enumerate(data_write_to_file.contents):
            if index == 5:
                continue
            if index == 11:
                break

            # print(index, cont.find('h3', {'class', 'dpTableCardTitle'}).getText())
            cont_text = cont.find('h3', {'class', 'dpTableCardTitle'}).getText()
            cont_text = '_'.join((cont_text.lower().split()))
            collected_data[cont_text] = []
        #    print(index,cont .getText())
            
        #    continue
            try:
                if not cont:
                    continue
                for item in cont.find('div', {'class', 'dpTableCard'}):
                    try:
                        # zip(item.find('div',{'class','dpTableKey'}),item.find('div',{'class','dpTableValue'})):
                        for i, val in enumerate(item):
                            if i % 2 == 0:
                                current_key = val.getText().strip()
                                current_key = '_'.join((current_key.lower().split()))
                                # print(type(current_key))
                            #    print('\t',val.getText())
                                # collected_data[cont_text].update({current_key: ''})
                            else:
                                collected_data[cont_text].append(
                                    [current_key, val.getText()])
                        

                            #    print('\t\t',val.getText())
                            # input()

                        # input()
                    except Exception as e:
                        print(e, index)
                        input()
            except Exception as ee:
                print(ee, index)
                input()

    except Exception as ee:
        print(ee)
        input()

    # for the formatting of collected data
    # print(dict(zip(collected_data)))
    for iIndex, i in enumerate(collected_data):
        current_data_set = collected_data[i]
        pop_item = []
        for index, item in enumerate(current_data_set):
            # print(item)
            # print(index,item)
            if i == 'Panchang' or True:
                # continue
                if item[0] == '':
                    current_data_set[index-2][1] = current_data_set[index -
                                                                    2][1] + ' :&: ' + item[1]
                    pop_item.append(index)

            if i == 'Rashi and Nakshatra':
                if item[0] == '':
                    current_data_set[1][1] = current_data_set[1][1] + \
                        ' :&: ' + item[1]
        for pop_i in pop_item:
            current_data_set[pop_i] = []
        current_data_set = list(
            filter(lambda ls: not not ls, current_data_set))
        # date = [int(i) for i in date.split('/')]
        # current_data_set.append({'date':datetime.date(day=date[0],month=date[1],year=date[2])})
        collected_data[i] = current_data_set


    for i in collected_data:
        collected_data[i] = make_dictionary(collected_data[i])
    
    return collected_data


grbdata = grab_data('10/03/2023')
with open('json.json','w') as f:
    json.dump(grbdata,f)

initial_date = '01/05/2023'
# print( save_data_database('10/03/2001',grbdata))

for i in range(731):
    date = datetime.datetime.strptime(initial_date, '%d/%m/%Y')
    # date = date + datetime.timedelta(days=i)
    date = datetime.datetime.strftime(
        date + datetime.timedelta(days=i), '%d/%m/%Y')
    
    try:
        save_data_database(date,grab_data(date))
        # t1 = threading.Thread(target=save_data_database,args=(date,grab_data(date),))
        # t1.start()
    except Exception as ee:
        print(ee)
        # raise(ee)
    else:
        print(i)
