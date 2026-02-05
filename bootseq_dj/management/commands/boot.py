from django.core.management.base import BaseCommand
from bootseq_dj.runner import run_bootseq, plan_bootseq


class Command(BaseCommand):
    help = "Run bootseq bootstrap tasks"

    def add_arguments(self, parser):
        parser.add_argument(
            "command",
            nargs="?",
            default="run",
            choices=["run", "plan"],
            help="Command to execute: 'run' (default) or 'plan'",
        )
        parser.add_argument(
            "--dry-run",
            action="store_true",
            help="Simulate execution without running tasks",
        )
        parser.add_argument(
            "--only", nargs="*", help="Only run these tasks (supports wildcards)"
        )
        parser.add_argument(
            "--skip", nargs="*", help="Skip these tasks (supports wildcards)"
        )
        parser.add_argument("--tags", nargs="*", help="Only run tasks with these tags")
        parser.add_argument(
            "--max-workers", type=int, default=4, help="Max parallel workers"
        )
        parser.add_argument(
            "--no-progress", action="store_true", help="Disable progress bar"
        )

    def handle(self, *args, **options):
        command = options["command"]

        if command == "plan":
            plan_bootseq(
                only=options["only"],
                skip=options["skip"],
                tags=options["tags"],
                stdout=self.stdout,
            )
            return

        # command == "run"
        run_bootseq(
            only=options["only"],
            skip=options["skip"],
            tags=options["tags"],
            dry_run=options["dry_run"],
            max_workers=options["max_workers"],
            show_progress=not options["no_progress"],
        )

        if not options["dry_run"]:
            self.stdout.write(self.style.SUCCESS("✔✔✔✔✔ Successfully boot up"))
