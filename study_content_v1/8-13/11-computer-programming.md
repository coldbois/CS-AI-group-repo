# Section 11: Computer Programming

## 1. What is computer programming?

**Computer programming** is the process of designing instructions for a computer, writing those instructions in a programming language, and testing and fixing the resulting program. The goal is to solve a problem or make the computer perform a task.

Think of programming as writing a highly precise to-do list for a robot. The robot follows the instructions literally; it cannot reliably guess what you meant when a step is vague or missing.

## 2. Programming languages

A **programming language** gives people a structured way to express instructions that can ultimately be carried out by a computer. Without such languages, programmers would have to work much more directly with machine code, which is difficult for people to read and write.

Two common ways to run programs are compilation and interpretation.

| Method | How it works | Common examples in introductory explanations | General trade-off |
|---|---|---|---|
| **Compilation** | A compiler translates source code into a lower-level form, often machine code, before the resulting program is run. | C and C++ | The resulting program can run efficiently, although compilation takes time and may require a separate build step. |
| **Interpretation** | An interpreter or runtime executes the program based on its source or an intermediate form as the program runs. | Python and JavaScript are often introduced this way. | Interactive testing and debugging can be convenient. Execution speed depends on the implementation and workload. |

Compilation and interpretation are useful beginner-level categories, but real language implementations can combine techniques. For example, modern Python and JavaScript runtimes may compile code into intermediate forms or machine code internally. Therefore, the table describes common usage rather than a strict rule for every implementation.

## 3. Assembly language and high-level languages

**Assembly language** is a low-level language closely tied to a processor's instruction set. It uses short names called **mnemonics**—such as `MOV`, `ADD`, and `SUB`—to represent machine instructions.

Common assembly terms include:

- **Register:** a very small, fast storage location inside the CPU, such as an x86 register named `EAX`.
- **Instruction or command:** an operation for the processor to carry out, such as adding two values.
- **Label:** a name for a location in code that another instruction can refer to.
- **Operand:** a value or location an instruction uses.

Example in x86-style assembly:

```asm
section .text
global _start
_start:
    mov eax, 5      ; put 5 in register eax
    add eax, 3      ; add 3, so eax becomes 8
```

Here, `mov` puts the value `5` into the register `eax`; `add` then adds `3` to that register's value. Assembly syntax differs between processor families and assemblers, so this example is not universal assembly code.

A **high-level language**, such as Python, C++, or JavaScript, hides many hardware details so programmers can focus on the program's logic rather than individual processor instructions. C has high-level features, such as functions and structured control flow, while also allowing relatively direct control over memory. For that reason, many textbooks describe C as a **middle-level language**. This is an informal description, not an official category shared by every programming-language classification.

## 4. Programming paradigms

A **programming paradigm** is a general style or way of organizing a program.

| Paradigm | Main idea | Examples |
|---|---|---|
| **Procedural** | Organizes a program as a sequence of steps, usually grouped into functions. Data and the functions that operate on it can be kept separate. | C, Fortran, Pascal, BASIC. |
| **Object-oriented programming (OOP)** | Organizes code around classes and objects. A class describes a kind of object; an object is a particular instance created from that class. | Java, C++, Python. |
| **Functional** | Builds programs using functions. Pure functional code emphasizes functions that produce results without changing external state. | Lisp, Haskell. |
| **Logic-based** | Expresses facts and rules, then asks the system to find answers that satisfy them. | Prolog. |

In object-oriented programming, a **class is the blueprint**, not the real entity; an **object is an instance** of the class. For example, a `Car` class might define properties and behaviors, while one particular red car in a program is an object created from that class.

A **pure function** has three useful properties:

1. Given the same inputs, it returns the same output.
2. It does not cause side effects, such as changing a global variable or writing to a file.
3. Its result depends only on its inputs, not on hidden external state.

These properties support **referential transparency**: a call to the function can be replaced with its result without changing the program's behavior. That makes pure functions easier to test and reason about. A procedural approach is often a natural fit when a task is best described as an ordered recipe of steps.

## 5. Not every web language is a programming language

| Language or technology | Role |
|---|---|
| **HTML** | A markup language that structures web content, such as headings, paragraphs, images, and links. HTML is not itself a programming language. |
| **JavaScript** | A general-purpose programming language often used to make web pages interactive. With environments such as Node.js, it can also run on servers. |
| **SQL** | A language used to define, retrieve, and change data in relational databases. It is often described as a domain-specific language because it focuses on database work. |
| **Python** | A general-purpose programming language used in web development, data science, AI, automation, and many other fields. |

HTML describes the structure of content; JavaScript can describe behavior. SQL expresses database operations, while Python can be used for a broader variety of tasks.

## 6. Debugging

**Debugging** means finding the cause of a program's incorrect behavior and fixing it. A practical process is:

1. Reproduce the problem so you can observe it reliably.
2. Narrow down where it occurs.
3. Use tools to inspect the program's state and test a fix.
4. Run the program again to check that the fix works and has not introduced another problem.

Useful tools include:

- **Breakpoints:** instructions to a debugger to pause execution at a chosen line so you can inspect variables and program state.
- **Debuggers:** tools such as GDB that let you step through a program and investigate its behavior.
- **Static analyzers:** tools that examine code without running it and flag potential errors or risky patterns.

A famous computing anecdote concerns a moth found in a Harvard computer and logged on 9 September 1947. The incident helped popularize the physical “bug” story, but the word *bug* was already used for technical faults before then; it was not newly invented by that incident.

## Key takeaways

- Programming turns a solution into precise instructions a computer can execute.
- Compilers and interpreters are two ways of translating or executing code, and modern runtimes can combine techniques.
- Assembly is closely tied to processor instructions; high-level languages hide many hardware details.
- Procedural, object-oriented, functional, and logic-based programming organize problem-solving in different ways.
- Debugging combines reproducing a problem, inspecting program behavior, and testing a correction.
