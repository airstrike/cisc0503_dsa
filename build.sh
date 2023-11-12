#!/bin/bash

# Description: Build script for the assignments project.

echo "Building project"

# Check for verbose flag
VERBOSE=0
if [ "$1" == "-v" ] || [ "$1" == "--verbose" ]; then
    VERBOSE=1
fi

# Define arrays for task names and their corresponding commands
task_names=("Unit tests" "Coverage report" "Documentation")
commands=(
    "coverage run -m unittest discover tests"
    "coverage html --directory ./html/coverage"
    "pdoc3 --html --force --output-dir ./html/docs ./src/cisc0503_dsa"
)

# Function to run a command and check its status
run_task() {
    local task_name=$1
    local command=$2
    local last_task=$3

    if [ $VERBOSE -eq 0 ]; then
        OUTPUT=$($command 2>&1)
    else
        echo "├── Running $task_name..."
        $command
    fi

    if [ $? -eq 0 ]; then
        if [ $VERBOSE -eq 0 ]; then
            if [ "$last_task" == "yes" ]; then
                echo "└── $task_name... ✓"
            else
                echo "├── $task_name... ✓"
            fi
        else
            echo "├── $task_name passed."
        fi
    else
        if [ $VERBOSE -eq 0 ]; then
            echo "└── $task_name... ✘"
        else
            echo "└── $task_name failed."
        fi
        exit 1
    fi
}

# Iterate over the tasks and execute them
task_count=${#task_names[@]}
for (( i=0; i<${task_count}; i++ )); do
    last_task="no"
    if [ $((i + 1)) -eq $task_count ]; then
        last_task="yes"
    fi
    run_task "${task_names[i]}" "${commands[i]}" "$last_task"
done
