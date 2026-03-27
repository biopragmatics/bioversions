# Summary of Errors

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

- **Protein Ontology**
  `[pr] failed to resolve: HTTPSConnectionPool(host='proconsortium.org', port=443): Read timed out. (read timeout=15)`

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

## Protein Ontology

Using class: `PRGetter`

```python-traceback
Traceback (most recent call last):
  File "/home/runner/work/bioversions/bioversions/.tox/update/lib/python3.12/site-packages/urllib3/connectionpool.py", line 464, in _make_request
    self._validate_conn(conn)
  File "/home/runner/work/bioversions/bioversions/.tox/update/lib/python3.12/site-packages/urllib3/connectionpool.py", line 1093, in _validate_conn
    conn.connect()
  File "/home/runner/work/bioversions/bioversions/.tox/update/lib/python3.12/site-packages/urllib3/connection.py", line 796, in connect
    sock_and_verified = _ssl_wrap_socket_and_match_hostname(
                        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/runner/work/bioversions/bioversions/.tox/update/lib/python3.12/site-packages/urllib3/connection.py", line 975, in _ssl_wrap_socket_and_match_hostname
    ssl_sock = ssl_wrap_socket(
               ^^^^^^^^^^^^^^^^
  File "/home/runner/work/bioversions/bioversions/.tox/update/lib/python3.12/site-packages/urllib3/util/ssl_.py", line 483, in ssl_wrap_socket
    ssl_sock = _ssl_wrap_socket_impl(sock, context, tls_in_tls, server_hostname)
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/runner/work/bioversions/bioversions/.tox/update/lib/python3.12/site-packages/urllib3/util/ssl_.py", line 527, in _ssl_wrap_socket_impl
    return ssl_context.wrap_socket(sock, server_hostname=server_hostname)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.12.13/x64/lib/python3.12/ssl.py", line 455, in wrap_socket
    return self.sslsocket_class._create(
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.12.13/x64/lib/python3.12/ssl.py", line 1041, in _create
    self.do_handshake()
  File "/opt/hostedtoolcache/Python/3.12.13/x64/lib/python3.12/ssl.py", line 1319, in do_handshake
    self._sslobj.do_handshake()
TimeoutError: _ssl.c:993: The handshake operation timed out

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "/home/runner/work/bioversions/bioversions/.tox/update/lib/python3.12/site-packages/requests/adapters.py", line 645, in send
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
  File "/home/runner/work/bioversions/bioversions/.tox/update/lib/python3.12/site-packages/urllib3/connectionpool.py", line 488, in _make_request
    raise new_e
  File "/home/runner/work/bioversions/bioversions/.tox/update/lib/python3.12/site-packages/urllib3/connectionpool.py", line 466, in _make_request
    self._raise_timeout(err=e, url=url, timeout_value=conn.timeout)
  File "/home/runner/work/bioversions/bioversions/.tox/update/lib/python3.12/site-packages/urllib3/connectionpool.py", line 367, in _raise_timeout
    raise ReadTimeoutError(
urllib3.exceptions.ReadTimeoutError: HTTPSConnectionPool(host='proconsortium.org', port=443): Read timed out. (read timeout=15)

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
  File "/home/runner/work/bioversions/bioversions/src/bioversions/sources/pr.py", line 23, in get
    soup = get_soup(URL)
           ^^^^^^^^^^^^^
  File "/home/runner/work/bioversions/bioversions/.tox/update/lib/python3.12/site-packages/pystow/utils/__init__.py", line 863, in get_soup
    res = requests.get(url, verify=verify, timeout=timeout or 15, headers=headers)
          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/runner/work/bioversions/bioversions/.tox/update/lib/python3.12/site-packages/requests/api.py", line 73, in get
    return request("get", url, params=params, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/runner/work/bioversions/bioversions/.tox/update/lib/python3.12/site-packages/requests/api.py", line 59, in request
    return session.request(method=method, url=url, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/runner/work/bioversions/bioversions/.tox/update/lib/python3.12/site-packages/requests/sessions.py", line 592, in request
    resp = self.send(prep, **send_kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/runner/work/bioversions/bioversions/.tox/update/lib/python3.12/site-packages/requests/sessions.py", line 706, in send
    r = adapter.send(request, **kwargs)
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/runner/work/bioversions/bioversions/.tox/update/lib/python3.12/site-packages/requests/adapters.py", line 691, in send
    raise ReadTimeout(e, request=request)
requests.exceptions.ReadTimeout: HTTPSConnectionPool(host='proconsortium.org', port=443): Read timed out. (read timeout=15)

```
