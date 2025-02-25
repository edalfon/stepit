# CHANGELOG


## v0.5.1 (2025-02-25)

### Bug Fixes

- Update uv.lock
  ([`b70e3c2`](https://github.com/edalfon/stepit/commit/b70e3c20bf4d07fd874ff320741f6b1423265cba))

### Build System

- --set-upstream origin in release-yml
  ([`ac4bc90`](https://github.com/edalfon/stepit/commit/ac4bc900bfddd5bcf526e79cf1ff193df6ac0d4d))


## v0.5.0 (2025-02-25)

### Bug Fixes

- Don't use composite hash but both args and source hash
  ([`c286d82`](https://github.com/edalfon/stepit/commit/c286d82d795c5f5236f338efa657ea88548f8867))

### Build System

- Fix release.yml
  ([`ff6ae0b`](https://github.com/edalfon/stepit/commit/ff6ae0b090311e90e3db3c856df3bad9330a24a4))

- Update uv.lock after semantic release, by commiting the updated file
  ([`8dde9f8`](https://github.com/edalfon/stepit/commit/8dde9f88ceaa6fda5138469977726c5c52829412))

### Features

- Use it's own custom link to current cache file, instead of symlink
  ([`575c4a1`](https://github.com/edalfon/stepit/commit/575c4a1630f8b04cc0a75e7d6a659ccb1b0fcc03))

### Refactoring

- Hash calculation fns
  ([`b162872`](https://github.com/edalfon/stepit/commit/b1628724238e0aba91100bc5d6a1a74823d48bfa))

### Testing

- Add a few assert messages
  ([`f064929`](https://github.com/edalfon/stepit/commit/f0649292d773bac8e9c12e1aa8053d16351c68f8))


## v0.4.0 (2025-02-24)

### Features

- Add timestamp to log messages (info level)
  ([`6198622`](https://github.com/edalfon/stepit/commit/6198622163368e590c2a5fd41c2de0da9a355e02))


## v0.3.1 (2025-02-17)

### Bug Fixes

- No custom repository-url needed for pypi
  ([`37475a8`](https://github.com/edalfon/stepit/commit/37475a86a57295d0abd4c0a7114cb9233b2aa464))


## v0.3.0 (2025-02-17)

### Features

- Proof of concept, yet, ready for pypi
  ([`79014f1`](https://github.com/edalfon/stepit/commit/79014f111479644bfda712f9cda5c8dd1e64683c))


## v0.2.0 (2025-02-17)

### Bug Fixes

- Barebones
  ([`7e809e2`](https://github.com/edalfon/stepit/commit/7e809e255586bc263afda93044e3b83993c8185e))

- Check symlink explicitly
  ([`ba32c58`](https://github.com/edalfon/stepit/commit/ba32c58970c40448ee5f2aee20b0a2bba91ac150))

- Closer look
  ([`456695d`](https://github.com/edalfon/stepit/commit/456695d98401b977e5a6b4f3eeade73c2903ff89))

- Do not create symlink, just copy the file
  ([`b22095c`](https://github.com/edalfon/stepit/commit/b22095c9826a500698544479c68f7446b2277d33))

- Just print it, 'cause logger level debug has already too much info
  ([`ac971f0`](https://github.com/edalfon/stepit/commit/ac971f01de2858d4ba5ce138ab9c90d9022f413e))

- Minimum tests
  ([`cf577ea`](https://github.com/edalfon/stepit/commit/cf577eaeffc081f591d785d01c0d8837b7a1f923))

- Retore tests and in default deserialize, consider there might be symlinks
  ([`10976a8`](https://github.com/edalfon/stepit/commit/10976a856c50a8217a623670127381c748e1cb92))

- Use os.readlink, when it is a symlink
  ([`d344f87`](https://github.com/edalfon/stepit/commit/d344f8799333fe1fbf145f7ed68386cadac061b6))

### Features

- Add debug info before reading file
  ([`9f32f53`](https://github.com/edalfon/stepit/commit/9f32f5336cf8d037a3e53e9e8fb11c6fc5594f70))


## v0.1.5 (2025-02-17)

### Bug Fixes

- Put tests back on
  ([`e5bddfc`](https://github.com/edalfon/stepit/commit/e5bddfc00a4826f8e438589f31d38fd4e0438d5d))


## v0.1.4 (2025-02-17)

### Bug Fixes

- No way
  ([`d4180b1`](https://github.com/edalfon/stepit/commit/d4180b139ba047b74e31cccf0e3919c17436632e))


## v0.1.3 (2025-02-17)

### Bug Fixes

- Debug
  ([`5615203`](https://github.com/edalfon/stepit/commit/56152038bd34593aaf64ea75cd86a29c807719ab))


## v0.1.2 (2025-02-17)

### Bug Fixes

- Barebones test
  ([`d99a21a`](https://github.com/edalfon/stepit/commit/d99a21a8f9478f94eec9f930c53047d12280c34b))


## v0.1.1 (2025-02-17)

### Bug Fixes

- Debug test
  ([`07a46a0`](https://github.com/edalfon/stepit/commit/07a46a0f254ce6466bd291119dca5191384a2ce1))

### Build System

- Amend makefile
  ([`90988fe`](https://github.com/edalfon/stepit/commit/90988febf0a6ddcc96bc949894b00073f7558825))


## v0.1.0 (2025-02-17)

### Build System

- Uv's lock file and gitignore cache dirs
  ([`98ce3a2`](https://github.com/edalfon/stepit/commit/98ce3a2d0117c514e42567f5bde865ed8f9c9cbb))

### Documentation

- Add readme first version
  ([`61d9ac0`](https://github.com/edalfon/stepit/commit/61d9ac0890c6f1586c90aed8dd02ef816ea5efb1))

### Features

- Add first working version
  ([`115d56e`](https://github.com/edalfon/stepit/commit/115d56e6165d71eacf192adb551ce9fd4b538164))

### Testing

- Add first round of tests
  ([`11a3c44`](https://github.com/edalfon/stepit/commit/11a3c44f5cd4bc27d60b7c4f8ec843db42c55c4a))


## v0.0.0 (2025-02-17)
