class State:
    state_name = "Maharashtra"

    def __init__(self, state_id,capital):
        self.state_id=state_id
        self.capital=capital

    @classmethod
    def change_state_name(cls,state_name):
        cls.state_name=state_name

    @classmethod
    def display_state_name(cls):
        return cls.state_name

    @staticmethod
    def addition(economy):
        return economy

def main():
    s1=State(1,'Mumbai')
    print('Name:',s1.state_name,'ID:',s1.state_id,'Capital:',s1.capital)

    State.change_state_name('Pune')

    print(State.display_state_name())
    print('Name:', s1.state_name, 'ID:', s1.state_id, 'Capital:', s1.capital)


if __name__ == "__main__":
    main()

