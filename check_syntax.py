#!/usr/bin/env python3
"""
Quick Rust Syntax Checker
Validates basic brace/bracket matching without compiling
"""

import sys
import os
from pathlib import Path

def check_file(filepath):
    """Check a single Rust file for brace matching"""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Track braces
    braces = []
    brackets = []
    parens = []
    
    # Simple check (not perfect, ignores strings/comments but good enough)
    for i, char in enumerate(content):
        if char == '{':
            braces.append(i)
        elif char == '}':
            if not braces:
                return False, f"Unexpected }} at position {i}"
            braces.pop()
        elif char == '[':
            brackets.append(i)
        elif char == ']':
            if not brackets:
                return False, f"Unexpected ] at position {i}"
            brackets.pop()
        elif char == '(':
            parens.append(i)
        elif char == ')':
            if not parens:
                return False, f"Unexpected ) at position {i}"
            parens.pop()
    
    if braces:
        return False, f"Unclosed {{ at position {braces[0]}"
    if brackets:
        return False, f"Unclosed [ at position {brackets[0]}"
    if parens:
        return False, f"Unclosed ( at position {parens[0]}"
    
    return True, "OK"

def main():
    src_dir = Path("src")
    errors = []
    
    for rs_file in src_dir.rglob("*.rs"):
        ok, msg = check_file(rs_file)
        if ok:
            print(f"✅ {rs_file}: {msg}")
        else:
            print(f"❌ {rs_file}: {msg}")
            errors.append((rs_file, msg))
    
    if errors:
        print(f"\n❌ Found {len(errors)} files with errors")
        sys.exit(1)
    else:
        print(f"\n✅ All files passed basic syntax check")
        sys.exit(0)

if __name__ == "__main__":
    main()
