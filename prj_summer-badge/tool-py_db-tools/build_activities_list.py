from pandas import read_csv

activities_list = read_csv("activities.csv").fillna("").to_dict(orient='records')

out_list = [i["activities"] for i in activities_list]

print(out_list)