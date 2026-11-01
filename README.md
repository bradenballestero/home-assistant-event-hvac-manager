# Home Assistant Event HVAC Manager

A Home Assistant blueprint for managing one shared HVAC zone from a calendar, a weekly schedule, occupancy, and manual controls. Optional text helpers show the selected mode and the reason for it.

**Status:** The newer Event HVAC Manager is experimental and is still being field-tested. The [legacy blueprint](blueprints/automation/calendar_master_climate_control_legacy.yaml) is the first-generation version used at the original facility. Review and test either blueprint against your own equipment before relying on it.

## Is it a fit?

The newer blueprint is intended for a zone whose thermostats all support either Home Assistant's `heat_cool` mode with low and high targets, or `cool` mode with a single target, as selected in the blueprint. The thermostats must also support the selected `on` and `auto` fan modes. Inputs are in Fahrenheit. It sends the same settings to all selected thermostats. It requires a calendar entity with `start_time` and `end_time` attributes. Check your thermostat integration and calendar before installation; other equipment and Celsius installations have not been established as supported.

It checks on Home Assistant startup and at the selected interval (15 minutes by default). Add control and occupancy entities to **Controls to watch** for prompt reevaluation. Changes to other inputs, including calendar events, can take up to one interval to be evaluated. A blocker or hold prevents future commands once evaluated; it does not stop a command already in progress. Calendar unavailability holds the current settings, except when a higher-priority blocker, admin comfort, or hold applies.

The mode and reason helpers report the **selected decision**, not confirmation that a thermostat accepted it. Check thermostat states and automation traces for command errors. The manager does not itself expire manual cooling or hold: use the optional companion blueprints described in [timed overrides](docs/timed-overrides.md), or your own scripts and automations.

## Get started

1. Copy [`event_hvac_manager.yaml`](blueprints/automation/event_hvac_manager.yaml) to `config/blueprints/automation/readable_hvac/event_hvac_manager.yaml` in your Home Assistant configuration directory. Reload automation blueprints or restart Home Assistant.
2. Create an automation from **Settings → Automations & scenes → Blueprints**. Select the Event HVAC Manager blueprint, your calendar, and one or more compatible climate entities.
3. Review the temperature setpoints, fan mode, pre-cool time, weekly schedule, and check interval. The defaults include weekday office hours; change them to fit your building.
4. Optionally create the control and status helpers described in [helpers](docs/helpers.md), then select them in the blueprint and add controls you want to react promptly to **Controls to watch**. Set up [timed overrides](docs/timed-overrides.md) if needed. Save and enable the automation.
5. Run the automation manually or wait for the next check. Inspect its trace and actual thermostat settings. Test a hold or blocker, a calendar event, and Eco fallback before relying on it. Allow for the check interval when changing inputs.

For a complete example of blueprint inputs, see [the Sanctuary example](examples/sanctuary-example.yaml); replace all entity IDs with your own. See [troubleshooting](docs/troubleshooting.md) and the optional [dashboard example](docs/dashboard.md).

To use the legacy blueprint, copy [`calendar_master_climate_control_legacy.yaml`](blueprints/automation/calendar_master_climate_control_legacy.yaml) into the same blueprint directory and create an automation from it. Its behavior and inputs differ from the newer blueprint.

## Decision priority

The newer blueprint evaluates: admin comfort, hold current, blockers, calendar unavailable, event/pre-cool, Eco override, manual cool, occupancy, office/school hours, then Eco fallback. A higher item wins. During a hold it sends no thermostat commands. Otherwise it checks current targets and fan mode before sending commands to reduce unnecessary calls.

## Contributing

See [the NDWC comparison](docs/ndwc-comparison.md) for what is and is not included from the live installation. See [CONTRIBUTING.md](CONTRIBUTING.md) for validation, reporting issues, and project scope. Licensed under the [MIT License](LICENSE).
