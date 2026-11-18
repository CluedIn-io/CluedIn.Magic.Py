# Integration tests

The tests in this folder exercise the `%cluedin` magic against a **real,
running CluedIn instance** over the network. They are not run as part of a
normal unit test pass and require setup before they will work.

## Prerequisites

- A reachable CluedIn instance.
- A valid JWT access token for that instance, with permission to run the
  `get-context` and `search` queries used by these tests.
- The target instance must contain the dataset these tests assert against
  (e.g. the `/IMDb/Name` and `/Infrastructure/User` entities referenced in
  `test_search.py`, with the specific counts the tests expect). Point these
  tests at an environment seeded with that data, or update the expected
  counts to match your own dataset.

## Setup

1. Create a `.env` file in the repository root (it's already git-ignored,
   so it will never be committed):

   ```env
   ACCESS_TOKEN=<a valid JWT access token for your CluedIn instance>
   ```

2. Install dependencies, including the `dev` group, with Poetry:

   ```sh
   poetry install
   ```

## Running

Run only the integration tests:

```sh
poetry run pytest tests/integration
```

Run everything except the integration tests (unit tests, no network or
`.env` required):

```sh
poetry run pytest tests/unit
```
