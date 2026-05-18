import re
import unittest
from pathlib import Path

import yaml


REPO_ROOT = Path(__file__).resolve().parent.parent
SKILL_INSTALLER = REPO_ROOT / "skill-installer" / "SKILL.md"
EXPECTED_CHINESE_DISCOVERY_EXAMPLE = "我找一個superpower skill"


class SkillInstallerMetadataTests(unittest.TestCase):
    def test_description_mentions_skill_discovery_and_superpower_request(self):
        content = SKILL_INSTALLER.read_text(encoding="utf-8").lstrip("\ufeff")
        match = re.search(r"^---\n(.*?)\n---", content, re.DOTALL | re.MULTILINE)

        self.assertIsNotNone(match)
        frontmatter = yaml.safe_load(match.group(1))

        self.assertIsInstance(frontmatter, dict)
        description = frontmatter.get("description")
        self.assertIsInstance(description, str)
        self.assertIn("discover the right skill", description)
        self.assertIn(EXPECTED_CHINESE_DISCOVERY_EXAMPLE, description)


if __name__ == "__main__":
    unittest.main()
