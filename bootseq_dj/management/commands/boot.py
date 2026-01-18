from django.core.management.base import BaseCommand
from bootseq_dj.runner import run_bootseq


class Command(BaseCommand):
    help = "Run bootseq bootstrap tasks"

    def add_arguments(self, parser):
        parser.add_argument("--dry-run", action="store_true")
        parser.add_argument("--only", nargs="*")
        parser.add_argument("--skip", nargs="*")
        parser.add_argument("--tags", nargs="*")
        parser.add_argument("--max-workers", type=int, default=4)

    def handle(self, *args, **options):
        run_bootseq(
            only=options["only"],
            skip=options["skip"],
            tags=options["tags"],
            dry_run=options["dry_run"],
            max_workers=options["max_workers"],
        )
        self.stdout.write(self.style.SUCCESS("✔✔✔✔✔ Successffully boot up"))
