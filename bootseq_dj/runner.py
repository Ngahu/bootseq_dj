from django.db import transaction
from bootseq import default_registry
from bootseq.runner import Runner
from bootseq.filters import Filters
from bootseq.resolver import resolve


def run_bootseq(
    *,
    only=None,
    skip=None,
    tags=None,
    dry_run=False,
    max_workers=1,
    show_progress=True,
):
    filters = Filters(
        only=only,
        skip=skip,
        tags=tags,
    )

    runner = Runner(
        default_registry,
        filters=filters,
        dry_run=dry_run,
        max_workers=max_workers,
        show_progress=show_progress,
    )

    if dry_run:
        runner.run()
        return

    with transaction.atomic():
        runner.run()


def plan_bootseq(*, only=None, skip=None, tags=None, stdout=None):
    """List all registered tasks in execution order."""
    filters = Filters(only=only, skip=skip, tags=tags)
    tasks = resolve(default_registry.all())

    if filters:
        tasks = [t for t in tasks if filters.allow(t)]

    if not tasks:
        if stdout:
            stdout.write("No tasks registered.")
        else:
            print("No tasks registered.")
        return

    # Format output
    header = f"{'ID':<40} {'Order':<8} {'Tags':<20} {'Requires'}"
    separator = "-" * 90
    lines = ["\n", header, separator]

    for task in tasks:
        task_tags = ", ".join(task.tags) if task.tags else "-"
        requires = ", ".join(task.requires) if task.requires else "-"
        lines.append(f"{task.id:<40} {task.order:<8} {task_tags:<20} {requires}")

    lines.append(f"\nTotal: {len(tasks)} task(s)\n")

    output = "\n".join(lines)
    if stdout:
        stdout.write(output)
    else:
        print(output)
