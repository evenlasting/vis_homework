import json
import csv
import os

# state = input("state name:")
# date = input("date:")

prefix = 'C:/Users/123456/Repository/Python/confirmed/'
postfix = '.csv'

def get_tree_json_data(cities,year,month,day):

    date = str(day)+'/'+str(month)+'/'+str(year)

    wrap = []

    states = cities.split(",")

    for state in states:

        with open(prefix+state+postfix,"r",encoding='utf-8') as f:
            reader = csv.reader(f)

            county_list = []
            data_list = []

            flag = 0

            for row in reader:
                if flag == 0:
                    for item in row:
                        county_list.append(item)
                    county_list.remove(county_list[0])
                    flag = 1

                if row[0] == date:
                    for item in row:
                        data_list.append(item)
                    data_list.remove(data_list[0])
                    break
            
            data_sum = 0
            count = 0
            child_list = []
            for item in county_list:
                tem_dic = {}

                tem_dic["value"]=data_list[count]
                tem_dic["name"]=county_list[count]
                tem_dic["path"]=state+"/"+county_list[count]

                child_list.append(tem_dic)
                data_sum += int(data_list[count])
                count += 1

            father = {}
            father["value"]=data_sum
            father["name"]=state
            father["path"]=state
            father["children"]=child_list

            wrap.append(father)

        # if not os.path.exists("C:/Users/123456/Repository/Python/tree_json/tree.json"):
        #     f2 = open("C:/Users/123456/Repository/Python/tree_json/tree.json",'w+')
        #     f2.close()

        # with open("C:/Users/123456/Repository/Python/tree_json/tree.json","w")as f3:
        #     json.dump(wrap,f3,indent=2)
    
    return wrap
    
