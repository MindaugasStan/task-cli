# task-cli

https://github.com/MindaugasStan/task-cli/

A simple command-line task manager that lets you add, update, delete, and track the status of your tasks. Tasks are stored locally in a `tasks.json` file.

## Requirements

- Python 3.10 or higher

## Installation

Clone the repository and install it:

```bash
git clone
cd task-cli
pip install -e .
```

After installation, the `task-cli` command will be available in your terminal.

## Usage

### Add a task

```bash
task-cli add "Buy milk"
# Task added successfully (ID: 1)
```

### Update a task

```bash
task-cli update 1 "Buy oat milk"
```

### Delete a task

```bash
task-cli delete 1
```

### Mark a task as in progress

```bash
task-cli mark-in-progress 1
```

### Mark a task as done

```bash
task-cli mark-done 1
```

### List tasks

```bash
# List all tasks
task-cli list

# List tasks by status
task-cli list todo
task-cli list in_progress
task-cli list done
```

## Task statuses

A task can have one of three statuses: `todo`, `in_progress`, or `done`.
