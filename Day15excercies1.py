import json
import pickle

def main():
    my_dict = {"dict1":{"name":"prajwal","age":23}, "dict1":{"name":"Shubham","age":26}}

    json_data = json.dumps(my_dict)
    print("Serialized :", json_data)

    json_dict = json.loads(json_data)
    print("Deserialized: ", json_dict)

    pickle_data = pickle.dumps(my_dict)
    print(("Serilized Pickel: ", my_dict))

    pickle_dict = pickle.loads((pickle_data))
    print("Deserilized pickel: ", pickle_dict)

if __name__ =="__main__":
    main()