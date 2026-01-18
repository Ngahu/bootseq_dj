from bootseq.registry import default_registry
from bootseq_dj.autodiscover import autodiscover_bootseq


def test_autodiscover_does_not_crash(settings):
    settings.INSTALLED_APPS = [
        "django.contrib.contenttypes",
    ]
    autodiscover_bootseq()
