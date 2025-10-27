1. Easiest vs. Hardest Issues to Fix

Easiest: Formatting and naming issues were the simplest to fix. Problems such as missing blank lines (Flake8 E302), unused imports, and non-snake_case function names required only minor edits that didn’t affect logic.

Hardest: The harder issues were the ones flagged by Bandit—specifically the use of eval() and bare except blocks. These required rethinking the code logic for safe exception handling and replacing eval() with a secure alternative (ast.literal_eval), rather than just syntactic changes.

2. False Positives

Most warnings were valid. However, one potential false positive was the “missing docstring” messages in pylint_report.txt during the early development phase. Since the script was small and self-explanatory, these were stylistic rather than functional issues, though adding docstrings still improved readability.

3. Integrating Static Analysis in Development Workflow

Local checks: Run Flake8, Pylint, and Bandit before each commit using pre-commit hooks.

CI integration: Configure GitHub Actions (or any CI system) to automatically run these tools on every pull request. This prevents unsafe or non-compliant code from being merged.

IDE support: Enable on-save linting in VS Code to catch issues immediately while coding.

4. Tangible Improvements

Readability: Consistent naming, proper spacing, and detailed docstrings made the code easier to read and maintain.

Robustness: Safer exception handling and removal of eval() reduced the risk of runtime errors and security vulnerabilities.

Maintainability: Using with open() and clear logging/error messages improved clarity and made debugging simpler.

Overall: The final code now adheres to PEP 8 standards, is secure, and ready for integration into larger systems.
