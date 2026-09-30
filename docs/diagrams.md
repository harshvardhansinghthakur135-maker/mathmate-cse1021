# Diagrams (Mermaid source)

GitHub renders these blocks automatically. PNG versions (Graphviz) are in `docs/diagrams/`.
Note: the Mermaid blocks below were written by hand and were not render-tested in the build environment;
the PNG files are the tested versions.

## System Architecture
```mermaid
flowchart TB
  U([User]) --> M[main.py] --> MENU[menu.py]
  MENU --> V[validation.py]
  MENU --> L[logger.py] --> LF[(logs/mathmate.log)]
  MENU --> B[basic_algorithms.py\nUnit 3]
  MENU --> F[factoring.py\nUnit 4]
  MENU --> A[array_tools.py\nUnit 5]
  MENU --> E[efficiency.py\nUnit 1 / trade-off]
  T[tests/] -.-> B & F & A & E & V
```

## Workflow
```mermaid
flowchart TB
  S([Start]) --> MM[Show main menu] --> X{Choice 0?}
  X -- Yes --> E([Stop])
  X -- No --> C1{Valid?}
  C1 -- No --> MM
  C1 -- Yes --> SM[Show submenu] --> B{Choice 0?}
  B -- Yes --> MM
  B -- No --> C2{Valid?}
  C2 -- No --> SM
  C2 -- Yes --> IN[/Read and validate input/] --> P[Run algorithm] --> ER{ValueError?}
  ER -- Yes --> EM[/Print error, log WARNING/] --> SM
  ER -- No --> OUT[/Print result, log INFO/] --> SM
```

## Use Case
```mermaid
flowchart LR
  User((Student)) --> U1[Number basics]
  User --> U2[Factor and analyse numbers]
  User --> U3[Analyse a list]
  User --> U4[Compare efficiency]
  U1 & U2 & U3 & U4 -.include.-> V[Validate input]
  U1 & U2 & U3 & U4 -.extend.-> ER[Show error message]
  U1 & U2 & U3 & U4 -.-> LG[Write log entry]
```

## Component Diagram
```mermaid
flowchart LR
  main.py --> menu.py
  menu.py --> validation.py
  menu.py --> logger.py
  menu.py --> basic_algorithms.py
  menu.py --> factoring.py
  menu.py --> array_tools.py
  menu.py --> efficiency.py
  tests --> basic_algorithms.py & factoring.py & array_tools.py & efficiency.py & validation.py
```

## Sequence Diagram
```mermaid
sequenceDiagram
  actor User
  participant Menu as menu.py
  participant Val as validation.py
  participant Alg as Algorithm module
  participant Log as logger.py
  User->>Menu: choose module and option
  Menu->>Val: read_int(prompt, min, max)
  loop until valid
    Val-->>User: error message, ask again
    User->>Val: enter value
  end
  Val-->>Menu: validated value
  Menu->>Alg: function(value)
  alt valid
    Alg-->>Menu: result
    Menu-->>User: print result
    Menu->>Log: INFO
  else ValueError
    Alg-->>Menu: raise ValueError
    Menu-->>User: print "Error: ..."
    Menu->>Log: WARNING
  end
```

## ER Diagram / Database Schema
Not applicable: MathMate has no database. The only storage is the plain-text log file
`logs/mathmate.log`, one line per event: `timestamp | LEVEL | message`.
