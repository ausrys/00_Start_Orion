import gc


class MyObject:
    def __del__(self):
        print("MyObject is being garbage collected")


# Disable automatic garbage collection for demonstration
gc.disable()

print("Before object creation:")
print("Garbage collector enabled?", gc.isenabled())
print("Unreachable objects:", gc.collect())

# Create a circular reference
a = MyObject()
b = MyObject()
a.ref = b
b.ref = a

# Remove direct references
a = None
b = None

print("\nAfter dereferencing:")
print("Unreachable objects before manual collect:", gc.collect())

# Re-enable garbage collection
gc.enable()
print("\nGarbage collector re-enabled.")
