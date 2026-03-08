import nox

pythons = ["3.10", "3.11", "3.12", "3.13", "3.14"]
djangos = ["4.2", "5.0", "6.0"]


@nox.session(venv_backend="uv")
@nox.parametrize(
    "python,django",
    [
        (python, django)
        for python in pythons
        for django in djangos
        if (python, django) not in [("3.11", "6.0"), ("3.10", "6.0")]
    ],
)
def test(session, django):
    """Run tests."""
    session.install(f"django=={django}")

    session.run(
        "pytest",
        "--cov-report=term-missing",
        "--cov-config=pyproject.toml",
        "--cov=django_view_decorator",
        "--cov=tests",
        "--cov=append",
    )
