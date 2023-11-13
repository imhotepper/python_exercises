def hello_world(name: str = 'world!'):
    print(f'Hello, {name}')


if __name__ == "__main__":
    hello_world()
    print("What's your name?")
    name = input()
    hello_world(name)
