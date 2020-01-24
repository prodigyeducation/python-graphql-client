# Introduction

First off, thanks for even considering to contribute to this project!

The goal of this document is to hopefully fill in any gaps in knowledge for how you can help.

# Table of Contents

-   [Introduction](#introduction)
-   [Table of Contents](#table-of-contents)
-   [Getting started](#getting-started)
-   [Testing](#testing)
-   [How to submit changes](#how-to-submit-changes)
-   [How to report a bug](#how-to-report-a-bug)
-   [How to request an enhancement](#how-to-request-an-enhancement)
-   [Style Guide](#style-guide)
-   [Code of Conduct](#code-of-conduct)
-   [Where can I ask for help?](#where-can-i-ask-for-help)

# Getting started

First thing you'll need to do is clone the project.

```bash
git clone git@github.com:prodigyeducation/python-graphql-client.git
```

After that you'll need to install the required python dependencies as well as development dependencies for linting the project.

```bash
pip install -e ."[dev]"
```

Finally, you should make sure `pre-commit` has setup the git hooks on your machine by running the following command. This will run the automated checks every time you commit.

```bash
pre-commit install
```

# Testing

Once the above setup is complete, you can run the tests with the following command.

```bash
make tests
```

# How to submit changes

1. Create a fork of the repository. Checkout this [github article](https://help.github.com/en/github/getting-started-with-github/fork-a-repo) for more information.
2. Make changes in your fork of the project.
3. Open a pull request to merge the changes in your fork back into the main repository. Follow the pull request template with details about the changes you're adding.

# How to report a bug

1. Do a scan of the [issues](https://github.com/prodigyeducation/python-graphql-client/issues) on the github repository to see if someone else has already opened an issue similar to yours.
2. Create an issue on github using the `Bug report` template.
3. Fill out the issue template with relevant details.

# How to request an enhancement

1. Do a scan of the [issues](https://github.com/prodigyeducation/python-graphql-client/issues) on the github repository to see if someone else has already opened an issue similar to yours.
2. Create an issue on github using the `Feature request` template.
3. Fill out the issue template with relevant details.

# Style Guide

This project uses some automated linter and style checks to make sure the code quality stays at an acceptable level. All the checks used in this project should run when you commit (thanks to pre-commit and git hooks) and remotely when creating the pull request (thanks to github actions).

# Code of Conduct

Take a peek at the [Code of Conduct](CODE_OF_CONDUCT.md) document for more information.

# Where can I ask for help?

This project is pretty new, so for now feel free to add an issue into the project. Otherwise you can always email us at opensource@prodigygame.com for questions. Maybe one day we'll create a slack group for this project.
