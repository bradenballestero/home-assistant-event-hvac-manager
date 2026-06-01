# Home Assistant Event HVAC Manager

Readable Home Assistant HVAC automation for churches, venues, offices, classrooms, and other shared spaces.

This project started as a real-world church Sanctuary HVAC setup. The goal is simple: make HVAC behavior understandable, predictable, and safe to override.

The automation is designed so a non-coder can open Home Assistant and answer:

- What mode is the room in?
- Why is it in that mode?
- What is allowed to override the normal schedule?
- Did it actually need to touch the thermostats?

## What It Does

- Uses calendar events and pre-cool windows.
- Supports normal weekly office/school hours.
- Supports Eco fallback when nothing important is happening.
- Supports blockers like cleaning, prayer, maintenance, or "do not touch HVAC."
- Supports admin comfort and temporary manual cooling patterns.
- Avoids reacting to brief calendar `unavailable` reload blips.
- Avoids sending repeated thermostat commands when the thermostat is already correct.
- Uses a simple startup/cadence trigger in the reusable blueprint for portability.
- Keeps the control path legible for people who do not want to debug mystery YAML.

## Current Status

This is an early extraction from a working Home Assistant setup. The included blueprint is the reusable starting point. The `examples/` folder shows how the original Sanctuary-style setup maps into the project.

## Files

- `blueprints/automation/event_hvac_manager.yaml` - reusable Home Assistant automation blueprint
- `examples/sanctuary-example.yaml` - example automation using the pattern
- `docs/helpers.md` - helper entities that make the automation readable
- `docs/troubleshooting.md` - common problems and what to check first

## Design Philosophy

Most HVAC automations fail in boring ways:

- The calendar briefly goes unavailable and the automation thinks the event ended.
- One thermostat updates and the other does not.
- A manual wall change fights the automation.
- Nobody can tell why the room changed modes.
- The automation hammers a slow thermostat cloud integration every few minutes.

This project treats HVAC automation like a small control panel, not a hidden script. The important decisions are exposed through helpers and plain-English reason fields.

## Installation

Copy `blueprints/automation/event_hvac_manager.yaml` into:

```text
config/blueprints/automation/readable_hvac/event_hvac_manager.yaml
```

Then create a new automation from the blueprint in Home Assistant.

## License

MIT
