# Troubleshooting

## Thermostats Flip Between Event and Eco

Likely cause: the calendar briefly becomes `unavailable` during a reload.

Fix pattern:

- Do not trigger directly on calendar state changes.
- Use calendar `start_time` and `end_time` attributes.
- Treat `unavailable` as "hold current," not "no event."

## One Thermostat Updates and the Other Does Not

Likely cause: cloud thermostat state lag.

Fix pattern:

- Check all thermostats before commanding.
- Command each out-of-line thermostat independently.
- If all thermostats already match, send no command.

## Honeywell Timeout Warnings

Honeywell cloud thermostats can be slow. The newer blueprint checks current targets and fan mode before sending commands, which can reduce unnecessary calls. Command errors can still occur and should be checked in the automation trace.

Good signs:

- Recent automation traces finish cleanly.
- Thermostats agree on mode and setpoints.
- Repeated cadence runs skip thermostat commands when already correct.

Bad signs:

- The automation sends commands every cadence even when nothing changed.
- The same room has mismatched setpoints for a long time.
- Errors happen at the same time as real desired mode changes.

## Duplicate Runs at Schedule Boundaries

If a time pattern runs every 15 minutes and a schedule edge is also exactly on a 15-minute boundary, the automation can run twice in the same minute.

Usually this is harmless, but it can create duplicate cloud thermostat commands. Prefer one of these:

- rely on the cadence only
- move explicit schedule-edge triggers off the cadence minute
- keep the thermostat command guard so duplicate runs skip when already correct

The included reusable blueprint uses startup plus cadence only for this reason.

## A Control Does Not Take Effect Right Away

The newer blueprint evaluates watched controls on state changes, and all inputs at startup and on its configured cadence. Add the control to Controls to watch, or wait for the next check, then inspect the trace. A mode or reason helper reports the selected decision, not confirmation that the thermostat accepted a command.

## Manual Cool Does Not Expire

The manager does not itself turn off the manual cool boolean. Configure the companion [timed override blueprints](timed-overrides.md), or turn it off manually.
