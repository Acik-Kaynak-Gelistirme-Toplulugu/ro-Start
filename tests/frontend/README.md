# Frontend Tests

This directory contains tests for the React frontend components.

## Running Tests

```bash
cd frontend
npm test
```

## Test Structure

- Component tests using Vitest/Jest
- Integration tests for user flows
- Snapshot tests for UI consistency

## Writing Tests

Example test file:

```typescript
import { describe, it, expect } from "vitest";
import { render, screen } from "@testing-library/react";
import { WelcomeScreen } from "../components/WelcomeScreen";

describe("WelcomeScreen", () => {
  it("renders welcome message", () => {
    render(<WelcomeScreen />);
    expect(screen.getByText(/welcome/i)).toBeInTheDocument();
  });
});
```
