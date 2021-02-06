import machine

print("Unique ID:")
print(" ".join([ "{:02x}".format(i) for i in machine.unique_id()]))

print("\nGoing to Sleep for 2seconds\n")
machine.lightsleep(2000)
print("Woke-up!")