# Contributing

Issues and pull requests are welcome. Include your Home Assistant version, thermostat integration and capabilities, relevant entity states, expected and actual behavior, and a sanitized automation trace. Remove private calendar details, tokens, and URLs.

The newer blueprint currently targets Fahrenheit dual-setpoint `heat_cool` zones. Please describe compatibility implications when proposing broader support. The legacy blueprint is retained separately; changes to it should preserve its existing behavior unless clearly documented.

## Validation

Run the repository checks with Python 3:

```sh
python -m pip install PyYAML
python -m unittest discover -s tests -v
```

These checks parse the YAML and check the example and selected decision ordering. They do not execute Home Assistant templates or thermostat actions. For behavioral changes, also validate the blueprint and exercise the relevant cases in a Home Assistant instance; include the version and results in the pull request. Never assume a passing static check proves a thermostat command succeeded.
