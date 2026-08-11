# patchpilot-demo

A deliberately small storefront pricing module used to demonstrate
[PatchPilot](https://github.com/sualharun/PatchPilot), an autonomous engineering agent
that reads a GitHub issue, writes a fix, runs the test suite in a Docker sandbox, and
opens a pull request.

```bash
pip install -r requirements.txt
pytest -q
```

The `main` branch ships with one failing test. PatchPilot is expected to fix it without
breaking the three that pass.
