import inspect

# Get everything (methods, properties, attributes)
all_members = inspect.getmembers(str)

# print(all_members)

# Get only data attributes (ignoring callables/methods)
data_attributes = [
    m[0] for m in all_members if callable(m[1]) and not m[0].startswith("_")
]
print(*data_attributes, sep="\n")
