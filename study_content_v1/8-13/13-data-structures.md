# Section 13: Data Structures

## 1. What is a data structure?

A **data structure** is a way to store and organize information in a program so it can be found, added, removed, or changed efficiently. Data structures are used in everything from calculators and contact lists to operating systems, search engines, and AI applications.

Imagine organizing items at home:

- A row of numbered lockers resembles an **array**.
- A stack of plates resembles a **stack**, because the most recently placed plate is the first one removed.
- A canteen line resembles a **queue**, because people are served in the order they arrive.
- A family tree resembles a **tree** because it represents a hierarchy of relationships.

## 2. Common data structures

| Broad type | Structure | How it organizes data | Typical uses |
|---|---|---|---|
| Linear | **Array** | Stores elements in indexed positions in a sequence. | Lists of scores, image pixels, and other collections where positions are useful. |
| Linear | **Linked list** | Stores elements in separate nodes, with each node linking to the next node (and, in some versions, the previous node too). | Collections that change size or need frequent insertions and deletions. |
| Linear | **Stack** | Follows **last in, first out (LIFO)**: the newest item is removed first. | Undo operations and function-call tracking. |
| Linear | **Queue** | Follows **first in, first out (FIFO)**: the oldest waiting item is handled first. | OS task queues, waiting lines, and transaction processing. |
| Non-linear | **Tree** | Organizes nodes in a hierarchy beginning at a root node. | Folder structures, domain names and subdomains, and other hierarchies. |
| Non-linear | **Graph** | Represents nodes (also called vertices) connected by edges. Edges can represent different kinds of relationships. | Social networks, maps, pathfinding, and product recommendations. |
| Often grouped separately or as non-linear | **Hash table** | Stores key-value pairs and uses a hash of a key to locate its entry. | Dictionaries, databases, and fast lookups by key. |

A **node** is an individual element in a linked structure. In a graph, an **edge** represents a connection between two nodes. A tree is a particular kind of graph with a hierarchical structure.

Hash tables are often grouped with non-linear data structures because an item is located by its key rather than by its position in a sequence. Some courses discuss hash tables as a separate category, so the exact classification can depend on the course.

Examples of matching a structure to a task:

- A folder hierarchy is naturally represented by a tree.
- Undoing the most recent action fits a stack.
- An OS queue can keep tasks waiting in arrival order.
- A graph can represent roads connecting locations or products frequently bought together.

## 3. Arrays and linked lists compared

Arrays and linked lists can both store sequences, but they behave differently when a program accesses or changes items.

| Operation | Array | Linked list |
|---|---|---|
| Access an item at a known position | Fast: `O(1)` for index-based access. | Usually slower: `O(n)` in the general case because the program must follow links from the beginning (or another known node). |
| Add or remove at the end | Often `O(1)` for a suitable array implementation when capacity is available; resizing may occasionally cost more. | Fast if the list maintains a tail pointer; otherwise reaching the end can take `O(n)`. |
| Insert or delete in the middle | Often `O(n)` because later elements may need to shift. | Can be `O(1)` once the relevant node or position is already known, because links can be changed. Finding that position may still take `O(n)`. |
| Find the last item | Fast for an array with known length. | Usually requires following the links to the end unless the list maintains a tail pointer. |

An array is like a row of numbered lockers: you can go directly to locker number `4`. A linked list is like a treasure hunt: each clue tells you where to find the next clue. This is why linked lists can be convenient for changing connections between nodes, while arrays make indexed access straightforward.

The operation's assumptions matter. For example, inserting a node into a linked list can be constant-time **after** the insertion point is known, but searching for that point may take linear time.

## 4. Common operations on data structures

| Operation | Meaning | Example |
|---|---|---|
| **Insertion** | Add a new element. | Add a name to a contact list. |
| **Deletion** | Remove an element. | Remove a message from an inbox. |
| **Traversal** | Visit each element, often to process or inspect it. | Add together the prices of every item in a shopping cart. |
| **Searching** | Look for a particular element and stop when it is found (or when no match remains possible). | Look up a phone number. |
| **Sorting** | Rearrange elements into a defined order. | Order students by grade. |

Traversal visits all elements, so it generally takes time proportional to the number of elements, `O(n)`. Adding an item to a stack is usually `O(1)`, provided the underlying storage operation is available in constant time.

Searching an unsorted list may require checking every element. A hash table can find an item by key in about `O(1)` average time under typical assumptions, though performance can degrade in unfavorable cases. A hash table also does not inherently keep items in sorted order.

## 5. How data is placed in memory

Programs need memory for the values and structures they use. In C, some storage is set up with a size known in advance, while dynamic allocation lets a program request memory as it runs.

| Allocation style | When size or storage is determined | Typical memory area or C feature |
|---|---|---|
| **Fixed-size local storage** | The size is specified in the code, such as a local array with a fixed length. | A local automatic variable or array commonly uses the **stack**, depending on the implementation and context. |
| **Static storage duration** | Storage exists for the lifetime of the program. Its size is generally determined by the program's declarations. | Global variables and variables declared `static` use static storage; this is not the same thing as stack allocation. |
| **Dynamic allocation** | Memory is requested while the program is running, allowing the amount of allocated space to respond to the program's needs. | `malloc()` requests memory from the **heap** in C; `free()` releases it when it is no longer needed. |

**Accuracy clarification:** The original table labels static allocation as being in the stack. That is not generally correct in C. Fixed-size local automatic variables commonly reside on the stack, while objects with static storage duration are stored separately from ordinary stack allocations. Exact physical placement can depend on the implementation and optimization.

Dynamic allocation is helpful when the amount of data is not known in advance or can change during execution. For example, a program processing a changing number of records may need to request memory as records are added. `malloc()` reserves memory from the heap; it does not allocate memory from the stack. In C, the programmer must also manage the lifetime of dynamically allocated memory and release it when appropriate.

This connects data structures to the operating-system topics of processes, memory, and scheduling. For example, queues can hold jobs waiting for CPU time, while dynamic data structures may require additional heap memory as the amount of work grows.

## 6. Choosing a data structure

| If your main requirement is... | A reasonable starting choice is... |
|---|---|
| Keeping items in sequence | An array or linked list. |
| Representing hierarchical relationships | A tree. |
| Representing general connections between things | A graph. |
| Finding a value quickly by key | A hash table. |
| Undoing the most recent action first | A stack. |
| Processing items in arrival order | A queue. |
| Handling an amount of data that changes at runtime | A structure that can grow dynamically, using suitable memory allocation. |

No single data structure is best for every operation. The right choice depends on how the program will access the data, how often the data changes, and how much time and memory are available.

## 7. Real-world example: product recommendations

A product recommendation feature, such as “customers who bought this also bought,” can be modeled as a graph:

- Each product is represented by a node.
- An edge connects two products that are often purchased together.
- A recommendation system can explore these connections to identify products related to the item a customer is viewing.

The example illustrates why graphs are useful when the relationships between items matter as much as the items themselves.

## Key takeaways

- Data structures organize information so programs can work with it efficiently.
- Arrays and linked lists both store sequences, but differ in access and insertion costs.
- Stacks use LIFO order; queues use FIFO order.
- Trees represent hierarchies, graphs represent general relationships, and hash tables support lookup by key.
- Big-O costs depend on the exact operation and its assumptions, not only on the name of the data structure.
- In C, `malloc()` allocates heap memory, while stack allocation and static storage duration are distinct concepts.
