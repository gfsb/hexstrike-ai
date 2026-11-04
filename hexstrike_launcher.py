"""Console-script launcher for the HexStrike AI API server.

``hexstrike_server.py`` performs its startup inside an ``if __name__ ==
"__main__"`` block rather than a callable function, so it cannot be referenced
directly as a ``module:function`` entry point. This thin wrapper executes that
module as ``__main__`` (exactly as ``python3 hexstrike_server.py`` would),
passing command-line arguments through untouched, so that `pip install`
can expose a ``hexstrike-server`` command on PATH without modifying the
server module itself.
"""

import runpy


def run_server() -> None:
    """Run hexstrike_server.py as if invoked as a script."""
    # run_name="__main__" triggers the server's startup block; argv is already
    # set by the console-script entry point, so argparse inside it sees the
    # user's flags (e.g. --debug, --port).
    runpy.run_module("hexstrike_server", run_name="__main__", alter_sys=True)


if __name__ == "__main__":
    run_server()
