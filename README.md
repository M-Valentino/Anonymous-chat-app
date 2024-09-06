# Real-Time Chat Application with Django Channels

## Overview
This is a real-time chat application built using Django Channels and WebSockets. Users can chat with their friends anonymously by creating or joining a chat room using a room code. This repo is a fork from another chat app created by [NancyAanchal](https://github.com/NancyAanchal/Anonymous-chat-app).

## Features

- Create and join chat rooms using a room code
- Real-time messaging with WebSockets
- Anonymous chat without requiring user registration

## Technologies Used

- Django
- Django Channels
- WebSockets
- HTML/CSS/JavaScript

## Running
You will need to install the following Python modules in addition to Django:
- `Celery`
- `Channels`
- `Daphne`

To install these all at once, you can run:
`pip install -r requirements.txt`

### Running With Debug Mode:
First go to `settings.py` and make sure `DEBUG = True`.
Then run:
```
python manage.py runserver

```

### Running Without Debug Mode:
First go to `settings.py` and make sure `DEBUG = False`.
Then run:
```
python manage.py collectstatic
python manage.py runserver

```

## License
This project is licensed under the MIT License.

