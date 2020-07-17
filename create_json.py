import json
import csv
import os


# state = input("state name:")
# date = input("date:")

prefix = 'C:/Users/123456/Repository/Python/confirmed/'
postfix = '.csv'

def get_map_json_data(cities,year,month,day):
    
    date = str(day)+'/'+str(month)+'/'+str(year)

    feature_list = []

    states = cities.split(",")

    for state in states:
        with open("C:/Users/123456/Repository/Python/new.json",'r',encoding='ISO-8859-1') as f:
            coor_data = json.load(f)
            
            with open(prefix + state + postfix,'r') as f2:
                state_data = csv.reader(f2)

                county_list = []
                data_list = []

                flag = 0

                for row in state_data:
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
                
                
                
                count = 0
                for item in county_list:
                    tem_dic = {}

                    tem_dic["type"]="Feature"

                    tem_dic["name"]=item

                    dbh = {}
                    dbh["dbh"]=data_list[count]
                    tem_dic["properties"] = dbh

                    geo = {}
                    geo["type"]="Point"
                    geo["coordinates"]=[]
                    tem_dic["geometry"]=geo

                    feature_list.append(tem_dic)

                    count += 1
                
                for item in feature_list:
                    #print(item["name"])
                    for key in coor_data.keys():
                        if coor_data[key]["name"] == state:
                            if item["name"] in coor_data[key]["county"]:
                                item["geometry"]["coordinates"]=coor_data[key]["county"][item["name"]]

    json_data = {}
    json_data["type"]="FeatureCollection"
    json_data["features"]=feature_list

    # if not os.path.exists("C:/Users/123456/Repository/Python/map_json/map.json"):
    #     f2 = open("C:/Users/123456/Repository/Python/map_json/map.json",'w+')
    #     f2.close()

    # with open("C:/Users/123456/Repository/Python/map_json/map.json","w") as f3:
    #     json.dump(json_data,f3,indent=2)

    return json_data

#print("Done")