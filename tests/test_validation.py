import os
import unittest
import yaml

class TestAlertmanagerConfig(unittest.TestCase):
    def test_core_files_exist(self):
        required_files = [
            "README.md",
            "Makefile",
            "SECURITY.md",
            ".gitattributes",
            ".github/workflows/ci.yml",
            "scripts/healthcheck.sh",
            "config/production.env.example",
            "alertmanager.yml",
            "inhibit_rules.yml",
            "docker-compose.yml",
            "docs/architecture.svg",
            "templates/default.tmpl"
        ]
        for file_path in required_files:
            self.assertTrue(os.path.exists(file_path), f"Missing required file: {file_path}")

    def test_alertmanager_yaml_validity(self):
        with open("alertmanager.yml", "r", encoding="utf-8") as f:
            config = yaml.safe_load(f)
        
        self.assertIn("global", config)
        self.assertIn("route", config)
        self.assertIn("receivers", config)
        self.assertIn("inhibit_rules", config)

        # Verify default receiver and grouping
        route = config["route"]
        self.assertEqual(route["receiver"], "slack-default")
        self.assertIn("alertname", route["group_by"])
        self.assertIn("cluster", route["group_by"])

        # Check critical receiver definitions
        receiver_names = {r["name"] for r in config["receivers"]}
        self.assertIn("pagerduty-high-priority", receiver_names)
        self.assertIn("slack-critical-warroom", receiver_names)
        self.assertIn("pagerduty-dba-oncall", receiver_names)
        self.assertIn("slack-security-soc", receiver_names)

    def test_inhibition_rules_structure(self):
        with open("inhibit_rules.yml", "r", encoding="utf-8") as f:
            rules_doc = yaml.safe_load(f)
        
        self.assertIn("inhibit_rules", rules_doc)
        rules = rules_doc["inhibit_rules"]
        self.assertGreaterEqual(len(rules), 3)
        for rule in rules:
            self.assertTrue("source_match" in rule or "source_match_re" in rule)
            self.assertTrue("target_match" in rule or "target_match_re" in rule)
            self.assertIn("equal", rule)

    def test_architecture_diagram_white_theme(self):
        with open("docs/architecture.svg", "r", encoding="utf-8") as f:
            svg_content = f.read()
        self.assertIn('fill="#ffffff"', svg_content, "SVG must feature strict pure white background")
        self.assertIn('Alertmanager', svg_content)

if __name__ == "__main__":
    unittest.main()
