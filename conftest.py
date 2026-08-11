# Makes the project root importable so bare `pytest` finds `pricing`.
# Without this, pytest puts only tests/ on sys.path and the import fails.
