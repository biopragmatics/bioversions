# Summary of Errors

- **PathBank**
  `[pathbank] failed to resolve: HTTPSConnectionPool(host='pathbank.org', port=443): Read timed out. (read timeout=15)`
- **SILVA ribosomal RNA database** `[silva.taxon] issue parsing: 'date'`
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

- **Ensembl**
  `[ensembl] failed to resolve: HTTPSConnectionPool(host='useast.ensembl.org', port=443): Read timed out. (read timeout=15)`

## PathBank

Using class: `PathBankGetter`

```python-traceback
Traceback (most recent call last):
  File "/home/runner/work/bioversions/bioversions/.tox/update/lib/python3.12/site-packages/urllib3/connectionpool.py", line 534, in _make_request
    response = conn.getresponse()
               ^^^^^^^^^^^^^^^^^^
  File "/home/runner/work/bioversions/bioversions/.tox/update/lib/python3.12/site-packages/urllib3/connection.py", line 571, in getresponse
    httplib_response = super().getresponse()
                       ^^^^^^^^^^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.12.12/x64/lib/python3.12/http/client.py", line 1430, in getresponse
    response.begin()
  File "/opt/hostedtoolcache/Python/3.12.12/x64/lib/python3.12/http/client.py", line 331, in begin
    version, status, reason = self._read_status()
                              ^^^^^^^^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.12.12/x64/lib/python3.12/http/client.py", line 292, in _read_status
    line = str(self.fp.readline(_MAXLINE + 1), "iso-8859-1")
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.12.12/x64/lib/python3.12/socket.py", line 720, in readinto
    return self._sock.recv_into(b)
           ^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.12.12/x64/lib/python3.12/ssl.py", line 1251, in recv_into
    return self.read(nbytes, buffer)
           ^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.12.12/x64/lib/python3.12/ssl.py", line 1103, in read
    return self._sslobj.read(len, buffer)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TimeoutError: The read operation timed out

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "/home/runner/work/bioversions/bioversions/.tox/update/lib/python3.12/site-packages/requests/adapters.py", line 644, in send
    resp = conn.urlopen(
           ^^^^^^^^^^^^^
  File "/home/runner/work/bioversions/bioversions/.tox/update/lib/python3.12/site-packages/urllib3/connectionpool.py", line 841, in urlopen
    retries = retries.increment(
              ^^^^^^^^^^^^^^^^^^
  File "/home/runner/work/bioversions/bioversions/.tox/update/lib/python3.12/site-packages/urllib3/util/retry.py", line 490, in increment
    raise reraise(type(error), error, _stacktrace)
          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/runner/work/bioversions/bioversions/.tox/update/lib/python3.12/site-packages/urllib3/util/util.py", line 39, in reraise
    raise value
  File "/home/runner/work/bioversions/bioversions/.tox/update/lib/python3.12/site-packages/urllib3/connectionpool.py", line 787, in urlopen
    response = self._make_request(
               ^^^^^^^^^^^^^^^^^^^
  File "/home/runner/work/bioversions/bioversions/.tox/update/lib/python3.12/site-packages/urllib3/connectionpool.py", line 536, in _make_request
    self._raise_timeout(err=e, url=url, timeout_value=read_timeout)
  File "/home/runner/work/bioversions/bioversions/.tox/update/lib/python3.12/site-packages/urllib3/connectionpool.py", line 367, in _raise_timeout
    raise ReadTimeoutError(
urllib3.exceptions.ReadTimeoutError: HTTPSConnectionPool(host='pathbank.org', port=443): Read timed out. (read timeout=15)

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/home/runner/work/bioversions/bioversions/src/bioversions/sources/__init__.py", line 271, in iter_versions
    yv = resolve(cls)
         ^^^^^^^^^^^^
  File "/home/runner/work/bioversions/bioversions/src/bioversions/sources/__init__.py", line 193, in resolve
    return _resolve_helper_cached(name)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/runner/work/bioversions/bioversions/.tox/update/lib/python3.12/site-packages/cachier/core.py", line 393, in func_wrapper
    return _call(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^
  File "/home/runner/work/bioversions/bioversions/.tox/update/lib/python3.12/site-packages/cachier/core.py", line 332, in _call
    return _calc_entry(core, key, func, args, kwds)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/runner/work/bioversions/bioversions/.tox/update/lib/python3.12/site-packages/cachier/core.py", line 66, in _calc_entry
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
  File "/home/runner/work/bioversions/bioversions/src/bioversions/sources/pathbank.py", line 21, in get
    soup = get_soup(URL)
           ^^^^^^^^^^^^^
  File "/home/runner/work/bioversions/bioversions/.tox/update/lib/python3.12/site-packages/pystow/utils.py", line 1522, in get_soup
    res = requests.get(url, verify=verify, timeout=timeout or 15, headers=headers)
          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/runner/work/bioversions/bioversions/.tox/update/lib/python3.12/site-packages/requests/api.py", line 73, in get
    return request("get", url, params=params, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/runner/work/bioversions/bioversions/.tox/update/lib/python3.12/site-packages/requests/api.py", line 59, in request
    return session.request(method=method, url=url, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/runner/work/bioversions/bioversions/.tox/update/lib/python3.12/site-packages/requests/sessions.py", line 589, in request
    resp = self.send(prep, **send_kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/runner/work/bioversions/bioversions/.tox/update/lib/python3.12/site-packages/requests/sessions.py", line 703, in send
    r = adapter.send(request, **kwargs)
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/runner/work/bioversions/bioversions/.tox/update/lib/python3.12/site-packages/requests/adapters.py", line 690, in send
    raise ReadTimeout(e, request=request)
requests.exceptions.ReadTimeout: HTTPSConnectionPool(host='pathbank.org', port=443): Read timed out. (read timeout=15)

```

## SILVA ribosomal RNA database

Using class: `SILVAGetter`

```python-traceback
Traceback (most recent call last):
  File "/home/runner/work/bioversions/bioversions/src/bioversions/sources/__init__.py", line 271, in iter_versions
    yv = resolve(cls)
         ^^^^^^^^^^^^
  File "/home/runner/work/bioversions/bioversions/src/bioversions/sources/__init__.py", line 193, in resolve
    return _resolve_helper_cached(name)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/runner/work/bioversions/bioversions/.tox/update/lib/python3.12/site-packages/cachier/core.py", line 393, in func_wrapper
    return _call(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^
  File "/home/runner/work/bioversions/bioversions/.tox/update/lib/python3.12/site-packages/cachier/core.py", line 332, in _call
    return _calc_entry(core, key, func, args, kwds)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/runner/work/bioversions/bioversions/.tox/update/lib/python3.12/site-packages/cachier/core.py", line 66, in _calc_entry
    func_res = func(*args, **kwds)
               ^^^^^^^^^^^^^^^^^^^
  File "/home/runner/work/bioversions/bioversions/src/bioversions/sources/__init__.py", line 203, in _resolve_helper_cached
    return getter.resolve()
           ^^^^^^^^^^^^^^^^
  File "/home/runner/work/bioversions/bioversions/src/bioversions/utils.py", line 219, in resolve
    date=cls.date,
         ^^^^^^^^
  File "/home/runner/work/bioversions/bioversions/src/bioversions/utils.py", line 110, in date
    date = cls._cache_prop["date"]
           ~~~~~~~~~~~~~~~^^^^^^^^
KeyError: 'date'

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
  File "/home/runner/work/bioversions/bioversions/.tox/update/lib/python3.12/site-packages/cachier/core.py", line 393, in func_wrapper
    return _call(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^
  File "/home/runner/work/bioversions/bioversions/.tox/update/lib/python3.12/site-packages/cachier/core.py", line 332, in _call
    return _calc_entry(core, key, func, args, kwds)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/runner/work/bioversions/bioversions/.tox/update/lib/python3.12/site-packages/cachier/core.py", line 66, in _calc_entry
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
  File "/home/runner/work/bioversions/bioversions/.tox/update/lib/python3.12/site-packages/zenodo_client/api.py", line 109, in __init__
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

## Ensembl

Using class: `EnsemblGetter`

```python-traceback
Traceback (most recent call last):
  File "/home/runner/work/bioversions/bioversions/.tox/update/lib/python3.12/site-packages/urllib3/connectionpool.py", line 534, in _make_request
    response = conn.getresponse()
               ^^^^^^^^^^^^^^^^^^
  File "/home/runner/work/bioversions/bioversions/.tox/update/lib/python3.12/site-packages/urllib3/connection.py", line 571, in getresponse
    httplib_response = super().getresponse()
                       ^^^^^^^^^^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.12.12/x64/lib/python3.12/http/client.py", line 1430, in getresponse
    response.begin()
  File "/opt/hostedtoolcache/Python/3.12.12/x64/lib/python3.12/http/client.py", line 331, in begin
    version, status, reason = self._read_status()
                              ^^^^^^^^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.12.12/x64/lib/python3.12/http/client.py", line 292, in _read_status
    line = str(self.fp.readline(_MAXLINE + 1), "iso-8859-1")
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.12.12/x64/lib/python3.12/socket.py", line 720, in readinto
    return self._sock.recv_into(b)
           ^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.12.12/x64/lib/python3.12/ssl.py", line 1251, in recv_into
    return self.read(nbytes, buffer)
           ^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.12.12/x64/lib/python3.12/ssl.py", line 1103, in read
    return self._sslobj.read(len, buffer)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TimeoutError: The read operation timed out

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "/home/runner/work/bioversions/bioversions/.tox/update/lib/python3.12/site-packages/requests/adapters.py", line 644, in send
    resp = conn.urlopen(
           ^^^^^^^^^^^^^
  File "/home/runner/work/bioversions/bioversions/.tox/update/lib/python3.12/site-packages/urllib3/connectionpool.py", line 841, in urlopen
    retries = retries.increment(
              ^^^^^^^^^^^^^^^^^^
  File "/home/runner/work/bioversions/bioversions/.tox/update/lib/python3.12/site-packages/urllib3/util/retry.py", line 490, in increment
    raise reraise(type(error), error, _stacktrace)
          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/runner/work/bioversions/bioversions/.tox/update/lib/python3.12/site-packages/urllib3/util/util.py", line 39, in reraise
    raise value
  File "/home/runner/work/bioversions/bioversions/.tox/update/lib/python3.12/site-packages/urllib3/connectionpool.py", line 787, in urlopen
    response = self._make_request(
               ^^^^^^^^^^^^^^^^^^^
  File "/home/runner/work/bioversions/bioversions/.tox/update/lib/python3.12/site-packages/urllib3/connectionpool.py", line 536, in _make_request
    self._raise_timeout(err=e, url=url, timeout_value=read_timeout)
  File "/home/runner/work/bioversions/bioversions/.tox/update/lib/python3.12/site-packages/urllib3/connectionpool.py", line 367, in _raise_timeout
    raise ReadTimeoutError(
urllib3.exceptions.ReadTimeoutError: HTTPSConnectionPool(host='useast.ensembl.org', port=443): Read timed out. (read timeout=15)

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/home/runner/work/bioversions/bioversions/src/bioversions/sources/__init__.py", line 271, in iter_versions
    yv = resolve(cls)
         ^^^^^^^^^^^^
  File "/home/runner/work/bioversions/bioversions/src/bioversions/sources/__init__.py", line 193, in resolve
    return _resolve_helper_cached(name)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/runner/work/bioversions/bioversions/.tox/update/lib/python3.12/site-packages/cachier/core.py", line 393, in func_wrapper
    return _call(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^
  File "/home/runner/work/bioversions/bioversions/.tox/update/lib/python3.12/site-packages/cachier/core.py", line 332, in _call
    return _calc_entry(core, key, func, args, kwds)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/runner/work/bioversions/bioversions/.tox/update/lib/python3.12/site-packages/cachier/core.py", line 66, in _calc_entry
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
  File "/home/runner/work/bioversions/bioversions/src/bioversions/sources/ensembl.py", line 23, in get
    soup = get_soup(URL)
           ^^^^^^^^^^^^^
  File "/home/runner/work/bioversions/bioversions/.tox/update/lib/python3.12/site-packages/pystow/utils.py", line 1522, in get_soup
    res = requests.get(url, verify=verify, timeout=timeout or 15, headers=headers)
          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/runner/work/bioversions/bioversions/.tox/update/lib/python3.12/site-packages/requests/api.py", line 73, in get
    return request("get", url, params=params, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/runner/work/bioversions/bioversions/.tox/update/lib/python3.12/site-packages/requests/api.py", line 59, in request
    return session.request(method=method, url=url, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/runner/work/bioversions/bioversions/.tox/update/lib/python3.12/site-packages/requests/sessions.py", line 589, in request
    resp = self.send(prep, **send_kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/runner/work/bioversions/bioversions/.tox/update/lib/python3.12/site-packages/requests/sessions.py", line 724, in send
    history = [resp for resp in gen]
                                ^^^
  File "/home/runner/work/bioversions/bioversions/.tox/update/lib/python3.12/site-packages/requests/sessions.py", line 265, in resolve_redirects
    resp = self.send(
           ^^^^^^^^^^
  File "/home/runner/work/bioversions/bioversions/.tox/update/lib/python3.12/site-packages/requests/sessions.py", line 703, in send
    r = adapter.send(request, **kwargs)
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/runner/work/bioversions/bioversions/.tox/update/lib/python3.12/site-packages/requests/adapters.py", line 690, in send
    raise ReadTimeout(e, request=request)
requests.exceptions.ReadTimeout: HTTPSConnectionPool(host='useast.ensembl.org', port=443): Read timed out. (read timeout=15)

```
