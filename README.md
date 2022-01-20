# dalec-discourse

Django Aggregate a Lot of External Content -- Discourse

Aggregate last discourse issue or event from a given discourse instance.

Plugin of [dalec](https://dev.webu.coop/w/i/dalec).

## Installation

We use [pydiscourse](https://github.com/bennylope/pydiscourse/), but for version >= 1.2,
that is not already published. So you should mannualy install the master branch.

```
pip install git+https://github.com/bennylope/pydiscourse.git@188decb02accb414b4c0a609b94881d09eec7689
```

then install the module:

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

Real examples:

### Topics

Retrieves latest topics:
```django
{% dalec "discourse" "topic" %}
```

Retrieves latest topics from a category:
```django
{% dalec "discourse" "tpic" channel="category" channel_object="15" %}
```

### Categories

Retrieves discourse categories:
```django
{% dalec "discourse" "category" %}
```


## Settings

Django settings must define:

  - `DALEC_DISCOURSE_BASE_URL` : discourse instance url (ex: `https://discourse.org/`)
  - `DALEC_DISCOURSE_API_USERNAME` : discourse username (ex: `admin`)
  - `DALEC_DISCOURSE_API_TOKEN` : discourse api token (ex: `azeazeaezdfqsmlkrjzr`)

It could also define the login/password attribute, and then this auth method will be used
(may be usefull for htaccess access for instance):

  - `DISCOURSE_AUTH_USERNAME`
  - `DISCOURSE_AUTH_PASSWORD`


