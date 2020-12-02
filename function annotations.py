def kinetic_energy(m: float = 1., v: float = 0.) -> int:
    # Both : and -> are used to denote the type that arguments and returns are supposed to be, but no coercion
    # is done by this syntax. They are mere function annotations. Note that annotations always precede default
    # values for parameters. Note that if you replace m by m: 1., it will assume that the annotation type
    # is that of 1., ie. float, but it will not take 1. as the default value for parameter m.
    return round(1/2*m*v**2)

print(kinetic_energy.__annotations__['return'])
# Note: annotations are dictionaries; here we are searching for an entry in annotations with key 'return'.


# The fact that annotations are dictionaries allows us to annotate units in which the function works, in case
# some dimensional constants are introduced:
return_annotations = {"type": int, "units": 'Joule'}
def kinetic_energy_dim(m: {"type": float, "units": 'kilograms'} = 1., v: float = 0.) -> return_annotations:
    # You may input the dictionary straight in the annotation, without variable declaration, but as of
    # Python 3.7 PyCharm shows a warning (no exception is raised though)
    return round(1/2*m*v**2)

print(kinetic_energy_dim.__annotations__['return'])
print(kinetic_energy_dim.__annotations__['m']['units'])

