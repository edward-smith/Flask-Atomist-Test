# Flask-Atomist-Test

Testing out Atomist

## Setting up the environment

This project depends on [Python](https://www.python.org/) 2.7+ or 3.4+
and the [Flask](http://flask.pocoo.org/) web framework.

Once you have installed Python for your environment, you
should also setup a [virtual environment](https://virtualenv.pypa.io/en/stable/)
with [pip](https://pip.pypa.io/en/stable/installing/).

Then, you should install the dependencies required by
the project as follows:

```
$ pip install -r requirements.txt
```


## Getting started

Before you can run the application, the package must be found
in your `PYTHONPATH`. To do so, run the next command once:

```
$ python setup.py develop
```

Run the application as follows:

```
$ python -m Flask-Atomist-Test --dev
```

then point your client at `http://localhost:5000/`.

## Develop your application

### Run tests

Tests are part of the project and should be continuously. Those
tests are implemented using the [py.test](http://pytest.readthedocs.io/en/latest/)
framework and located in the `tests` directories.

To execute them, run the following command:

```
$ pytest -v
```

## Package & distribute your application as a container image

The project provides a recipe to build a Docker
image of the application and its dependencies to
simply its distribution. You can build the image
as follows:

```
$ docker build -t Flask-Atomist-Test .
```

To run the application inside a container, execute then
the following commands:

```
$ docker run -d -p 5000:5000 Flask-Atomist-Test
```

This will use [CherryPy](http://cherrypy.org/) well-established
and production ready WSGI server.
