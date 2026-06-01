# Home Assistant Event HVAC Manager

Readable Home Assistant HVAC automations for churches, venues, offices, classrooms, and other shared spaces.

This project started as a real-world church Sanctuary HVAC setup. The goal is simple: make HVAC behavior understandable, predictable, and safe to override.

It is not AI-first. It is **human-first**. The automation is written so a person, an admin, or an AI assistant can look at Home Assistant and answer:

- What mode is the room in?
- Why is it in that mode?
- What is allowed to override it?
- When will the override expire?
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
- Keeps the control path legible for humans and safe for assistants.

## Current Status

This is an early extraction from a working Home Assistant setup. The included blueprint is the reusable starting point. The `examples/` folder shows how the original Sanctuary-style setup maps into the project.

## Files

- `blueprints/automation/event_hvac_manager.yaml` - reusable Home Assistant automation blueprint
- `examples/sanctuary-example.yaml` - example automation using the pattern
- `docs/helpers.md` - helper entities that make the automation readable
- `docs/ai-support-bot.md` - how to let an assistant help safely
- `docs/troubleshooting.md` - common problems and what to check first

## Design Philosophy

Most HVAC automations fail in boring ways:

- The calendar briefly goes unavailable and the automation thinks the event ended.
- One thermostat updates and the other does not.
- A manual wall change fights the automation.
- Nobody can tell why the room changed modes.
- The automation hammers a slow thermostat cloud integration every few minutes.

This project treats HVAC automation like a small control panel, not a hidden script. The important decisions are exposed through helpers and plain-English reason fields.

## Safe Assistant Pattern

An assistant should not directly control random Home Assistant devices. The safer model is:

1. Read current state.
2. Explain what is happening.
3. Change only approved HVAC helper entities.
4. Use bounded temperatures and timers.
5. Let the automation remain the source of truth.

For example, if someone says, "It is hot in the Sanctuary," the assistant should inspect the room temperature, active mode, calendar, blockers, and current thermostat state. Then it can turn on an approved helper like Manual Cool or Admin Comfort for a limited time.

## Installation

Copy `blueprints/automation/event_hvac_manager.yaml` into:

```text
config/blueprints/automation/readable_hvac/event_hvac_manager.yaml
```

Then create a new automation from the blueprint in Home Assistant.

## License

MIT
