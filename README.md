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


# List all tasks
python manage.py boot plan

# List tasks with specific tags
python manage.py boot plan --tags auth

# Run all tasks
python manage.py boot run

# Run with dry-run (no actual execution)
python manage.py boot run --dry-run

# Run without progress bar (good for logs/CI)
python manage.py boot run --no-progress

# Run specific tasks only
python manage.py boot run --only auth.create_roles billing.setup
```