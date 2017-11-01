# pyramid-learning-journal

A simple Pyramid app for listing, displaying and editing blog posts.

**Authors**:

- Kavdi H. (kavdyjh@gmail.com)

## Routes:

- `/` - the home page and a listing of all posts
- `/journal/id` - to to view the post
- `/create/id` - to create a new post
- `/update/id` - to edit a post

## Set Up and Installation:

- Clone this repository to your local machine.

- Begin a new virtual environment with Python 3 and activate it.

- `pip install` the packages into your virtual environment.

- `$ initialize_db development.ini` to initialize the database, populating with random models.

- `$ pserve development.ini --reload` to serve the application on `http://localhost:6543`

## To Test

- If you have the `testing` extras installed, testing is simple. If you're in the same directory as `setup.py` type the following:

```
$ py.test expense_tracker
```