class A:
    def method(self):
        print("method A")

class B(A):
    def method(self):
        print("method B")
        super().method()

class C(A):
    def method(self):
        print("method C")
        super().method()

class D(B, C):
    pass

def main():
    d = D()
    d.method()

if __name__ == "__main__":
    main()
