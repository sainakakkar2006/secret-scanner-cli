import tempfile
import unittest
from contextlib import redirect_stdout
from io import StringIO
from pathlib import Path

from secret_scanner.cli import main


class CLITests(unittest.TestCase):
    def test_cli_returns_nonzero_when_findings_exist(self):
        with tempfile.TemporaryDirectory() as temp_name:
            path = Path(temp_name) / ".env"
            path.write_text("TOKEN=demo-token\n", encoding="utf-8")

            with redirect_stdout(StringIO()):
                exit_code = main(["scan", str(path)])

        self.assertEqual(exit_code, 1)

    def test_cli_no_fail_keeps_exit_code_zero(self):
        with tempfile.TemporaryDirectory() as temp_name:
            path = Path(temp_name) / ".env"
            path.write_text("TOKEN=demo-token\n", encoding="utf-8")

            with redirect_stdout(StringIO()):
                exit_code = main(["scan", str(path), "--no-fail"])

        self.assertEqual(exit_code, 0)


if __name__ == "__main__":
    unittest.main()
