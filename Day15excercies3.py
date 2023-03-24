import json
import pickle

class VedioGameCharcahter:
    def __init__(self, name, level, score, coins):
        self.name = name
        self.level = level
        self.score = score
        self.coins = coins

    def print_attributes(self):
        print("VideoGameCharachter attributes: ", self.level, self.level, self.score, self.coins)

class VideoGame:
    def __init__(self, characters=[]):
        self._dict_ = None
        if characters is None:
            characters = []
        self.characters = characters

    def print_attributes(self):
        for i in self.characters:
            print(i)

def main(o__dict__=None):
    my_char1 = VedioGameCharcahter("Robart", 7, 546, 123)

    json_data1 = json.dumps(my_char1.__dict__)
    print("Serialized :", json_data1)

    json_ser1 = json.dumps(json_data1)
    print("json Deserilization", json_ser1)

    my_char2 = VedioGameCharcahter("Mario", 3, 766, 223)

    json_data2 = json.dumps(my_char2.__dict__)
    print("Serialized :", json_data2)

    json_ser2 = json.dumps(json_data2)
    print("json Deserilization", json_ser2)

    vg = VideoGame([my_char1, my_char2])
    vg.print_attributes()
    vg_ser = pickle.dumps(vg)
    print("pickle serialization", vg_ser)
    vg_deser = pickle.loads(vg_ser)
    vg_deser.print_attributes()
    print("Pickle Deseralization", vg_deser)

    vg_ser=json.dumps(vg._dict_,default=lambda o:o__dict__)
    print("json serialization:", vg_ser)
    vg_deser = json.loads(vg_ser)
    vg_deser.print_attributes()
    print("json Deserialisation:", vg_deser)

if __name__ == "__main__":
    main()