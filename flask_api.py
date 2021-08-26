from flask import Flask, request, jsonify


app = Flask(__name__)

data = [{"id":1,"name":"Akshay","sname":"Waghmare","email":"name"+"sname"+"@gmail.com","phone":1111, "Tal":"Akluj","state":"Maha","course":["python","html","css"],"pincode":11},                                                    
    {"id":2,"name":"Amol","sname":"Nagrale","email":"name"+"sname"+"@gmail.com","phone":2222, "Tal":"Akluj","state":"Maha","course":["python","hadoop","javascript"],"pincode":22},                                                    
    {"id":3,"name":"Suraj","sname":"Jagtap","email":"name"+"sname"+"@gmail.com","phone":3333, "Tal":"Akluj","state":"Maha","course":["python","mongoDB","js"],"pincode":33},                                                    
    {"id":4,"name":"Saurabh","sname":"Patil","email":"name"+"sname"+"@gmail.com","phone":4444, "Tal":"Amravati","state":"Maha","course":["python","plsql","html"],"pincode":44}]                                                   
                           
@app.route('/name/<string:user>',methods=['POST'])
def add_user(user):
    new_user = {"name":user}
    data.append(new_user)

    return jsonify({"data":data})


@app.route('/name/',methods=['GET'])
def show_data():
    a = request.args.get('user')
    t = request.args.get('Tal')

    if a=="all":
        return jsonify({"data":data})

    for name in data:
        # print(name["name"])
        if name["name"]==a and name["Tal"]==t:
            return jsonify({"data":name})

    return jsonify({"message":"invalid"})


@app.route('/get/',methods=['GET'])
def show_course():
    c = request.args.get('c')
    t = request.args.get('t')

    new_data=[]
    for name in data:
        if c in name["course"] and t in name["Tal"]:
            new_data.append(name)
        else:
            return jsonify({"message":"omfg!! not found"})

    return jsonify({"data":new_data})

    


@app.route('/name/<user>',methods=['PUT'])
def update_user(user):

    got = request.json['name']
   
    for name in data:
        if name["name"] == user:
            name["name"] = got
        else:
            return jsonify({"message":f"invalid {user} user name"})
    return jsonify({"data":data})

@app.route('/name/<user>',methods=['DELETE'])
def delete_user(user):
    new_data = []
    for name in data:
        if name["name"]!=user:
            new_data.append(name)

    return jsonify({"data":new_data})

if __name__=="__main__":
    app.run(debug=True)