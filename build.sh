#!/bin/bash

# Description: Build script for the assignments project.

echo "Building project"

# Check for verbose flag
VERBOSE=0
if [ "$1" == "-v" ] || [ "$1" == "--verbose" ]; then
    VERBOSE=1
fi

# Run the tests
if [ $VERBOSE -eq 0 ]; then
    TEST_OUTPUT=$(python -m unittest discover tests 2>&1)
else
    echo "├── Running tests..."
    python -m unittest discover tests
fi

# Check the exit status of the last command (i.e., the tests)
if [ $? -eq 0 ]; then
    if [ $VERBOSE -eq 0 ]; then
        echo "├── Running tests... ✓"
    else
        echo "├── Tests passed."
    fi

    # Build the documentation
    if [ $VERBOSE -eq 0 ]; then
        DOC_OUTPUT=$(pdoc --html --force --output-dir ./docs ./src 2>&1)
        echo "└── Building docs... ✓"
    else
        echo "├── Building documentation..."
        pdoc --html --force --output-dir ./docs ./src
        echo "└── Documentation built."
    fi
else
    if [ $VERBOSE -eq 0 ]; then
        echo "└── Running tests... ✘"
    elif [ $VERBOSE -eq 1 ]; then
        echo "└── Tests failed."
    fi
    exit 1
fi
