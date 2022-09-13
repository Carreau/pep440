import os

import pytest
import pep440

NAME = "pep440"

@pytest.fixture
def cli(script_runner):
    def run_cli(*args, **kwargs):
        env = dict(os.environ)
        env.update(kwargs.pop("env", {}))
        env["PYTHONIOENCODING"] = "utf-8"
        kwargs["env"] = env
        return script_runner.run(NAME, *map(str, args), **kwargs)

    return run_cli


@pytest.mark.parametrize("args,rc", [
    [["--help"], 0],
    [[], 2]
])
def test_cli_help(cli, args, rc):
    ret = cli(*args)
    assert ret.returncode == rc
    assert f"usage: {NAME}" in ret.stdout.strip()

@pytest.mark.parametrize("version,rc",[
    ["0.0.0", 0],
    ["not-a-version", 1]
])
def test_cli_version(cli, version, rc):
    ret = cli(version)
    assert ret.returncode == rc
