from django.apps import AppConfig


class BootseqDjangoConfig(AppConfig):
    name = "bootseq_dj"
    verbose_name = "Bootseq Django Adapter"

    def ready(self):
        # Autodiscover bootstrap modules safely
        from .autodiscover import autodiscover_bootseq

        autodiscover_bootseq()
