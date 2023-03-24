import json
import pickle

class VedioGameCharcahter:
    def __init__(self, name, level, score, coins):
        self.name = name
        self.level = level
        self.score = score
        self.coins = coins


def main():
    my_char = VedioGameCharcahter("Robart", 7, 546, 123)

    json_data = json.dumps(my_char.__dict__)
    print("Serialized :", json_data)

    pickle_data = pickle.dumps(my_char)
    print(("Serilized Pickel: ", pickle_data))

    json_deserialized_data = json.loads(json_data)
    json_my_char = VedioGameCharcahter(**json_deserialized_data)
    print("json deserliized")

    pickle_dict = pickle.loads((pickle_data))
    print("Deserilized pickel: ", pickle_dict)


if __name__ == "__main__":
    main()