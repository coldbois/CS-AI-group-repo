# Section 11 — Computer Programming

Programming means working out a solution and writing instructions a computer can follow. It includes planning, writing code, testing it, and fixing mistakes. Computers follow their instructions, so those instructions need to be clear.

## Programming languages

A programming language lets people express instructions without writing every machine instruction as 0s and 1s.

A **compiled** program is translated ahead of time into another form, often machine code, before it runs. C and C++ are common examples. An **interpreted** program is executed through an interpreter at runtime; Python and JavaScript are often taught this way. Modern runtimes can mix techniques, so this is a helpful starting distinction rather than a strict rule.

Assembly language is closer to the CPU. It uses short instruction names such as `MOV`, `ADD`, and `SUB`. Registers are small, fast storage locations inside the processor; operands are the values an instruction uses; labels name places in the code. High-level languages hide many hardware details. C is relatively close to the hardware while still providing features such as functions and loops, which helps make it useful for system software.

## Different ways to organize programs

- **Procedural programming** arranges instructions into steps and functions. C is a common example and works well for tasks with a clear order.
- **Object-oriented programming (OOP)** groups data and related behaviour into objects. A class is a blueprint; an object is an actual instance of that class. Java, C++, and Python support OOP.
- **Functional programming** emphasises functions and tries to avoid changing existing data. A pure function returns the same result for the same inputs and has no side effects. Lisp and Haskell are associated with this style.
- **Logic programming** describes facts and rules, then asks the system to find answers. Prolog is a well-known example.

Pure functions are usually easier to test because their results do not depend on hidden changes elsewhere in the program.

## Web languages and debugging

HTML describes a page's structure, such as headings, paragraphs, images, and links. It is a markup language, not a general-purpose programming language. JavaScript adds interactivity and can also run on servers. SQL is used to query and change database information. Python is a general-purpose language used for web development, data analysis, AI, and automation.

**Debugging** means finding and fixing the cause of a problem. Start by reproducing the problem, then narrow down where it begins. A debugger can pause a program and let you inspect variables; a breakpoint is a place where it pauses. Static analysers can flag likely problems without running the code. GDB is one debugger used with C.

A famous 1947 story involved a moth found in a computer and recorded as a “bug,” though people already used the word for faults. The broader lesson is that programming involves more than writing code: testing and fixing it are part of the work.
