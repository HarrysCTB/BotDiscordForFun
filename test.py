import time

minutes = 0.

print("Le minuteur démarre maintenant...")

for i in range(minutes, 0, -1):
    print(i, "minutes restantes")
    time.sleep(60)

print("good")
