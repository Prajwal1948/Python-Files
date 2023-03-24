class A:
    def method_a(self):
        print("method A")

class B(A):
    def method_b(self):
        print("method B")

class C(A):
    def method_a(self):
        print("method C")

class D(B, C):
    def method_d(self):
        print("method D")

def main():
    print(D.mro())

if __name__ == "__main__":
    main()
