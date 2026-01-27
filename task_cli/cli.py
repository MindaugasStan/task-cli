import argparse
from typing import Sequence

from task_cli.models import Task
from task_cli.services import add_task, update_task, delete_task, mark_task_in_progress, mark_task_done, list_tasks


def run(argv: Sequence | None = None) -> int:
    parser = argparse.ArgumentParser(prog='task_cli')
    subparsers = parser.add_subparsers(dest='command', required=True)

    add_parser = subparsers.add_parser('add', help='Add a new task')
    add_parser.add_argument('task')
    add_parser.set_defaults(func=handle_add)

    update_parser = subparsers.add_parser('update', help='Update a task')
    update_parser.add_argument('task_id', type=int)
    update_parser.add_argument('description')
    update_parser.set_defaults(func=handle_update)

    delete_parser = subparsers.add_parser('delete', help='Delete a task')
    delete_parser.add_argument('task_id', type=int)
    delete_parser.set_defaults(func=handle_delete)

    in_progress_parser = subparsers.add_parser('mark-in-progress', help='Mark a task as in progress')
    in_progress_parser.add_argument('task_id', type=int)
    in_progress_parser.set_defaults(func=handle_in_progress)

    done_parser = subparsers.add_parser('mark-done', help='Mark a task as done')
    done_parser.add_argument('task_id', type=int)
    done_parser.set_defaults(func=handle_done)

    list_parser = subparsers.add_parser('list', help='List all tasks by their statuses')
    list_parser.add_argument(
        "status",
        nargs="?",
        choices=["todo", "in-progress", "done"],
    )
    list_parser.set_defaults(func=handle_list)

    args = parser.parse_args(argv)

    return args.func(args)


def handle_add(args: argparse.Namespace) -> int:
    task = add_task(args.task)
    if task:
        print(f"Task added successfully (ID: {task.id})")
        return 0
    return 1


def handle_update(args: argparse.Namespace) -> int:
    try:
        task = update_task(args.task_id, args.description)
        print(f"Task updated: {task}")
        return 0
    except KeyError as error:
        print(error)
        return 1


def handle_delete(args: argparse.Namespace) -> int:
    try:
        delete_task(args.task_id)
    except KeyError as error:
        print(error)
        return 1
    return 0


def handle_in_progress(args: argparse.Namespace) -> int:
    try:
        mark_task_in_progress(args.task_id)
        return 0
    except KeyError as error:
        print(error)
        return 1


def handle_done(args: argparse.Namespace) -> int:
    try:
        mark_task_done(args.task_id)
        return 0
    except KeyError as error:
        print(error)
        return 1


def handle_list(args: argparse.Namespace) -> int:
    tasks = list_tasks(args.status)
    if not tasks:
        print("No tasks found")
        return 0
    for task_dict in tasks:
        task = Task.from_dict(task_dict)
        print(task)
    return 0
