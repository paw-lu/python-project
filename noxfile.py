import nox

locations = "src", "tests", "noxfile.py"
nox.options.sessions = "lint", "tests"


@nox.session(python=["3.8", "3.7"])
def tests(session):
    args = session.posargs or ["--cov", "-m", "not e2e"]
    session.run("poetry", "install", external=True)
    session.run("pytest", *args)


@nox.session(python=["3.8", "3.7"])
def lint(session):
    args = session.posargs or locations
    # Would typically just install flake8 and extensions, but isort
    # needs to see which packages are installed
    session.run("poetry", "install", external=True)
    session.run("flake8", *args)


@nox.session(python="3.8")
def sort(session):
    args = session.posargs or locations
    # isort needs to see which packages are installed to properly sort
    # imports
    session.run("poetry", "install", external=True)
    session.run("isort", "-rc", *args)


@nox.session(python="3.8")
def black(session):
    args = session.posargs or locations
    session.install("black")
    session.run("black", *args)
