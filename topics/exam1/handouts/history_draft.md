```mermaid
flowchart TB
  R[Registers<br/>(fastest, smallest)]
  C[Cache<br/>(very fast, small)]
  M[Main Memory (RAM)<br/>(fast, larger)]
  S[Solid-State Drive (SSD)<br/>(slower, persistent)]
  H[Mechanical Hard Drive<br/>(slowest, persistent, largest)]

  R --> C --> M --> S --> H
```

