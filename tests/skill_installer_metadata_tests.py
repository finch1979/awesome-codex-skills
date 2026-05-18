import re
import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parent.parent
SKILL_INSTALLER = REPO_ROOT / "skill-installer" / "SKILL.md"


class SkillInstallerMetadataTests(unittest.TestCase):
    def test_description_mentions_skill_discovery_and_superpower_request(self):
        content = SKILL_INSTALLER.read_text(encoding="utf-8")
        match = re.match(r"^---\n(.*?)\n---", content, re.DOTALL)

        self.assertIsNotNone(match)
        frontmatter = match.group(1)
        description_line = next(
            line for line in frontmatter.splitlines() if line.startswith("description:")
        )

        self.assertIn("discover the right skill", description_line)
        self.assertIn('我找一個superpower skill', description_line)


if __name__ == "__main__":
    unittest.main()
