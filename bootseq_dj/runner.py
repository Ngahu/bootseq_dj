from bootseq import default_registry
from bootseq.runner import Runner
from bootseq.filters import Filters


def run_bootseq(
    *,
    only=None,
    skip=None,
    tags=None,
    dry_run=False,
    max_workers=4,
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
    )

    runner.run()
