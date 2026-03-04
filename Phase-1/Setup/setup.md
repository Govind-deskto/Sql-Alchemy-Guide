# Setup Guide

This document explains how to set up the environment for this project.

------------------------------------------------------------------------

## 1. Create a Virtual Environment (Recommended)

``` bash
python -m venv venv
```

Activate the environment.

### Linux / Mac

``` bash
source venv/bin/activate
```

### Windows

``` bash
venv\Scripts\activate
```

------------------------------------------------------------------------

## 2. Install Dependencies

Install the required packages using:

``` bash
python -m pip install -r requirements.txt
```

------------------------------------------------------------------------

## requirements.txt

``` txt
sqlalchemy>=2.0
```

------------------------------------------------------------------------

## Notes

-   The project currently requires **SQLAlchemy only**.
-   SQLite works out of the box with Python, so no additional driver
    installation is required.
-   You can later configure MySQL or PostgreSQL if needed.
