# Summary of Errors

- **DisGeNet**
  `failed to resolve DisGeNet`
- **Pathway Commons**
  `issue parsing Pathway Commons: could not find an element matching args=({'class': 'boost'},) and kwargs={}`
- **ChEBI**
  `failed to resolve ChEBI`
- **DrugBank**
  `failed to resolve DrugBank`
- **International Classification of Diseases, 10th Revision**
  `failed to resolve International Classification of Diseases, 10th Revision`
- **International Classification of Diseases, 11th Revision**
  `failed to resolve International Classification of Diseases, 11th Revision`
- **International Classification of Functioning, Disability and Health**
  `failed to resolve International Classification of Functioning, Disability and Health`
- **ITIS**
  `issue parsing ITIS: time data '<!doctype html>\n<html>\n  <head>\n    <meta charset="utf-8">\n    <meta http-equiv="X-UA-Compatible" content="IE=edge">\n    <title>Page Not Found | Puppet Enterprise</title>\n    <meta name="viewport" content="width=device-width, initial-scale=1">\n    <link rel="stylesheet" type="text/css" href="/404/styles/normalize-8b255ea2eb5f2f8ef944c2b15939ad0b.css">\n    <link rel="stylesheet" type="text/css" href="/404/styles/main-42547b4e8ea0b123fcaf9c4c9b012c47.css">\n  </head>\n  <body>\n    <div id="wrap">\n      <div id="identity">\n        <img src="/auth/images/pe-logo-amber.svg" alt="">\n      </div>\n      <div class="not-found-container">\n        <h1>404</h1>\n        <p>Page not found</p>\n        <a href="/">Return to home</a>\n      </div>\n      <div id="puppet">\n        <img src="/auth/images/logo.svg" alt="">\n      </div>\n      <footer>\n      Copyright &copy; 2022 Puppet<span class="sep">|</span> <a href="http://www.puppet.com">www.puppet.com</a>\n      </footer>\n    </div>\n  </body>\n</html>\n' does not match format '%d-%b-%Y'`

## DisGeNet

Using class: `DisGeNetGetter`

```python-traceback
Traceback (most recent call last):
  File "/home/runner/work/bioversions/bioversions/.tox/update/lib/python3.12/site-packages/requests/models.py", line 974, in json
    return complexjson.loads(self.text, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.12.9/x64/lib/python3.12/json/__init__.py", line 346, in loads
    return _default_decoder.decode(s)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.12.9/x64/lib/python3.12/json/decoder.py", line 338, in decode
    obj, end = self.raw_decode(s, idx=_w(s, 0).end())
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.12.9/x64/lib/python3.12/json/decoder.py", line 356, in raw_decode
    raise JSONDecodeError("Expecting value", s, err.value) from None
json.decoder.JSONDecodeError: Expecting value: line 1 column 1 (char 0)

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/home/runner/work/bioversions/bioversions/src/bioversions/sources/__init__.py", line 246, in _iter_versions
    yv = resolve(cls.name)
         ^^^^^^^^^^^^^^^^^
  File "/home/runner/work/bioversions/bioversions/src/bioversions/sources/__init__.py", line 173, in resolve
    return _resolve_helper_cached(name)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/runner/work/bioversions/bioversions/.tox/update/lib/python3.12/site-packages/cachier/core.py", line 258, in func_wrapper
    return _calc_entry(core, key, func, args, kwds)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/runner/work/bioversions/bioversions/.tox/update/lib/python3.12/site-packages/cachier/core.py", line 61, in _calc_entry
    func_res = func(*args, **kwds)
               ^^^^^^^^^^^^^^^^^^^
  File "/home/runner/work/bioversions/bioversions/src/bioversions/sources/__init__.py", line 180, in _resolve_helper_cached
    return _resolve_helper(name)
           ^^^^^^^^^^^^^^^^^^^^^
  File "/home/runner/work/bioversions/bioversions/src/bioversions/sources/__init__.py", line 186, in _resolve_helper
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
  File "/home/runner/work/bioversions/bioversions/src/bioversions/sources/disgenet.py", line 24, in get
    res_json = res.json()
               ^^^^^^^^^^
  File "/home/runner/work/bioversions/bioversions/.tox/update/lib/python3.12/site-packages/requests/models.py", line 978, in json
    raise RequestsJSONDecodeError(e.msg, e.doc, e.pos)
requests.exceptions.JSONDecodeError: Expecting value: line 1 column 1 (char 0)

```

## Pathway Commons

Using class: `PathwayCommonsGetter`

```python-traceback
Traceback (most recent call last):
  File "/home/runner/work/bioversions/bioversions/src/bioversions/sources/__init__.py", line 246, in _iter_versions
    yv = resolve(cls.name)
         ^^^^^^^^^^^^^^^^^
  File "/home/runner/work/bioversions/bioversions/src/bioversions/sources/__init__.py", line 173, in resolve
    return _resolve_helper_cached(name)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/runner/work/bioversions/bioversions/.tox/update/lib/python3.12/site-packages/cachier/core.py", line 258, in func_wrapper
    return _calc_entry(core, key, func, args, kwds)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/runner/work/bioversions/bioversions/.tox/update/lib/python3.12/site-packages/cachier/core.py", line 61, in _calc_entry
    func_res = func(*args, **kwds)
               ^^^^^^^^^^^^^^^^^^^
  File "/home/runner/work/bioversions/bioversions/src/bioversions/sources/__init__.py", line 180, in _resolve_helper_cached
    return _resolve_helper(name)
           ^^^^^^^^^^^^^^^^^^^^^
  File "/home/runner/work/bioversions/bioversions/src/bioversions/sources/__init__.py", line 186, in _resolve_helper
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
  File "/home/runner/work/bioversions/bioversions/src/bioversions/sources/pathwaycommons.py", line 21, in get
    boost = find(soup, {"class": "boost"})
            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/runner/work/bioversions/bioversions/src/bioversions/utils.py", line 71, in find
    raise ValueError(f"could not find an element matching {args=} and {kwargs=}")
ValueError: could not find an element matching args=({'class': 'boost'},) and kwargs={}

```

## ChEBI

Using class: `ChEBIGetter`

```python-traceback
Traceback (most recent call last):
  File "/home/runner/work/bioversions/bioversions/.tox/update/lib/python3.12/site-packages/urllib3/connection.py", line 198, in _new_conn
    sock = connection.create_connection(
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/runner/work/bioversions/bioversions/.tox/update/lib/python3.12/site-packages/urllib3/util/connection.py", line 85, in create_connection
    raise err
  File "/home/runner/work/bioversions/bioversions/.tox/update/lib/python3.12/site-packages/urllib3/util/connection.py", line 73, in create_connection
    sock.connect(sa)
ConnectionRefusedError: [Errno 111] Connection refused

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "/home/runner/work/bioversions/bioversions/.tox/update/lib/python3.12/site-packages/urllib3/connectionpool.py", line 787, in urlopen
    response = self._make_request(
               ^^^^^^^^^^^^^^^^^^^
  File "/home/runner/work/bioversions/bioversions/.tox/update/lib/python3.12/site-packages/urllib3/connectionpool.py", line 493, in _make_request
    conn.request(
  File "/home/runner/work/bioversions/bioversions/.tox/update/lib/python3.12/site-packages/urllib3/connection.py", line 445, in request
    self.endheaders()
  File "/opt/hostedtoolcache/Python/3.12.9/x64/lib/python3.12/http/client.py", line 1333, in endheaders
    self._send_output(message_body, encode_chunked=encode_chunked)
  File "/opt/hostedtoolcache/Python/3.12.9/x64/lib/python3.12/http/client.py", line 1093, in _send_output
    self.send(msg)
  File "/opt/hostedtoolcache/Python/3.12.9/x64/lib/python3.12/http/client.py", line 1037, in send
    self.connect()
  File "/home/runner/work/bioversions/bioversions/.tox/update/lib/python3.12/site-packages/urllib3/connection.py", line 276, in connect
    self.sock = self._new_conn()
                ^^^^^^^^^^^^^^^^
  File "/home/runner/work/bioversions/bioversions/.tox/update/lib/python3.12/site-packages/urllib3/connection.py", line 213, in _new_conn
    raise NewConnectionError(
urllib3.exceptions.NewConnectionError: <urllib3.connection.HTTPConnection object at 0x7ff8337e7620>: Failed to establish a new connection: [Errno 111] Connection refused

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "/home/runner/work/bioversions/bioversions/.tox/update/lib/python3.12/site-packages/requests/adapters.py", line 667, in send
    resp = conn.urlopen(
           ^^^^^^^^^^^^^
  File "/home/runner/work/bioversions/bioversions/.tox/update/lib/python3.12/site-packages/urllib3/connectionpool.py", line 841, in urlopen
    retries = retries.increment(
              ^^^^^^^^^^^^^^^^^^
  File "/home/runner/work/bioversions/bioversions/.tox/update/lib/python3.12/site-packages/urllib3/util/retry.py", line 519, in increment
    raise MaxRetryError(_pool, url, reason) from reason  # type: ignore[arg-type]
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
urllib3.exceptions.MaxRetryError: HTTPConnectionPool(host='ftp.ebi.ac.uk', port=80): Max retries exceeded with url: /pub/databases/chebi/ontology/chebi.obo (Caused by NewConnectionError('<urllib3.connection.HTTPConnection object at 0x7ff8337e7620>: Failed to establish a new connection: [Errno 111] Connection refused'))

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/home/runner/work/bioversions/bioversions/src/bioversions/sources/__init__.py", line 246, in _iter_versions
    yv = resolve(cls.name)
         ^^^^^^^^^^^^^^^^^
  File "/home/runner/work/bioversions/bioversions/src/bioversions/sources/__init__.py", line 173, in resolve
    return _resolve_helper_cached(name)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/runner/work/bioversions/bioversions/.tox/update/lib/python3.12/site-packages/cachier/core.py", line 258, in func_wrapper
    return _calc_entry(core, key, func, args, kwds)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/runner/work/bioversions/bioversions/.tox/update/lib/python3.12/site-packages/cachier/core.py", line 61, in _calc_entry
    func_res = func(*args, **kwds)
               ^^^^^^^^^^^^^^^^^^^
  File "/home/runner/work/bioversions/bioversions/src/bioversions/sources/__init__.py", line 180, in _resolve_helper_cached
    return _resolve_helper(name)
           ^^^^^^^^^^^^^^^^^^^^^
  File "/home/runner/work/bioversions/bioversions/src/bioversions/sources/__init__.py", line 186, in _resolve_helper
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
  File "/home/runner/work/bioversions/bioversions/src/bioversions/utils.py", line 292, in get
    return self.process(get_obo_version(url))
                        ^^^^^^^^^^^^^^^^^^^^
  File "/home/runner/work/bioversions/bioversions/src/bioversions/utils.py", line 263, in get_obo_version
    with requests.get(url, stream=True, timeout=60) as res:
         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
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
  File "/home/runner/work/bioversions/bioversions/.tox/update/lib/python3.12/site-packages/requests/adapters.py", line 700, in send
    raise ConnectionError(e, request=request)
requests.exceptions.ConnectionError: HTTPConnectionPool(host='ftp.ebi.ac.uk', port=80): Max retries exceeded with url: /pub/databases/chebi/ontology/chebi.obo (Caused by NewConnectionError('<urllib3.connection.HTTPConnection object at 0x7ff8337e7620>: Failed to establish a new connection: [Errno 111] Connection refused'))

```

## DrugBank

Using class: `DrugBankGetter`

```python-traceback
Traceback (most recent call last):
  File "/home/runner/work/bioversions/bioversions/src/bioversions/sources/__init__.py", line 246, in _iter_versions
    yv = resolve(cls.name)
         ^^^^^^^^^^^^^^^^^
  File "/home/runner/work/bioversions/bioversions/src/bioversions/sources/__init__.py", line 173, in resolve
    return _resolve_helper_cached(name)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/runner/work/bioversions/bioversions/.tox/update/lib/python3.12/site-packages/cachier/core.py", line 258, in func_wrapper
    return _calc_entry(core, key, func, args, kwds)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/runner/work/bioversions/bioversions/.tox/update/lib/python3.12/site-packages/cachier/core.py", line 61, in _calc_entry
    func_res = func(*args, **kwds)
               ^^^^^^^^^^^^^^^^^^^
  File "/home/runner/work/bioversions/bioversions/src/bioversions/sources/__init__.py", line 180, in _resolve_helper_cached
    return _resolve_helper(name)
           ^^^^^^^^^^^^^^^^^^^^^
  File "/home/runner/work/bioversions/bioversions/src/bioversions/sources/__init__.py", line 186, in _resolve_helper
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
  File "/home/runner/work/bioversions/bioversions/src/bioversions/sources/drugbank.py", line 28, in get
    res.raise_for_status()
  File "/home/runner/work/bioversions/bioversions/.tox/update/lib/python3.12/site-packages/requests/models.py", line 1024, in raise_for_status
    raise HTTPError(http_error_msg, response=self)
requests.exceptions.HTTPError: 403 Client Error: Forbidden for url: https://go.drugbank.com/releases.json

```

## International Classification of Diseases, 10th Revision

Using class: `ICD10Getter`

```python-traceback
Traceback (most recent call last):
  File "/home/runner/work/bioversions/bioversions/.tox/update/lib/python3.12/site-packages/urllib3/connectionpool.py", line 464, in _make_request
    self._validate_conn(conn)
  File "/home/runner/work/bioversions/bioversions/.tox/update/lib/python3.12/site-packages/urllib3/connectionpool.py", line 1093, in _validate_conn
    conn.connect()
  File "/home/runner/work/bioversions/bioversions/.tox/update/lib/python3.12/site-packages/urllib3/connection.py", line 741, in connect
    sock_and_verified = _ssl_wrap_socket_and_match_hostname(
                        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/runner/work/bioversions/bioversions/.tox/update/lib/python3.12/site-packages/urllib3/connection.py", line 920, in _ssl_wrap_socket_and_match_hostname
    ssl_sock = ssl_wrap_socket(
               ^^^^^^^^^^^^^^^^
  File "/home/runner/work/bioversions/bioversions/.tox/update/lib/python3.12/site-packages/urllib3/util/ssl_.py", line 480, in ssl_wrap_socket
    ssl_sock = _ssl_wrap_socket_impl(sock, context, tls_in_tls, server_hostname)
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/runner/work/bioversions/bioversions/.tox/update/lib/python3.12/site-packages/urllib3/util/ssl_.py", line 524, in _ssl_wrap_socket_impl
    return ssl_context.wrap_socket(sock, server_hostname=server_hostname)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.12.9/x64/lib/python3.12/ssl.py", line 455, in wrap_socket
    return self.sslsocket_class._create(
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.12.9/x64/lib/python3.12/ssl.py", line 1041, in _create
    self.do_handshake()
  File "/opt/hostedtoolcache/Python/3.12.9/x64/lib/python3.12/ssl.py", line 1319, in do_handshake
    self._sslobj.do_handshake()
ssl.SSLCertVerificationError: [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: unable to get local issuer certificate (_ssl.c:1010)

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/home/runner/work/bioversions/bioversions/.tox/update/lib/python3.12/site-packages/urllib3/connectionpool.py", line 787, in urlopen
    response = self._make_request(
               ^^^^^^^^^^^^^^^^^^^
  File "/home/runner/work/bioversions/bioversions/.tox/update/lib/python3.12/site-packages/urllib3/connectionpool.py", line 488, in _make_request
    raise new_e
urllib3.exceptions.SSLError: [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: unable to get local issuer certificate (_ssl.c:1010)

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "/home/runner/work/bioversions/bioversions/.tox/update/lib/python3.12/site-packages/requests/adapters.py", line 667, in send
    resp = conn.urlopen(
           ^^^^^^^^^^^^^
  File "/home/runner/work/bioversions/bioversions/.tox/update/lib/python3.12/site-packages/urllib3/connectionpool.py", line 841, in urlopen
    retries = retries.increment(
              ^^^^^^^^^^^^^^^^^^
  File "/home/runner/work/bioversions/bioversions/.tox/update/lib/python3.12/site-packages/urllib3/util/retry.py", line 519, in increment
    raise MaxRetryError(_pool, url, reason) from reason  # type: ignore[arg-type]
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
urllib3.exceptions.MaxRetryError: HTTPSConnectionPool(host='icd.who.int', port=443): Max retries exceeded with url: /browse10/ (Caused by SSLError(SSLCertVerificationError(1, '[SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: unable to get local issuer certificate (_ssl.c:1010)')))

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/home/runner/work/bioversions/bioversions/src/bioversions/sources/__init__.py", line 246, in _iter_versions
    yv = resolve(cls.name)
         ^^^^^^^^^^^^^^^^^
  File "/home/runner/work/bioversions/bioversions/src/bioversions/sources/__init__.py", line 173, in resolve
    return _resolve_helper_cached(name)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/runner/work/bioversions/bioversions/.tox/update/lib/python3.12/site-packages/cachier/core.py", line 258, in func_wrapper
    return _calc_entry(core, key, func, args, kwds)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/runner/work/bioversions/bioversions/.tox/update/lib/python3.12/site-packages/cachier/core.py", line 61, in _calc_entry
    func_res = func(*args, **kwds)
               ^^^^^^^^^^^^^^^^^^^
  File "/home/runner/work/bioversions/bioversions/src/bioversions/sources/__init__.py", line 180, in _resolve_helper_cached
    return _resolve_helper(name)
           ^^^^^^^^^^^^^^^^^^^^^
  File "/home/runner/work/bioversions/bioversions/src/bioversions/sources/__init__.py", line 186, in _resolve_helper
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
  File "/home/runner/work/bioversions/bioversions/src/bioversions/sources/icd10.py", line 24, in get
    response = requests.get(URL, allow_redirects=True, timeout=15)
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
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
  File "/home/runner/work/bioversions/bioversions/.tox/update/lib/python3.12/site-packages/requests/adapters.py", line 698, in send
    raise SSLError(e, request=request)
requests.exceptions.SSLError: HTTPSConnectionPool(host='icd.who.int', port=443): Max retries exceeded with url: /browse10/ (Caused by SSLError(SSLCertVerificationError(1, '[SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: unable to get local issuer certificate (_ssl.c:1010)')))

```

## International Classification of Diseases, 11th Revision

Using class: `ICD11Getter`

```python-traceback
Traceback (most recent call last):
  File "/home/runner/work/bioversions/bioversions/.tox/update/lib/python3.12/site-packages/urllib3/connectionpool.py", line 464, in _make_request
    self._validate_conn(conn)
  File "/home/runner/work/bioversions/bioversions/.tox/update/lib/python3.12/site-packages/urllib3/connectionpool.py", line 1093, in _validate_conn
    conn.connect()
  File "/home/runner/work/bioversions/bioversions/.tox/update/lib/python3.12/site-packages/urllib3/connection.py", line 741, in connect
    sock_and_verified = _ssl_wrap_socket_and_match_hostname(
                        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/runner/work/bioversions/bioversions/.tox/update/lib/python3.12/site-packages/urllib3/connection.py", line 920, in _ssl_wrap_socket_and_match_hostname
    ssl_sock = ssl_wrap_socket(
               ^^^^^^^^^^^^^^^^
  File "/home/runner/work/bioversions/bioversions/.tox/update/lib/python3.12/site-packages/urllib3/util/ssl_.py", line 480, in ssl_wrap_socket
    ssl_sock = _ssl_wrap_socket_impl(sock, context, tls_in_tls, server_hostname)
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/runner/work/bioversions/bioversions/.tox/update/lib/python3.12/site-packages/urllib3/util/ssl_.py", line 524, in _ssl_wrap_socket_impl
    return ssl_context.wrap_socket(sock, server_hostname=server_hostname)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.12.9/x64/lib/python3.12/ssl.py", line 455, in wrap_socket
    return self.sslsocket_class._create(
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.12.9/x64/lib/python3.12/ssl.py", line 1041, in _create
    self.do_handshake()
  File "/opt/hostedtoolcache/Python/3.12.9/x64/lib/python3.12/ssl.py", line 1319, in do_handshake
    self._sslobj.do_handshake()
ssl.SSLCertVerificationError: [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: unable to get local issuer certificate (_ssl.c:1010)

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/home/runner/work/bioversions/bioversions/.tox/update/lib/python3.12/site-packages/urllib3/connectionpool.py", line 787, in urlopen
    response = self._make_request(
               ^^^^^^^^^^^^^^^^^^^
  File "/home/runner/work/bioversions/bioversions/.tox/update/lib/python3.12/site-packages/urllib3/connectionpool.py", line 488, in _make_request
    raise new_e
urllib3.exceptions.SSLError: [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: unable to get local issuer certificate (_ssl.c:1010)

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "/home/runner/work/bioversions/bioversions/.tox/update/lib/python3.12/site-packages/requests/adapters.py", line 667, in send
    resp = conn.urlopen(
           ^^^^^^^^^^^^^
  File "/home/runner/work/bioversions/bioversions/.tox/update/lib/python3.12/site-packages/urllib3/connectionpool.py", line 841, in urlopen
    retries = retries.increment(
              ^^^^^^^^^^^^^^^^^^
  File "/home/runner/work/bioversions/bioversions/.tox/update/lib/python3.12/site-packages/urllib3/util/retry.py", line 519, in increment
    raise MaxRetryError(_pool, url, reason) from reason  # type: ignore[arg-type]
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
urllib3.exceptions.MaxRetryError: HTTPSConnectionPool(host='icd.who.int', port=443): Max retries exceeded with url: /browse/latest-release/mms/en (Caused by SSLError(SSLCertVerificationError(1, '[SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: unable to get local issuer certificate (_ssl.c:1010)')))

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/home/runner/work/bioversions/bioversions/src/bioversions/sources/__init__.py", line 246, in _iter_versions
    yv = resolve(cls.name)
         ^^^^^^^^^^^^^^^^^
  File "/home/runner/work/bioversions/bioversions/src/bioversions/sources/__init__.py", line 173, in resolve
    return _resolve_helper_cached(name)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/runner/work/bioversions/bioversions/.tox/update/lib/python3.12/site-packages/cachier/core.py", line 258, in func_wrapper
    return _calc_entry(core, key, func, args, kwds)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/runner/work/bioversions/bioversions/.tox/update/lib/python3.12/site-packages/cachier/core.py", line 61, in _calc_entry
    func_res = func(*args, **kwds)
               ^^^^^^^^^^^^^^^^^^^
  File "/home/runner/work/bioversions/bioversions/src/bioversions/sources/__init__.py", line 180, in _resolve_helper_cached
    return _resolve_helper(name)
           ^^^^^^^^^^^^^^^^^^^^^
  File "/home/runner/work/bioversions/bioversions/src/bioversions/sources/__init__.py", line 186, in _resolve_helper
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
  File "/home/runner/work/bioversions/bioversions/src/bioversions/sources/icd11.py", line 24, in get
    response = requests.get(URL, allow_redirects=True, timeout=15)
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
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
  File "/home/runner/work/bioversions/bioversions/.tox/update/lib/python3.12/site-packages/requests/adapters.py", line 698, in send
    raise SSLError(e, request=request)
requests.exceptions.SSLError: HTTPSConnectionPool(host='icd.who.int', port=443): Max retries exceeded with url: /browse/latest-release/mms/en (Caused by SSLError(SSLCertVerificationError(1, '[SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: unable to get local issuer certificate (_ssl.c:1010)')))

```

## International Classification of Functioning, Disability and Health

Using class: `ICFGetter`

```python-traceback
Traceback (most recent call last):
  File "/home/runner/work/bioversions/bioversions/.tox/update/lib/python3.12/site-packages/urllib3/connectionpool.py", line 464, in _make_request
    self._validate_conn(conn)
  File "/home/runner/work/bioversions/bioversions/.tox/update/lib/python3.12/site-packages/urllib3/connectionpool.py", line 1093, in _validate_conn
    conn.connect()
  File "/home/runner/work/bioversions/bioversions/.tox/update/lib/python3.12/site-packages/urllib3/connection.py", line 741, in connect
    sock_and_verified = _ssl_wrap_socket_and_match_hostname(
                        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/runner/work/bioversions/bioversions/.tox/update/lib/python3.12/site-packages/urllib3/connection.py", line 920, in _ssl_wrap_socket_and_match_hostname
    ssl_sock = ssl_wrap_socket(
               ^^^^^^^^^^^^^^^^
  File "/home/runner/work/bioversions/bioversions/.tox/update/lib/python3.12/site-packages/urllib3/util/ssl_.py", line 480, in ssl_wrap_socket
    ssl_sock = _ssl_wrap_socket_impl(sock, context, tls_in_tls, server_hostname)
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/runner/work/bioversions/bioversions/.tox/update/lib/python3.12/site-packages/urllib3/util/ssl_.py", line 524, in _ssl_wrap_socket_impl
    return ssl_context.wrap_socket(sock, server_hostname=server_hostname)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.12.9/x64/lib/python3.12/ssl.py", line 455, in wrap_socket
    return self.sslsocket_class._create(
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.12.9/x64/lib/python3.12/ssl.py", line 1041, in _create
    self.do_handshake()
  File "/opt/hostedtoolcache/Python/3.12.9/x64/lib/python3.12/ssl.py", line 1319, in do_handshake
    self._sslobj.do_handshake()
ssl.SSLCertVerificationError: [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: unable to get local issuer certificate (_ssl.c:1010)

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/home/runner/work/bioversions/bioversions/.tox/update/lib/python3.12/site-packages/urllib3/connectionpool.py", line 787, in urlopen
    response = self._make_request(
               ^^^^^^^^^^^^^^^^^^^
  File "/home/runner/work/bioversions/bioversions/.tox/update/lib/python3.12/site-packages/urllib3/connectionpool.py", line 488, in _make_request
    raise new_e
urllib3.exceptions.SSLError: [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: unable to get local issuer certificate (_ssl.c:1010)

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "/home/runner/work/bioversions/bioversions/.tox/update/lib/python3.12/site-packages/requests/adapters.py", line 667, in send
    resp = conn.urlopen(
           ^^^^^^^^^^^^^
  File "/home/runner/work/bioversions/bioversions/.tox/update/lib/python3.12/site-packages/urllib3/connectionpool.py", line 841, in urlopen
    retries = retries.increment(
              ^^^^^^^^^^^^^^^^^^
  File "/home/runner/work/bioversions/bioversions/.tox/update/lib/python3.12/site-packages/urllib3/util/retry.py", line 519, in increment
    raise MaxRetryError(_pool, url, reason) from reason  # type: ignore[arg-type]
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
urllib3.exceptions.MaxRetryError: HTTPSConnectionPool(host='icd.who.int', port=443): Max retries exceeded with url: /browse/latest-release/icf/en (Caused by SSLError(SSLCertVerificationError(1, '[SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: unable to get local issuer certificate (_ssl.c:1010)')))

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/home/runner/work/bioversions/bioversions/src/bioversions/sources/__init__.py", line 246, in _iter_versions
    yv = resolve(cls.name)
         ^^^^^^^^^^^^^^^^^
  File "/home/runner/work/bioversions/bioversions/src/bioversions/sources/__init__.py", line 173, in resolve
    return _resolve_helper_cached(name)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/runner/work/bioversions/bioversions/.tox/update/lib/python3.12/site-packages/cachier/core.py", line 258, in func_wrapper
    return _calc_entry(core, key, func, args, kwds)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/runner/work/bioversions/bioversions/.tox/update/lib/python3.12/site-packages/cachier/core.py", line 61, in _calc_entry
    func_res = func(*args, **kwds)
               ^^^^^^^^^^^^^^^^^^^
  File "/home/runner/work/bioversions/bioversions/src/bioversions/sources/__init__.py", line 180, in _resolve_helper_cached
    return _resolve_helper(name)
           ^^^^^^^^^^^^^^^^^^^^^
  File "/home/runner/work/bioversions/bioversions/src/bioversions/sources/__init__.py", line 186, in _resolve_helper
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
  File "/home/runner/work/bioversions/bioversions/src/bioversions/sources/icf.py", line 24, in get
    response = requests.get(URL, allow_redirects=True, timeout=15)
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
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
  File "/home/runner/work/bioversions/bioversions/.tox/update/lib/python3.12/site-packages/requests/adapters.py", line 698, in send
    raise SSLError(e, request=request)
requests.exceptions.SSLError: HTTPSConnectionPool(host='icd.who.int', port=443): Max retries exceeded with url: /browse/latest-release/icf/en (Caused by SSLError(SSLCertVerificationError(1, '[SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: unable to get local issuer certificate (_ssl.c:1010)')))

```

## ITIS

Using class: `ITISGetter`

```python-traceback
Traceback (most recent call last):
  File "/home/runner/work/bioversions/bioversions/src/bioversions/sources/__init__.py", line 246, in _iter_versions
    yv = resolve(cls.name)
         ^^^^^^^^^^^^^^^^^
  File "/home/runner/work/bioversions/bioversions/src/bioversions/sources/__init__.py", line 173, in resolve
    return _resolve_helper_cached(name)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/runner/work/bioversions/bioversions/.tox/update/lib/python3.12/site-packages/cachier/core.py", line 258, in func_wrapper
    return _calc_entry(core, key, func, args, kwds)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/runner/work/bioversions/bioversions/.tox/update/lib/python3.12/site-packages/cachier/core.py", line 61, in _calc_entry
    func_res = func(*args, **kwds)
               ^^^^^^^^^^^^^^^^^^^
  File "/home/runner/work/bioversions/bioversions/src/bioversions/sources/__init__.py", line 180, in _resolve_helper_cached
    return _resolve_helper(name)
           ^^^^^^^^^^^^^^^^^^^^^
  File "/home/runner/work/bioversions/bioversions/src/bioversions/sources/__init__.py", line 186, in _resolve_helper
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
  File "/home/runner/work/bioversions/bioversions/src/bioversions/sources/itis.py", line 26, in get
    return datetime.datetime.strptime(res, "%d-%b-%Y")
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.12.9/x64/lib/python3.12/_strptime.py", line 653, in _strptime_datetime
    tt, fraction, gmtoff_fraction = _strptime(data_string, format)
                                    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/opt/hostedtoolcache/Python/3.12.9/x64/lib/python3.12/_strptime.py", line 432, in _strptime
    raise ValueError("time data %r does not match format %r" %
ValueError: time data '<!doctype html>\n<html>\n  <head>\n    <meta charset="utf-8">\n    <meta http-equiv="X-UA-Compatible" content="IE=edge">\n    <title>Page Not Found | Puppet Enterprise</title>\n    <meta name="viewport" content="width=device-width, initial-scale=1">\n    <link rel="stylesheet" type="text/css" href="/404/styles/normalize-8b255ea2eb5f2f8ef944c2b15939ad0b.css">\n    <link rel="stylesheet" type="text/css" href="/404/styles/main-42547b4e8ea0b123fcaf9c4c9b012c47.css">\n  </head>\n  <body>\n    <div id="wrap">\n      <div id="identity">\n        <img src="/auth/images/pe-logo-amber.svg" alt="">\n      </div>\n      <div class="not-found-container">\n        <h1>404</h1>\n        <p>Page not found</p>\n        <a href="/">Return to home</a>\n      </div>\n      <div id="puppet">\n        <img src="/auth/images/logo.svg" alt="">\n      </div>\n      <footer>\n      Copyright &copy; 2022 Puppet<span class="sep">|</span> <a href="http://www.puppet.com">www.puppet.com</a>\n      </footer>\n    </div>\n  </body>\n</html>\n' does not match format '%d-%b-%Y'

```
