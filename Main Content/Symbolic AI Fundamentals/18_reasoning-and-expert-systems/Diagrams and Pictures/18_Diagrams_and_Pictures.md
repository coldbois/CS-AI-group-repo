# Topic 18 — Diagrams and Pictures

## Figure 1. Basic expert-system architecture

```mermaid
flowchart TD
    U[User] <--> UI[User interface]
    UI <--> WM[Working memory]
    WM <--> IE[Inference engine]
    KB[Knowledge base: facts and rules] <--> IE
    IE --> EX[Explanation facility]
    EX --> UI
```

**Caption:** The interface collects case information. The inference engine uses the knowledge base and current working memory to derive a result. An explanation facility can show which rules were used.

## Figure 2. Forward and backward chaining

```mermaid
flowchart TD
    subgraph F[Forward chaining]
      F1[Known facts] --> F2[Match rule conditions]
      F2 --> F3[Add new facts]
      F3 --> F4[More rules or conclusion]
    end
    subgraph B[Backward chaining]
      B1[Start with a goal] --> B2[Find a rule that concludes it]
      B2 --> B3[Check the rule conditions]
      B3 --> B4[Check facts or sub-goals]
    end
```

**Caption:** Forward chaining moves from available facts towards conclusions. Backward chaining starts from a question and checks what would support it.

## Figure 3. Example rule trace

```mermaid
flowchart TD
    A[prerequisite_passed] --> C[prerequisite_ok]
    B[fees_paid] --> D[finance_ok]
    C --> E{Both conditions true?}
    D --> E
    E -->|Yes| F[may_register]
```

**Caption:** The conclusion is reached only after both conditions needed by the final rule have been established.

## Optional images to add

- A simplified historical MYCIN overview with a clear “historical example” caption.
- A small decision tree for technical troubleshooting.
- A table comparing deduction, induction and abduction.

Use team-made diagrams where possible. For external images, check the individual licence and attribution requirements before including them.
