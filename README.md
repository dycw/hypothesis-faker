# hypothesis-faker

[`faker`](https://github.com/joke2k/faker/) providers exported as
[`hypothesis`](https://github.com/HypothesisWorks/hypothesis) strategies.

## Introduction

`hypothesis` is great, but sometime you need domain-specific data outside of the
standard `hypothesis` extras. This is where `faker` shines -- many domains have
been carved out and explored. This package exports the `faker` providers as
`hypothesis` strategies.

This is done by building a simple cache of `faker` objects from which
`hypothesis` will sample from. The cache is initially seeded and periodically
expanded (to ensure new samples flow through), whilst kept under a limited size
(to avoid unbounded file sizes).

## Installation

```bash
pip install hypothesis-faker
```

## Available strategies

Please refer to the [package root](https://github.com/dycw/hypothesis-faker/blob/master/src/hypothesis_faker/__init__.py).
