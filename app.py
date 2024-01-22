import os

message = os.getenv('MESSAGE')
receiver = os.getenv('RECEIVER')

print(f"Message: {message}")
print(f"Receiver: {receiver}")