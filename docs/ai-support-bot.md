# AI Support Bot Safety Pattern

This project does not require AI. The automation should work normally by itself.

If an AI assistant is added later, keep it on a short leash.

## Good Pattern

The assistant may:

- read thermostat state
- read calendar state
- read helper state
- explain the active mode and reason
- change approved HVAC helper entities
- start approved timers

The assistant should not:

- directly control unrelated lights, locks, doors, cameras, or audio gear
- directly call arbitrary Home Assistant services
- set temperatures outside configured limits
- create permanent overrides without a human confirming

## Example Request

User says:

```text
It is hot in the Sanctuary.
```

Assistant checks:

- current temperature
- current HVAC mode
- current setpoints
- active event/pre-cool state
- blockers
- Admin Comfort
- Manual Cool
- Hold Current
- recent errors

Then it replies with something like:

```text
The Sanctuary is 75 F and currently in Eco because no event or occupancy is active.
I turned on Manual Cool for 90 minutes. The automation will return to normal after that.
```

## Principle

The assistant should request intent through helpers. The automation should remain the source of truth.
