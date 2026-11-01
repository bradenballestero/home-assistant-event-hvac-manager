# Helpers

All helpers are optional for the newer blueprint. Create them in Home Assistant under Settings → Devices & services → Helpers, then select them in the automation. Use one set per zone.

- Two text helpers can display the selected mode and reason. They show the decision, not whether thermostat commands succeeded.
- Input booleans can activate admin comfort, hold current, manual cool, blockers, and Eco override. Blockers and Eco overrides can each contain multiple booleans.
- An occupancy binary sensor can select the occupied mode.

Add control, occupancy, and setpoint helpers to **Controls to watch** for prompt reevaluation; unlisted inputs are evaluated at startup and on the cadence. Optional input-number helpers override the fixed admin, event, office/school, and Eco cool setpoints. Optional input-select and time-only input-datetime helpers can override the comfort fan mode and schedule start/end. Add these to Controls to watch too. For expiring manual cool and hold, see [timed overrides](timed-overrides.md). The optional dashboard contains additional scripts and helpers that are not automatically created.

The priority order is documented in the [README](../README.md#decision-priority).
