from microrpc import Client

client = Client()

try:
    print(client.nonexistent())
except KeyError:
    print("Undefined remote procedure.")

print(client.add_two(1, 2))
print(client.add_two(3, 4))

