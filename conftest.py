"""Makes the project root importable so `pytest` finds `pricing`.

Without this, bare `pytest` puts only `tests/` on sys.path and
`from pricing import ...` fails. `python -m pytest` happens to work either
way, which makes the difference easy to miss.
"""
