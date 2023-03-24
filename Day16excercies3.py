import json
import codecs
def main():
    with open(r"C:\Users\Shubham\Downloads\countries_data.json", "r") as f:
        json_dict = json.load(f)
    print('json Deserilization:', json_dict)

if __name__ == "__main__":
    main()
