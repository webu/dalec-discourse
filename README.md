# dalec-discourse

Django Aggregate a Lot of External Content -- Discourse

Aggregate last discourse issue or event from a given discourse instance.

Plugin of [dalec](https://dev.webu.coop/w/i/dalec).

## Installation

```
pip install dalec_discourse
```

In django settings `INSTALLED_APPS`, add:

```
INSTALLED_APPS = [
    ...
    "dalec",
    "dalec_prime",
    "dalec_discourse",
    ...
    ]
```


## Usage

General usage:
```django
{% load dalec %}

{% dalec "discourse" content_type [channel=None] [channel_object=None] [template=None] %}
```

## Settings

Django settings must define:

  - `DALEC_DISCOURSE_BASE_URL` : discourse instance url (ex: `https://discourse.org/`)
  - `DALEC_DISCOURSE_API_USERNAME` : discourse username (ex: `admin`)
  - `DALEC_DISCOURSE_API_TOKEN` : discourse api token (ex: `azeazeaezdfqsmlkrjzr`)


