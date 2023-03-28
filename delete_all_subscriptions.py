from ngsiv2 import read_subcriptions,delete_subscription

status, data = read_subcriptions()

for subscription in data:
    id = subscription["id"]
    status = delete_subscription(id)
print("\nSubscripciones borradas!\n")
