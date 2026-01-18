import importlib
from django.apps import apps
import logging

log = logging.getLogger(__name__)

BOOTSTRAP_MODULE_NAMES = (
    "bootstrap",
    "bootseq",
)


def autodiscover_bootseq():
    """
    Import bootstrap modules from all installed Django apps.
    """
    for app_config in apps.get_app_configs():
        for module_name in BOOTSTRAP_MODULE_NAMES:
            try:
                importlib.import_module(f"{app_config.name}.{module_name}")
            except ModuleNotFoundError:
                continue
            except Exception:
                log.exception(
                    "Failed importing %s.%s",
                    app_config.name,
                    module_name,
                )
