# Problem 1

Heaps can be used as priority queues because they allow efficient access to the highest (or lowest) priority element.
The root of the heap always contains the maximum (or minimum) element, which allows for efficient retrieval.

Max Heap Example:
          50
       /     \
     30       20
    /  \     /  \
  10   15   5    10

After inserting 60:
          60
       /     \
     50       20
    /  \     /  \
  10   30   5    10
 / 
15  

After extracting max (60):
          50
       /     \
     30       20
    /  \     /  \
  10   15   5    10