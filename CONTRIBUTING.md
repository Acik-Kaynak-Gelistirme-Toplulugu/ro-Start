# Contributing to Ro-Start

First off, thanks for taking the time to contribute! ❤️

All types of contributions are encouraged and valued. See the [Table of Contents](#table-of-contents) for different ways to help and details about how this project handles them. Please make sure to read the relevant section before making your contribution. It will make it a lot easier for us maintainers and smooth out the experience for all involved. The community looks forward to your contributions.

## Table of Contents

- [Code of Conduct](#code-of-conduct)
- [I Have a Question](#i-have-a-question)
- [I Want To Contribute](#i-want-to-contribute)
- [Styleguides](#styleguides)

## Code of Conduct

This project and everyone participating in it is governed by the [Code of Conduct](CODE_OF_CONDUCT.md). By participating, you are expected to uphold this code. Please report unacceptable behavior to the maintainers.

## I Have a Question

> If you want to ask a question, we assume that you have read the available [Documentation](README.md).

Before you ask a question, it is best to search for existing [Issues](https://github.com/ro-start/ro-start/issues) that might help you. In case you've found a suitable issue and still need clarification, you can write your question in this issue. It is also advisable to search the internet for answers first.

## I Want To Contribute

### Legal Notice

When contributing to this project, you must agree that you have authored 100% of the content, that you have the necessary rights to the content and that the content you contribute may be provided under the project license.

### Development Setup

1.  **Fork and Clone:**

    ```bash
    git clone https://github.com/your-username/ro-start.git
    cd ro-start
    ```

2.  **Environment Setup:**

    - Python 3.10+
    - Node.js 18+

3.  **Install Dependencies:**

    ```bash
    # Backend
    python3 -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt

    # Frontend
    cd tema
    npm install
    ```

4.  **Run Development Mode:**
    - To run the full app: `python3 src/main.py`
    - To edit UI live: `cd tema && npm run dev`

### Project Structure

- `src/`: Python backend logic (system info, driver management).
- `tema/`: React frontend (UI components, styles).

## Styleguides

### Commit Messages

- Use the present tense ("Add feature" not "Added feature")
- Use the imperative mood ("Move cursor to..." not "Moves cursor to...")
- Limit the first line to 72 characters or less
- Reference issues and pull requests liberally after the first line

### Coding Style

- **Python:** Follow PEP 8.
- **TypeScript/React:** Follow standard React best practices (Functional Components, Hooks). Use Prettier for formatting.

---

Happy Coding! 🚀
