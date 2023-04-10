from ngsiv2 import read_subcriptions,delete_subscriptions

status, data = read_subcriptions()

ids = [subscription["id"] for subscription in data]
delete_subscriptions(ids)
print("\nSubscripciones borradas!\n")
