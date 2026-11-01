# Timed manual cool and hold

These optional companion blueprints provide a timed override for a single zone. Create separate instances and helpers for manual cool and for hold. They are newly extracted patterns and have not yet been tested in a Home Assistant runtime.

1. Create an input boolean, a timer, and an input datetime with both date and time enabled. Select the boolean as the manager's Manual cool or Hold current input, and add it to Controls to watch.
2. Copy `blueprints/script/timed_hvac_override.yaml` to `config/blueprints/script/readable_hvac/timed_hvac_override.yaml` and `blueprints/automation/timed_hvac_override_expiry.yaml` to `config/blueprints/automation/readable_hvac/timed_hvac_override_expiry.yaml`.
3. Create a script from **Start timed HVAC override**, selecting the three helpers and a duration. Create an automation from **Expire timed HVAC override**, selecting the same helpers. Enable both the manager and expiry automation.
4. Run the script to start or restart the override. To end it early, turn the boolean off and cancel the timer. The expiry automation checks on timer changes, startup, and each minute. If the timer is no longer active and the saved expiration has passed, it turns the boolean off. The manager reevaluates when the boolean changes if it is watched.
5. Test starting, stopping, expiry and restart recovery, and inspect traces before relying on the override. A hold prevents new commands only once the manager processes it; it cannot retract an already-running call.

The script uses a fixed duration configured in the blueprint. Unlike the church's live setup, it does not include a dashboard duration selector, synchronization of changes while active, or admin-lock warnings. Those require separate automations.
