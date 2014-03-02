from microrpc.client import create_client

client = create_client()

try:
    print(client.nonexistent())
except KeyError:
    print("Undefined remote procedure.")

print(client.add_two(1, 2))
print(client.add_two(3, 4))

