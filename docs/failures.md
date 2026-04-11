# Summary of Errors

- **DepMap**
  `[DepMap] failed to resolve: Expecting value: line 1 column 1 (char 0)`
- **National Cancer Institute Thesaurus**
  `[ncit] issue parsing: Issue in NCItGetter with date 2026-04-06 and fmt %B %d, %Y`
- **Research Organization Registry** `[ror] issue parsing: Could not look up
  zenodo/api_token and no default given.

This can be solved with one of the following:

1. Set the ZENODO_API_TOKEN environment variable
   - Windows, via GUI: https://www.computerhope.com/issues/ch000549.htm
   - Windows, via CLI:
     https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/set_1
   - Mac OS:
     https://apple.stackexchange.com/questions/106778/how-do-i-set-environment-variables-on-os-x
   - Linux:
     https://www.freecodecamp.org/news/how-to-set-an-environment-variable-in-linux/

2. Use the PyStow CLI from the command line to set the configuration like so:

   $ pystow set zenodo api_token <value>

   This creates an INI file in /home/runner/.config/zenodo.ini with the
   configuration in the right place.

3. Create/edit an INI file in /home/runner/.config/zenodo.ini and manually fill
   it in by 1) creating a section inside it called [zenodo] and 2) setting a
   value for api_token = <value> that looks like:

   # /home/runner/.config/zenodo.ini

   [zenodo] api_token = <value>

See https://github.com/cthoyt/pystow#%EF%B8%8F%EF%B8%8F-configuration for more
information. `

## DepMap

Using class: `DepMapGetter`

```python-traceback
Traceback (most recent call last):
  File "/home/runner/work/bioversions/bioversions/.tox/update/lib/python3.12/site-packages/requests/models.py", line 978, in json
    return complexjson.loads(self.text, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.12.13/x64/lib/python3.12/json/__init__.py", line 346, in loads
    return _default_decoder.decode(s)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.12.13/x64/lib/python3.12/json/decoder.py", line 338, in decode
    obj, end = self.raw_decode(s, idx=_w(s, 0).end())
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.12.13/x64/lib/python3.12/json/decoder.py", line 356, in raw_decode
    raise JSONDecodeError("Expecting value", s, err.value) from None
json.decoder.JSONDecodeError: Expecting value: line 1 column 1 (char 0)

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/home/runner/work/bioversions/bioversions/src/bioversions/sources/__init__.py", line 271, in iter_versions
    yv = resolve(cls)
         ^^^^^^^^^^^^
  File "/home/runner/work/bioversions/bioversions/src/bioversions/sources/__init__.py", line 193, in resolve
    return _resolve_helper_cached(name)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/runner/work/bioversions/bioversions/.tox/update/lib/python3.12/site-packages/cachier/core.py", line 606, in func_wrapper
    return _call(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^
  File "/home/runner/work/bioversions/bioversions/.tox/update/lib/python3.12/site-packages/cachier/core.py", line 459, in _call
    return _calc_entry(core, key, func, args, kwds, _print)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/runner/work/bioversions/bioversions/.tox/update/lib/python3.12/site-packages/cachier/core.py", line 84, in _calc_entry
    func_res = func(*args, **kwds)
               ^^^^^^^^^^^^^^^^^^^
  File "/home/runner/work/bioversions/bioversions/src/bioversions/sources/__init__.py", line 203, in _resolve_helper_cached
    return getter.resolve()
           ^^^^^^^^^^^^^^^^
  File "/home/runner/work/bioversions/bioversions/src/bioversions/utils.py", line 215, in resolve
    version=cls.version,
            ^^^^^^^^^^^
  File "/home/runner/work/bioversions/bioversions/src/bioversions/utils.py", line 93, in version
    if isinstance(cls._cache_prop, str):
                  ^^^^^^^^^^^^^^^
  File "/home/runner/work/bioversions/bioversions/src/bioversions/utils.py", line 87, in _cache_prop
    cls._cache = cls().get()
                 ^^^^^^^^^^^
  File "/home/runner/work/bioversions/bioversions/src/bioversions/sources/depmap.py", line 23, in get
    latest = next(release for release in res.json()["releaseData"] if release["isLatest"])
                                         ^^^^^^^^^^
  File "/home/runner/work/bioversions/bioversions/.tox/update/lib/python3.12/site-packages/requests/models.py", line 982, in json
    raise RequestsJSONDecodeError(e.msg, e.doc, e.pos)
requests.exceptions.JSONDecodeError: Expecting value: line 1 column 1 (char 0)

```

## National Cancer Institute Thesaurus

Using class: `NCItGetter`

```python-traceback
Traceback (most recent call last):
  File "/home/runner/work/bioversions/bioversions/src/bioversions/sources/__init__.py", line 271, in iter_versions
    yv = resolve(cls)
         ^^^^^^^^^^^^
  File "/home/runner/work/bioversions/bioversions/src/bioversions/sources/__init__.py", line 193, in resolve
    return _resolve_helper_cached(name)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/runner/work/bioversions/bioversions/.tox/update/lib/python3.12/site-packages/cachier/core.py", line 606, in func_wrapper
    return _call(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^
  File "/home/runner/work/bioversions/bioversions/.tox/update/lib/python3.12/site-packages/cachier/core.py", line 459, in _call
    return _calc_entry(core, key, func, args, kwds, _print)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/runner/work/bioversions/bioversions/.tox/update/lib/python3.12/site-packages/cachier/core.py", line 84, in _calc_entry
    func_res = func(*args, **kwds)
               ^^^^^^^^^^^^^^^^^^^
  File "/home/runner/work/bioversions/bioversions/src/bioversions/sources/__init__.py", line 203, in _resolve_helper_cached
    return getter.resolve()
           ^^^^^^^^^^^^^^^^
  File "/home/runner/work/bioversions/bioversions/src/bioversions/utils.py", line 219, in resolve
    date=cls.date,
         ^^^^^^^^
  File "/home/runner/work/bioversions/bioversions/src/bioversions/utils.py", line 120, in date
    raise ValueError(
ValueError: Issue in NCItGetter with date 2026-04-06 and fmt %B %d, %Y

```

## Research Organization Registry

Using class: `RORGetter`

```python-traceback
Traceback (most recent call last):
  File "/home/runner/work/bioversions/bioversions/src/bioversions/sources/__init__.py", line 271, in iter_versions
    yv = resolve(cls)
         ^^^^^^^^^^^^
  File "/home/runner/work/bioversions/bioversions/src/bioversions/sources/__init__.py", line 193, in resolve
    return _resolve_helper_cached(name)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/runner/work/bioversions/bioversions/.tox/update/lib/python3.12/site-packages/cachier/core.py", line 606, in func_wrapper
    return _call(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^
  File "/home/runner/work/bioversions/bioversions/.tox/update/lib/python3.12/site-packages/cachier/core.py", line 459, in _call
    return _calc_entry(core, key, func, args, kwds, _print)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/runner/work/bioversions/bioversions/.tox/update/lib/python3.12/site-packages/cachier/core.py", line 84, in _calc_entry
    func_res = func(*args, **kwds)
               ^^^^^^^^^^^^^^^^^^^
  File "/home/runner/work/bioversions/bioversions/src/bioversions/sources/__init__.py", line 203, in _resolve_helper_cached
    return getter.resolve()
           ^^^^^^^^^^^^^^^^
  File "/home/runner/work/bioversions/bioversions/src/bioversions/utils.py", line 215, in resolve
    version=cls.version,
            ^^^^^^^^^^^
  File "/home/runner/work/bioversions/bioversions/src/bioversions/utils.py", line 93, in version
    if isinstance(cls._cache_prop, str):
                  ^^^^^^^^^^^^^^^
  File "/home/runner/work/bioversions/bioversions/src/bioversions/utils.py", line 87, in _cache_prop
    cls._cache = cls().get()
                 ^^^^^^^^^^^
  File "/home/runner/work/bioversions/bioversions/src/bioversions/sources/ror.py", line 22, in get
    version_info = ror_downloader.get_version_info(download=False)
                   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/runner/work/bioversions/bioversions/.tox/update/lib/python3.12/site-packages/ror_downloader/api.py", line 227, in get_version_info
    client = zenodo_client.Zenodo()
             ^^^^^^^^^^^^^^^^^^^^^^
  File "/home/runner/work/bioversions/bioversions/.tox/update/lib/python3.12/site-packages/zenodo_client/api.py", line 117, in __init__
    self.access_token = pystow.get_config(
                        ^^^^^^^^^^^^^^^^^^
  File "/home/runner/work/bioversions/bioversions/.tox/update/lib/python3.12/site-packages/pystow/config_api.py", line 161, in get_config
    raise ConfigError(module=module, key=key)
pystow.config_api.ConfigError: Could not look up zenodo/api_token and no default given.

This can be solved with one of the following:

1. Set the ZENODO_API_TOKEN environment variable

   - Windows, via GUI: https://www.computerhope.com/issues/ch000549.htm
   - Windows, via CLI: https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/set_1
   - Mac OS: https://apple.stackexchange.com/questions/106778/how-do-i-set-environment-variables-on-os-x
   - Linux: https://www.freecodecamp.org/news/how-to-set-an-environment-variable-in-linux/

2. Use the PyStow CLI from the command line to
   set the configuration like so:

   $ pystow set zenodo api_token <value>

   This creates an INI file in /home/runner/.config/zenodo.ini
   with the configuration in the right place.

3. Create/edit an INI file in /home/runner/.config/zenodo.ini and manually
   fill it in by 1) creating a section inside it called [zenodo]
   and 2) setting a value for api_token = <value> that looks like:

   # /home/runner/.config/zenodo.ini
   [zenodo]
   api_token = <value>

See https://github.com/cthoyt/pystow#%EF%B8%8F%EF%B8%8F-configuration for more information.


```
