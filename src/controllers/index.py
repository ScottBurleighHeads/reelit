from flask import Blueprint, render_template
import requests, json
index = Blueprint("index",__name__)

@index.route("/home",methods=["GET"])
def home():
    return render_template("index.html")

@index.route("/getTemplates",methods=["GET","POST"])
def get_templates():
    response = requests.get(f"https://my-json-server.typicode.com/reelit/reelittakehome/templates")
    list_response = json.loads(response.text)

    genre_list = []
    for item in list_response:
        if item['template_genre']=='genre_1':
            genre_list.append(item)

    holder = list_response[0]
    for num,item in enumerate(list_response):
        if  item["total_length"] < holder["total_length"]:
            temp = list_response[num]
            list_response[num]=holder
            holder=temp
        else:
            holder = list_response[num]
    
    list_response.reverse()
    filterOrder = []
    for item in list_response:
        if item['template_genre']=='genre_1':
            filterOrder.append(item)
    
    names = ["Filtered","Ordered","Filtered and Ordered"]
    dictList=[genre_list,list_response,filterOrder]
                
    return render_template("data.html",dictList=dictList,names=names)