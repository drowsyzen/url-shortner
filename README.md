#  url-shortner

 url-shortner is a project for a  url-shortening application built with Django. This project provides api for generating a short url on the django application , which can be accessed o go to long(ORIGINAL) url.

## Table of Contents

- [Installation](#installation)
- [API Endpoints](#api-endpoints)
  - [URL-generation](#url-generation)
  - [User Registration](#user-registration)
  - [Note Management](#note-management)

## Installation

To get started with NoteAppBackend, follow these steps:

1. Clone the repository:

    ```bash
    git clone https://github.com/drowsyzen/markdown-Note-taking-App.git
    ```

2. Navigate to the project directory:

    ```bash
    cd noteappbackend
    ```

3. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Apply migrations:

    ```bash
    python manage.py migrate
    ```

5. Start the development server:

    ```bash
    python manage.py runserver
    ```

## API Endpoints

### url-generation

- **url-generation**
  - **URL:** `generate_url`
  - **Method:** `POST`
  - **Description:** Obtain a new short URL from the Endpoint by providing long url.

<!-- finished Version 1 , date - 3 july 2024  -->

##### version 1(end date) - 3 july 2024

<!-- NEED TO DO -->

<!-- fix new logic for short URL generation -->
<!-- need to return write url in generate url which can be directly pasted in browser -->
<!-- return different types of error in the generate url api -->