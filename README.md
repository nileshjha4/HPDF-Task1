# HPDF-Task 1

This repository is being maintained as a part of Hasura Product Development Fellowship and consists the sourcecode for a series of sub tasks assigned to me during first week of fellowship. For this task, we are expected to build a FLASK based web application with  various endpoints each serving different purpose. Brief overview of all the endpoints is provided in Endpoints section.

### Prerequisites

Python 3.6.3 or above

### Getting started

1. Clone the git repo on your machine.

```
git clone https://github.com/Sneaky-petrodectyl/HPDF-Task1
```

2. Install packages.

```
pip install -r requirements.txt
```

3. Launch app:
   - Run the application.
	```
	python app.py
	```
   - Explore the endpoints at `127.0.0.1:5000/`.

## Endpoints

- `/` : It returns a simple string with hello message.
- `/authors/` : It fetches and displays a list of author and their corresponding no. of posts.
- `/setcookie/` : It sets cookies.
- `/getcookie/` : Displays cookies.
- `/robot.txt/` : Access is denied to this endpoint.
- `/image/` : Responds with an image file.
-  `/input/` : Logs the form data to stdout.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
