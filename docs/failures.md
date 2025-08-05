# Summary of Errors

- **BiGG**
  `[BiGG] failed to resolve: HTTPConnectionPool(host='bigg.ucsd.edu', port=80): Read timed out. (read timeout=15)`
- **Online Mendelian Inheritance in Man**
  `[Online Mendelian Inheritance in Man] issue parsing: time data 'Augu 1, 2025' does not match format '%B %d, %Y'`

## BiGG

Using class: `BiGGGetter`

```python-traceback
Traceback (most recent call last):
  File "/home/runner/work/bioversions/bioversions/.tox/update/lib/python3.12/site-packages/urllib3/connectionpool.py", line 534, in _make_request
    response = conn.getresponse()
               ^^^^^^^^^^^^^^^^^^
  File "/home/runner/work/bioversions/bioversions/.tox/update/lib/python3.12/site-packages/urllib3/connection.py", line 565, in getresponse
    httplib_response = super().getresponse()
                       ^^^^^^^^^^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.12.11/x64/lib/python3.12/http/client.py", line 1430, in getresponse
    response.begin()
  File "/opt/hostedtoolcache/Python/3.12.11/x64/lib/python3.12/http/client.py", line 331, in begin
    version, status, reason = self._read_status()
                              ^^^^^^^^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.12.11/x64/lib/python3.12/http/client.py", line 292, in _read_status
    line = str(self.fp.readline(_MAXLINE + 1), "iso-8859-1")
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.12.11/x64/lib/python3.12/socket.py", line 720, in readinto
    return self._sock.recv_into(b)
           ^^^^^^^^^^^^^^^^^^^^^^^
TimeoutError: timed out

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "/home/runner/work/bioversions/bioversions/.tox/update/lib/python3.12/site-packages/requests/adapters.py", line 667, in send
    resp = conn.urlopen(
           ^^^^^^^^^^^^^
  File "/home/runner/work/bioversions/bioversions/.tox/update/lib/python3.12/site-packages/urllib3/connectionpool.py", line 841, in urlopen
    retries = retries.increment(
              ^^^^^^^^^^^^^^^^^^
  File "/home/runner/work/bioversions/bioversions/.tox/update/lib/python3.12/site-packages/urllib3/util/retry.py", line 474, in increment
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
urllib3.exceptions.ReadTimeoutError: HTTPConnectionPool(host='bigg.ucsd.edu', port=80): Read timed out. (read timeout=15)

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/home/runner/work/bioversions/bioversions/src/bioversions/sources/__init__.py", line 318, in iter_versions
    yv = resolve(cls.name)
         ^^^^^^^^^^^^^^^^^
  File "/home/runner/work/bioversions/bioversions/src/bioversions/sources/__init__.py", line 239, in resolve
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
  File "/home/runner/work/bioversions/bioversions/src/bioversions/sources/__init__.py", line 246, in _resolve_helper_cached
    return _resolve_helper(name)
           ^^^^^^^^^^^^^^^^^^^^^
  File "/home/runner/work/bioversions/bioversions/src/bioversions/sources/__init__.py", line 257, in _resolve_helper
    return getter.resolve()
           ^^^^^^^^^^^^^^^^
  File "/home/runner/work/bioversions/bioversions/src/bioversions/utils.py", line 224, in resolve
    version=cls.version,
            ^^^^^^^^^^^
  File "/home/runner/work/bioversions/bioversions/src/bioversions/utils.py", line 102, in version
    if isinstance(cls._cache_prop, str):
                  ^^^^^^^^^^^^^^^
  File "/home/runner/work/bioversions/bioversions/src/bioversions/utils.py", line 96, in _cache_prop
    cls._cache = cls().get()
                 ^^^^^^^^^^^
  File "/home/runner/work/bioversions/bioversions/src/bioversions/sources/bigg.py", line 24, in get
    res = requests.get(URL, timeout=15).json()
          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
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
  File "/home/runner/work/bioversions/bioversions/.tox/update/lib/python3.12/site-packages/requests/adapters.py", line 713, in send
    raise ReadTimeout(e, request=request)
requests.exceptions.ReadTimeout: HTTPConnectionPool(host='bigg.ucsd.edu', port=80): Read timed out. (read timeout=15)

```

## Online Mendelian Inheritance in Man

Using class: `OMIMGetter`

```python-traceback
Traceback (most recent call last):
  File "/home/runner/work/bioversions/bioversions/src/bioversions/sources/__init__.py", line 318, in iter_versions
    yv = resolve(cls.name)
         ^^^^^^^^^^^^^^^^^
  File "/home/runner/work/bioversions/bioversions/src/bioversions/sources/__init__.py", line 239, in resolve
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
  File "/home/runner/work/bioversions/bioversions/src/bioversions/sources/__init__.py", line 246, in _resolve_helper_cached
    return _resolve_helper(name)
           ^^^^^^^^^^^^^^^^^^^^^
  File "/home/runner/work/bioversions/bioversions/src/bioversions/sources/__init__.py", line 257, in _resolve_helper
    return getter.resolve()
           ^^^^^^^^^^^^^^^^
  File "/home/runner/work/bioversions/bioversions/src/bioversions/utils.py", line 224, in resolve
    version=cls.version,
            ^^^^^^^^^^^
  File "/home/runner/work/bioversions/bioversions/src/bioversions/utils.py", line 102, in version
    if isinstance(cls._cache_prop, str):
                  ^^^^^^^^^^^^^^^
  File "/home/runner/work/bioversions/bioversions/src/bioversions/utils.py", line 96, in _cache_prop
    cls._cache = cls().get()
                 ^^^^^^^^^^^
  File "/home/runner/work/bioversions/bioversions/src/bioversions/sources/omim.py", line 28, in get
    return datetime.datetime.strptime(rv, "%B %d, %Y")
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.12.11/x64/lib/python3.12/_strptime.py", line 653, in _strptime_datetime
    tt, fraction, gmtoff_fraction = _strptime(data_string, format)
                                    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.12.11/x64/lib/python3.12/_strptime.py", line 432, in _strptime
    raise ValueError("time data %r does not match format %r" %
ValueError: time data 'Augu 1, 2025' does not match format '%B %d, %Y'

```
