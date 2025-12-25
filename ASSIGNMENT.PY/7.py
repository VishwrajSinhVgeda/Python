# 7 . How memory is managed in Python? 
# Answer :
# Memory management in Python involves a private heap containing all Python objects and data structures.
# The management of this private heap is ensured internally by the Python memory manager.
# Python also has an inbuilt garbage collector, which recycles all the unused memory to make it available for heap space.
# Explanation :
# 1. Private Heap: All Python objects and data structures are stored in a private heap.
# 2. Memory Manager: The Python memory manager manages the allocation of heap space for Python
#    objects.
# 3. Garbage Collection: Python has an inbuilt garbage collector that recycles unused memory
#    to make it available for heap space.
#    It uses reference counting and cyclic garbage collector to manage memory.
