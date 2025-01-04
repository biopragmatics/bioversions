# Summary of Errors

- DisGeNet - failed to resolve DisGeNet
- Antibody Registry - failed to resolve Antibody Registry
- DrugBank - failed to resolve DrugBank

## DisGeNet

Using class: `DisGeNetGetter`

```python-traceback
Traceback (most recent call last):
  File "/home/runner/work/bioversions/bioversions/.tox/update/lib/python3.12/site-packages/requests/models.py", line 974, in json
    return complexjson.loads(self.text, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.12.8/x64/lib/python3.12/json/__init__.py", line 346, in loads
    return _default_decoder.decode(s)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.12.8/x64/lib/python3.12/json/decoder.py", line 338, in decode
    obj, end = self.raw_decode(s, idx=_w(s, 0).end())
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.12.8/x64/lib/python3.12/json/decoder.py", line 356, in raw_decode
    raise JSONDecodeError("Expecting value", s, err.value) from None
json.decoder.JSONDecodeError: Expecting value: line 1 column 1 (char 0)

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/home/runner/work/bioversions/bioversions/src/bioversions/sources/__init__.py", line 216, in _iter_versions
    yv = resolve(cls.name)
         ^^^^^^^^^^^^^^^^^
  File "/home/runner/work/bioversions/bioversions/src/bioversions/sources/__init__.py", line 169, in resolve
    return _resolve_helper_cached(name)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/runner/work/bioversions/bioversions/.tox/update/lib/python3.12/site-packages/cachier/core.py", line 258, in func_wrapper
    return _calc_entry(core, key, func, args, kwds)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/runner/work/bioversions/bioversions/.tox/update/lib/python3.12/site-packages/cachier/core.py", line 61, in _calc_entry
    func_res = func(*args, **kwds)
               ^^^^^^^^^^^^^^^^^^^
  File "/home/runner/work/bioversions/bioversions/src/bioversions/sources/__init__.py", line 176, in _resolve_helper_cached
    return _resolve_helper(name)
           ^^^^^^^^^^^^^^^^^^^^^
  File "/home/runner/work/bioversions/bioversions/src/bioversions/sources/__init__.py", line 182, in _resolve_helper
    return getter.resolve()
           ^^^^^^^^^^^^^^^^
  File "/home/runner/work/bioversions/bioversions/src/bioversions/utils.py", line 216, in resolve
    version=cls.version,
            ^^^^^^^^^^^
  File "/home/runner/work/bioversions/bioversions/src/bioversions/utils.py", line 94, in version
    if isinstance(cls._cache_prop, str):
                  ^^^^^^^^^^^^^^^
  File "/home/runner/work/bioversions/bioversions/src/bioversions/utils.py", line 88, in _cache_prop
    cls._cache = cls().get()
                 ^^^^^^^^^^^
  File "/home/runner/work/bioversions/bioversions/src/bioversions/sources/disgenet.py", line 24, in get
    res_json = res.json()
               ^^^^^^^^^^
  File "/home/runner/work/bioversions/bioversions/.tox/update/lib/python3.12/site-packages/requests/models.py", line 978, in json
    raise RequestsJSONDecodeError(e.msg, e.doc, e.pos)
requests.exceptions.JSONDecodeError: Expecting value: line 1 column 1 (char 0)

```

## Antibody Registry

Using class: `AntibodyRegistryGetter`

```python-traceback
Traceback (most recent call last):
  File "/home/runner/work/bioversions/bioversions/src/bioversions/sources/__init__.py", line 216, in _iter_versions
    yv = resolve(cls.name)
         ^^^^^^^^^^^^^^^^^
  File "/home/runner/work/bioversions/bioversions/src/bioversions/sources/__init__.py", line 169, in resolve
    return _resolve_helper_cached(name)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/runner/work/bioversions/bioversions/.tox/update/lib/python3.12/site-packages/cachier/core.py", line 258, in func_wrapper
    return _calc_entry(core, key, func, args, kwds)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/runner/work/bioversions/bioversions/.tox/update/lib/python3.12/site-packages/cachier/core.py", line 61, in _calc_entry
    func_res = func(*args, **kwds)
               ^^^^^^^^^^^^^^^^^^^
  File "/home/runner/work/bioversions/bioversions/src/bioversions/sources/__init__.py", line 176, in _resolve_helper_cached
    return _resolve_helper(name)
           ^^^^^^^^^^^^^^^^^^^^^
  File "/home/runner/work/bioversions/bioversions/src/bioversions/sources/__init__.py", line 182, in _resolve_helper
    return getter.resolve()
           ^^^^^^^^^^^^^^^^
  File "/home/runner/work/bioversions/bioversions/src/bioversions/utils.py", line 216, in resolve
    version=cls.version,
            ^^^^^^^^^^^
  File "/home/runner/work/bioversions/bioversions/src/bioversions/utils.py", line 94, in version
    if isinstance(cls._cache_prop, str):
                  ^^^^^^^^^^^^^^^
  File "/home/runner/work/bioversions/bioversions/src/bioversions/utils.py", line 88, in _cache_prop
    cls._cache = cls().get()
                 ^^^^^^^^^^^
  File "/home/runner/work/bioversions/bioversions/src/bioversions/sources/antibodyregistry.py", line 21, in get
    return soup.find(**{"class": "footer"}).find("a").text.lstrip("v")
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
AttributeError: 'NoneType' object has no attribute 'find'

```

## DrugBank

Using class: `DrugBankGetter`

```python-traceback
Traceback (most recent call last):
  File "/home/runner/work/bioversions/bioversions/src/bioversions/sources/__init__.py", line 216, in _iter_versions
    yv = resolve(cls.name)
         ^^^^^^^^^^^^^^^^^
  File "/home/runner/work/bioversions/bioversions/src/bioversions/sources/__init__.py", line 169, in resolve
    return _resolve_helper_cached(name)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/runner/work/bioversions/bioversions/.tox/update/lib/python3.12/site-packages/cachier/core.py", line 258, in func_wrapper
    return _calc_entry(core, key, func, args, kwds)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/runner/work/bioversions/bioversions/.tox/update/lib/python3.12/site-packages/cachier/core.py", line 61, in _calc_entry
    func_res = func(*args, **kwds)
               ^^^^^^^^^^^^^^^^^^^
  File "/home/runner/work/bioversions/bioversions/src/bioversions/sources/__init__.py", line 176, in _resolve_helper_cached
    return _resolve_helper(name)
           ^^^^^^^^^^^^^^^^^^^^^
  File "/home/runner/work/bioversions/bioversions/src/bioversions/sources/__init__.py", line 182, in _resolve_helper
    return getter.resolve()
           ^^^^^^^^^^^^^^^^
  File "/home/runner/work/bioversions/bioversions/src/bioversions/utils.py", line 216, in resolve
    version=cls.version,
            ^^^^^^^^^^^
  File "/home/runner/work/bioversions/bioversions/src/bioversions/utils.py", line 94, in version
    if isinstance(cls._cache_prop, str):
                  ^^^^^^^^^^^^^^^
  File "/home/runner/work/bioversions/bioversions/src/bioversions/utils.py", line 88, in _cache_prop
    cls._cache = cls().get()
                 ^^^^^^^^^^^
  File "/home/runner/work/bioversions/bioversions/src/bioversions/sources/drugbank.py", line 28, in get
    res.raise_for_status()
  File "/home/runner/work/bioversions/bioversions/.tox/update/lib/python3.12/site-packages/requests/models.py", line 1024, in raise_for_status
    raise HTTPError(http_error_msg, response=self)
requests.exceptions.HTTPError: 403 Client Error: Forbidden for url: https://go.drugbank.com/releases.json

```

