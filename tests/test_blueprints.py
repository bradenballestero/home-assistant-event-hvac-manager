"""Static repository checks; Home Assistant runtime testing is still required."""
import unittest
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]


class Loader(yaml.SafeLoader):
    pass


def input_tag(loader, node):
    return {"!input": loader.construct_scalar(node)}


Loader.add_constructor("!input", input_tag)


def read(path):
    return yaml.load((ROOT / path).read_text(), Loader=Loader)


class BlueprintChecks(unittest.TestCase):
    def test_yaml_files_parse(self):
        for path in list((ROOT / "blueprints").rglob("*.yaml")) + list((ROOT / "examples").rglob("*.yaml")):
            with self.subTest(path=path):
                yaml.load(path.read_text(), Loader=Loader)

    def test_example_inputs_exist_and_required_inputs_are_supplied(self):
        blueprint = read("blueprints/automation/event_hvac_manager.yaml")
        inputs = blueprint["blueprint"]["input"]
        example = read("examples/sanctuary-example.yaml")["use_blueprint"]["input"]
        self.assertFalse(set(example) - set(inputs))
        self.assertFalse({name for name, spec in inputs.items() if "default" not in spec} - set(example))

    def test_all_blueprint_inputs_are_declared(self):
        def references(value):
            if isinstance(value, dict):
                if set(value) == {"!input"}:
                    return {value["!input"]}
                return set().union(*(references(v) for v in value.values()))
            if isinstance(value, list):
                return set().union(*(references(v) for v in value))
            return set()

        for path in (ROOT / "blueprints").rglob("*.yaml"):
            with self.subTest(path=path):
                blueprint = yaml.load(path.read_text(), Loader=Loader)
                self.assertFalse(references(blueprint) - set(blueprint["blueprint"]["input"]))

    def test_decision_priority(self):
        blueprint = read("blueprints/automation/event_hvac_manager.yaml")
        choices = blueprint["action"][0]["choose"]
        modes = [choice["sequence"][0]["variables"]["selected_mode"] for choice in choices]
        self.assertEqual(modes, ["Admin Comfort", "Hold Current", "Blocked", "Calendar Unavailable", "Event", "Eco", "Manual Cool", "Occupied", "Office or School"])
        self.assertEqual(blueprint["action"][0]["default"][0]["variables"]["selected_mode"], "Eco")


if __name__ == "__main__":
    unittest.main()
