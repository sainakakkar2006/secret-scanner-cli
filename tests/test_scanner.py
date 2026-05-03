import tempfile
import unittest
from pathlib import Path

from secret_scanner.scanner import mask_secret, scan_path


class ScannerTests(unittest.TestCase):
    def test_detects_and_masks_known_secret_patterns(self):
        with tempfile.TemporaryDirectory() as temp_name:
            path = Path(temp_name) / "config.py"
            secret = "AKIA" + "1234567890ABCDEF"
            path.write_text(f'KEY = "{secret}"\n', encoding="utf-8")

            findings = scan_path(path)

        self.assertEqual(len(findings), 1)
        self.assertEqual(findings[0].rule, "AWS access key")
        self.assertEqual(findings[0].line, 1)
        self.assertNotIn("1234567890", findings[0].value)

    def test_scans_directories_and_ignores_binary_files(self):
        with tempfile.TemporaryDirectory() as temp_name:
            root = Path(temp_name)
            (root / "app.py").write_text("password=super-secret\n", encoding="utf-8")
            (root / "image.png").write_bytes(b"\x89PNG\x00\x00")

            findings = scan_path(root)

        self.assertEqual(len(findings), 1)
        self.assertEqual(findings[0].rule, "Environment assignment with secret-like name")

    def test_mask_secret_keeps_short_values_hidden(self):
        self.assertEqual(mask_secret("abc"), "***")

    def test_missing_path_raises_error(self):
        with self.assertRaises(FileNotFoundError):
            scan_path("/definitely/missing/path")


if __name__ == "__main__":
    unittest.main()
