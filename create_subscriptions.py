from ngsiv2 import create_subscription

payload_motion = {
  "description": "Notify QuantumLeap of all Motion Sensor count changes",
  "subject": {
    "entities": [
      {
        "idPattern": "Motion.*"
      }
    ],
    "condition": {
      "attrs": [
        "count"
      ]
    }
  },
  "notification": {
    "http": {
      "url": "http://quantumleap:8668/v2/notify"
    },
    "attrs": [
      "count"
    ],
    "metadata": ["dateCreated", "dateModified"]
  }
}

payload_door = {
  "description": "Notify Quantum Leap every change in state of doors",
  "subject": {
    "entities": [
      {
        "idPattern": "Door.*"
      }
    ],
    "condition": {
      "attrs": [
        "state"
      ]
    }
  },
  "notification": {
    "http": {
      "url": "http://quantumleap:8668/v2/notify"
    },
    "attrs": [
      "state"
    ],
    "metadata": ["dateCreated", "dateModified"]
  }
}


payload_lamp = {
  "description": "Notify Quantum Leap to sample Lamp changes every five seconds",
  "subject": {
    "entities": [
      {
        "idPattern": "Lamp.*"
      }
    ],
    "condition": {
      "attrs": [
        "luminosity",
        "location"
      ]
    }
  },
  "notification": {
    "http": {
      "url": "http://quantumleap:8668/v2/notify"
    },
    "attrs": [
      "luminosity", "location"
    ],
    "metadata": ["dateCreated", "dateModified"]
  },
  "throttling": 5
}

payloads = [payload_motion, payload_door, payload_lamp]
for payload in payloads:
    create_subscription(payload)

print("\nSubscripciones creadas!\n")