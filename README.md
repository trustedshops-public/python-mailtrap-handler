# python-mailtrap-handler
[![GitHub License](https://img.shields.io/badge/license-MIT-lightgrey.svg)](https://github.com/trustedshops-public/mailtrap-handler/blob/main/LICENSE)
[![pre-commit](https://img.shields.io/badge/%E2%9A%93%20%20pre--commit-enabled-success)](https://pre-commit.com/)
[![CircleCI](https://circleci.com/gh/trustedshops-public/python-mailtrap-handler/tree/main.svg?style=shield)](https://circleci.com/gh/trustedshops-public/mailtrap-handler/tree/main)
[![PyPI version](https://badge.fury.io/py/mailtrap-handler.svg)](https://pypi.org/project/mailtrap-handler)

Implementation for MailTrap basic functionalities using Python.

## Requirements

All you need is Python version 3.6 or above

## Installation

```sh
pip3 install mailtrap-handler
```

## Usage

For [dedicated documentation click here](https://trustedshops-public.github.io/python-mailtrap-handler/mailtrap_handler)

```python
from mailtrap_handler import MailTrapHandler

mailtrap = MailTrapHandler(TOKEN)
# then do what you need with the mailtrap object
```

### Functions

Get mail id:

```python
# default value for title is None
list_of_ids = mailtrap.get_mail_id(inbox, email, title="Some Title here")
# returns a list of found mails ids
```

Get mail html content:

```python
# default value for title is None
# default value for waiting_time is 0
MailTrapHandler.get_mail(inbox, email, title, waiting_time=30)
# returns mail html content
```

Clean the inbox:

```python
MailTrapHandler.clean_inbox(inbox)
```

Delete target mail:

```python
MailTrapHandler.delete_mail(inbox, email, title="Some Title here")
# default value for title is None
```

## Example Code

```python
from mailtrap_handler import MailTrapHandler

# requirements
token = "123wellthiswouldbeyourtokenhere098"
inbox = 12349876  # this is your mailtrap inbox id
email = "target_email+probably_with_some_alias@inbox.mailtrap.io"
title = "Oy! Congrats on getting Your new T-shirt"

# creating mailtraphandler object
mailtrap = MailTrapHandler(token)

# getting the html content
mails = mailtrap.get_mail(inbox, email, title=title, 10)

# we do now whatever we need with the recieved mails
# and now we delete this mail
mailtrap.delete_mail(inbox, email, title=title)

# you know what let's just delete every mail in the inbox
mailtrap.clean_inbox(inbox)

# I got no more mails!
```

## How to Contribute

We welcome [issues](https://github.com/trustedshops-public/python-mailtrap-handler/issues) to
and [pull requests](https://github.com/trustedshops-public/python-mailtrap-handler/pulls) against this repository!

### Commit Message Convention

This repository follows [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/)

#### Format

`<type>(optional scope): <description>`
Example: `feat(pre-event): Add speakers section`

#### 1. Type

Available types are:

- feat → Changes about addition or removal of a feature. Ex: `feat: Add table on landing page`
  , `feat: Remove table from landing page`
- fix → Bug fixing, followed by the bug. Ex: `fix: Illustration overflows in mobile view`
- docs → Update documentation (README.md)
- style → Updating style, and not changing any logic in the code (reorder imports, fix whitespace, remove comments)
- chore → Installing new dependencies, or bumping deps
- refactor → Changes in code, same output, but different approach
- ci → Update github workflows, husky
- test → Update testing suite, cypress files
- revert → when reverting commits
- perf → Fixing something regarding performance (deriving state, using memo, callback)

#### 2. Optional Scope

Labels per page Ex: `feat(pre-event): Add date label`

*If there is no scope needed, you don't need to write it*

#### 3. Description

Description must fully explain what is being done.

Add BREAKING CHANGE in the description if there is a significant change.

**If there are multiple changes, then commit one by one**

- After colon, there are a single space Ex: `feat: Add something`
- When using `fix` type, state the issue Ex: `fix: File size limiter not working`
- Use imperative, dan present tense: "change" not "changed" or "changes"
- Use capitals in front of the sentence
- Don't add full stop (.) at the end of the sentence

### Publish new release

Commit according to semantic release spec above and let CircleCI (and semantic-release) do the magic.
