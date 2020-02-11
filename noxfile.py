import tempfile

import nox
from nox.sessions import Session

locations = "src", "tests", "noxfile.py"
nox.options.sessions = "lint", "mypy", "pytype", "safety", "tests"


def install_with_constraints(session, *args, **kwargs):
    with tempfile.NamedTemporaryFile() as requirements:
        session.run(
            "poetry",
            "export",
            "--dev",
            "--format=requirements.txt",
            f"--output={requirements.name}",
            external=True,
        )
        session.install(f"--constraint={requirements.name}", *args, **kwargs)


@nox.session(python=["3.8", "3.7"])
def tests(session):
    args = session.posargs or ["--cov", "-m", "not e2e"]
    session.run("poetry", "install", "--no-dev", external=True)
    install_with_constraints(
        session, "coverage[toml]", "pytest", "pytest-cov", "pytest-mock"
    )
    session.run("pytest", *args)


# TODO: Add more flake8 plugins
@nox.session(python=["3.8", "3.7"])
def lint(session):
    args = session.posargs or locations
    # Would typically just install flake8 and extensions, but isort
    # needs to see which packages are installed
    session.run("poetry", "install", "--no-dev", external=True)
    # Manually add non dev packages which are imported, like pytest
    install_with_constraints(
        session,
        "flake8",
        "flake8-bandit",
        "flake8-black",
        "flake8-bugbear",
        "flake8-isort",
        "toml",
        "pytest",
    )
    session.run("flake8", *args)


@nox.session(python="3.8")
def sort(session):
    args = session.posargs or locations
    # isort needs to see all installed packages that are imported
    session.run("poetry", "install", "--no-dev", external=True)
    # Manually add any non dev packages which are imported, like pytest
    install_with_constraints(session, "pytest", "toml")
    session.run("isort", "-rc", *args)


@nox.session(python="3.8")
def black(session):
    args = session.posargs or locations
    install_with_constraints(session, "black")
    session.run("black", *args)


@nox.session(python="3.8")
def safety(session):
    with tempfile.NamedTemporaryFile() as requirements:
        session.run(
            "poetry",
            "export",
            "--dev",
            "--format=requirements.txt",
            "--without-hashes",
            f"--output={requirements.name}",
            external=True,
        )
        install_with_constraints(session, "safety")
        session.run("safety", "check", f"--file={requirements.name}", "--full-report")


@nox.session(python=["3.8", "3.7"])
def mypy(session: Session) -> None:
    args = session.posargs or locations
    install_with_constraints(session, "mypy")
    session.run("mypy", *args)


# TODO: Update pytype
# As of now (2-11-2020), pytype does not yet support 3.8
# https://github.com/google/pytype/issues/440
@nox.session(python=["3.7"])
def pytype(session):
    """Run the static type checker."""
    args = session.posargs or ["--disable=import-error", *locations]
    install_with_constraints(session, "pytype")
    session.run("pytype", *args)
