# Section 13 — Data Structures

A data structure is a way of arranging information so a program can use it. Different structures make different tasks easier. A row of numbered lockers is like an array, a stack of plates is like a stack, and a line of people waiting is like a queue.

## Common structures

An **array** stores items in numbered positions. It is quick to get an item when you know its index, but inserting something in the middle may mean moving later items.

A **linked list** stores items in nodes, with each node pointing to the next. It can be easy to insert or remove a node once you have reached the right place, but searching by position usually means following the links one by one.

A **stack** follows last in, first out (LIFO): the last item added is the first removed. Undo features and function calls are common examples.

A **queue** follows first in, first out (FIFO): the first item added is the first removed. Operating systems use queues for work waiting its turn.

A **tree** stores data in a hierarchy, like folders and subfolders. A **graph** contains nodes connected by edges, making it useful for maps, social networks, and product relationships.

A **hash table** stores key-value pairs and uses a hash of the key to find a value. It can make lookup very fast on average, but it does not automatically sort items. Courses classify hash tables in different ways, so follow the approach used in your class.

## Common operations

Programs insert items, delete them, visit every item (traversal), search, or sort. Traversal gets more work as the collection grows. A stack push or pop is usually quick. Searching an unsorted list may mean checking every item, while hash-table lookup is usually close to constant time on average.

Arrays are good for fast access by position. Linked lists can be easier to modify once you reach the right node, but are slower to search by position. No structure is best for every job; the best choice depends on how the program will use the data.

## Where the memory lives

C programs can use **static storage** for data whose size and lifetime are set in advance, or **dynamic allocation** when memory is requested while the program runs. `malloc()` requests dynamic memory, commonly from the heap, and `free()` releases it.

One detail: a fixed-size array is not always on the stack. Its location depends on how it is declared. Dynamically allocated memory commonly comes from the heap, while each thread has a stack for function calls and local execution state.

Use a stack when the newest item should be handled first, a queue when arrival order matters, a tree for a hierarchy, a graph for connections, and a hash table for fast lookup by key. A product recommendation feature, for example, can be modelled as a graph where products are nodes and links connect items people often buy together.
