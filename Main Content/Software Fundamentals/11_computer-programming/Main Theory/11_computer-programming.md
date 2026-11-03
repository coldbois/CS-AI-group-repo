# 11. Computer Programming

## Topic overview

Computer programming is the process of writing instructions that a computer can execute. This chapter introduces source code, programming languages, variables, control flow, functions, debugging and basic development practices.

### Learning outcomes

1. Explain the basic program development cycle.
2. Identify variables, expressions, decisions, loops and functions.
3. Distinguish compilation from interpretation at a basic level.

### Key terms

| Term | Meaning |
|---|---|
| **Source code** | Human-readable instructions written in a programming language. |
| **Syntax** | The rules for how a language’s statements must be written. |
| **Compiler** | Translates source code before or during execution into another form. |
| **Interpreter** | Executes program instructions through an interpreting runtime. |
| **Debugging** | Finding, understanding and correcting defects. |
| **Test case** | An input and expected result used to check behaviour. |

## Main concepts

### 11.1 From problem to program

A programmer first understands the problem, identifies inputs and outputs, plans an algorithm, writes code, tests it and improves it. Breaking a task into smaller functions makes programs easier to understand and maintain.

### 11.2 Core building blocks

Variables store values. Types describe what kind of values are allowed. Expressions calculate results. Conditional statements choose a path; loops repeat work; functions group reusable behaviour. Arrays and other data structures organise collections of information.

### 11.3 Languages and execution

C is commonly compiled to machine code. Python is commonly run through an interpreter or virtual machine. Modern language implementations may combine compilation and interpretation, so the distinction is a simplified introduction rather than a strict rule for every implementation.

### 11.4 Debugging and testing

A syntax error breaks language rules. A runtime error occurs while the program executes. A logic error produces the wrong result despite running. Testing should include ordinary inputs, edge cases and invalid inputs. Debuggers and compiler warnings help locate issues.

### 11.5 Good habits

Use meaningful names, consistent formatting, comments for non-obvious decisions, version control and small, frequent tests. Avoid copying code without understanding it.

![Figure 1: An example of poorly formatted C code](https://i.imgur.com/egoYpeg.png)

*Figure 1. An example of poorly formatted C code, which you should try to avoid. Source: Self-made, image hosted on [Imgur](https://imgur.com/gallery/figure-3-aTlLIcr)*

![Figure 2: An example of properly formatted C code](https://i.imgur.com/Ea4kgev.png)

*Figure 2. An example of properly formatted C code, which you should learn from. Source: Self-made, image hosted on [Imgur](https://imgur.com/gallery/good-example-2V4PY75)*

## Worked example

For a program that checks leap years, translate the calendar rule into decisions: a year is a leap year when it is divisible by 400, or divisible by 4 but not by 100. Test 2000 (yes), 1900 (no), 2024 (yes) and 2023 (no). These tests cover ordinary and century edge cases.

## Visual references

![Figure 3: Flowchart alongside a simple C program example](https://i.sstatic.net/KhpYO.png)

*Figure 3. Flowchart alongside a simple C program example. Source: [Stack Overflow](https://i.sstatic.net/KhpYO.png).*

![Figure 4: CPU fetch–execute cycle](https://upload.wikimedia.org/wikipedia/commons/f/f0/CPU_fetch-execute_cycle.svg)

*Figure 4. CPU fetch–execute cycle. Source: [Wikimedia Commons](https://upload.wikimedia.org/wikipedia/commons/f/f0/CPU_fetch-execute_cycle.svg).*

## Applications and limitations

These concepts appear in real software systems, but the simplified examples in this chapter leave out some implementation details. Practical systems must also consider performance, errors, security and changing requirements. Always check that the model matches the problem before relying on its output.

## Connection to the next topic

Topic 12 focuses on the algorithms that programs implement.

## Key takeaways

- Explain the basic program development cycle.
- Identify variables, expressions, decisions, loops and functions.
- Distinguish compilation from interpretation at a basic level.
- Use the worked example to connect the terminology to a concrete situation.
- The diagrams are externally sourced images; check the source page and licence before public redistribution.
