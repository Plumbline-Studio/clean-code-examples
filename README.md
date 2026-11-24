# Clean code examples

Small examples you can run, one for each article on
[plumblinestudio.dev/resources](https://plumblinestudio.dev/resources/).

Each folder is one idea about building software you can trust. Each one is small, needs only
Python 3 (nothing to install), and has its own README that says what it shows and how to run it.

| Folder | The idea |
|---|---|
| [`01-every-fix-becomes-a-check`](01-every-fix-becomes-a-check/) | When a mistake is fixed once, a small test makes sure it never comes back. |

More are coming: "Green means green" (one command says ready or not ready, the same on every
machine) and "Approve from pictures, not code."

## Run them all

```
python3 -m unittest discover -s 01-every-fix-becomes-a-check -t 01-every-fix-becomes-a-check
```

Every folder is also checked on every change by [`.github/workflows/check.yml`](.github/workflows/check.yml).

## What is here, and what is not

Everything here was written for teaching. There is no client code, no client data and nothing
copied from a private project. The examples are made up, but the habits are the ones we use.

---

Plumbline Studio · Roanoke, Virginia · *Build it true.*
