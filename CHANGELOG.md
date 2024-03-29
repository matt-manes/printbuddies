# Changelog

## v2.1.3 (2024-02-22)

#### Refactorings

* import `typing_extensions` instead of `typing`


## v2.1.2 (2024-02-20)

#### Refactorings

* add additional `__init__` args

## v2.1.1 (2024-02-20)

#### Refactorings

* change `TaskProgressColumn` default significant digits


## v2.1.0 (2024-02-18)

#### New Features

* add `Grid` class
#### Performance improvements

* calculate gradient sequence without needing to split text into batches


## v2.0.3 (2024-02-18)

#### Refactorings

* clean up namespace by condensing imports
* override `BarColumn` and `TaskProgressColumn` instead of using get functions


## v2.0.2 (2024-02-18)

#### Fixes

* fix type checker not recognizing `add_task` override
#### Refactorings

* make `track` uses same default columns as `Progress`
* make progbar tests faster
* remove unneeded `Progress.__init__()` override


## v2.0.1 (2024-02-18)

#### Refactorings

* change default pulse style


## v2.0.0 (2024-02-17)

#### New Features

* add helpers and default overrides for rich package
#### Refactorings

* BREAKING - remove poolbar


## v1.5.0 (2024-02-14)

#### New Features

* add support for using `rich` formatted strings


## v1.4.1 (2023-09-29)

#### Fixes

* fix type annotation in PoolBar constructor

## v1.4.0 (2023-09-29)

#### New Features

* add thread/process pool executor and ProgBar integration class

## v1.3.1 (2023-06-10)

#### Fixes

* add exception handling to prevent crashing when there is no terminal
#### Refactorings

* make ProgBar.bar a property
#### Docs

* update readme
* update and improve docstrings
## v1.3.0 (2023-06-03)

#### New Features

* add movement to Spinner
* sequence width will update when the terminal width changes
#### Refactorings

* default character sequence is assigned as parameter default
* change width parameter to width_ratio
#### Others

* add missing version prefix


## v1.2.0 (2023-04-25)

#### New Features

* implement Spinner class
* add context manager functionality
* add runtime property to ProgBar
* implement update_frequency functionality
#### Fixes

* fix bug where bar display exceeds width_ratio if counter goes above total
#### Performance improvements

* remove leading space when no prefix is passed to display
#### Refactorings

* remove total property and start counter at 1 instead of 0
* improve type annotations
#### Docs

* update readme
* improve display() doc string


## v1.1.0 (2023-04-16)

#### Fixes

* update minimum python version required


## v1.0.2 (2023-03-22)

#### Others

* build v1.0.2
* update readme


## v1.0.1 (2023-02-13)

#### Fixes

* fix counter_override in error in ProgBar.display() if passed value is 0
#### Others

* build v1.0.1
* update changelog