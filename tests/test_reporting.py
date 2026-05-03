import json
import unittest

from secret_scanner.reporting import findings_to_json, findings_to_text
from secret_scanner.scanner import Finding


class ReportingTests(unittest.TestCase):
    def test_json_report_has_total_and_findings(self):
        report = findings_to_json(
            [Finding(path="app.py", line=1, rule="Token", severity="HIGH", value="abcd****wxyz")]
        )

        payload = json.loads(report)
        self.assertEqual(payload["total_findings"], 1)
        self.assertEqual(payload["findings"][0]["path"], "app.py")

    def test_text_report_handles_empty_findings(self):
        self.assertEqual(findings_to_text([]), "No secrets found.")


if __name__ == "__main__":
    unittest.main()

