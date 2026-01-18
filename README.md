# bootseq-dj

Django integration for **bootseq**, a deterministic bootstrap sequencing engine.

## Installation

```bash
pip install git+https://github.com/Ngahu/bootseq_dj.git#egg=bootseq_dj

```

Add to INSTALLED_APPS:

```
INSTALLED_APPS = [
    ...
    "bootseq_dj",
]

```


### Defining Tasks

Create bootstrap.py in any Django app:
```python
from bootseq import register

@register(tags={"auth"})
def create_roles():
    ...
```

#### Running
```
python manage.py boot
python manage.py boot --dry-run
python manage.py boot --tags auth
```