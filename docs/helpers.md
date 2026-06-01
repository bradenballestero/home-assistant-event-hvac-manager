# Helper Entities

The automation works best when the important controls are helpers instead of hidden hard-coded values.

## Recommended Helpers

Use these per HVAC zone:

- `input_text.<zone>_hvac_effective_mode`
- `input_text.<zone>_hvac_effective_reason`
- `input_boolean.<zone>_hvac_admin_comfort_lock`
- `input_boolean.<zone>_hvac_hold_current`
- `input_boolean.<zone>_hvac_manual_cool_active`

Optional but useful:

- `timer.<zone>_hvac_manual_cool`
- `timer.<zone>_hvac_hold_current`
- `input_select.<zone>_hvac_manual_cool_duration`
- `input_datetime.<zone>_hvac_manual_cool_until`
- `input_datetime.<zone>_hvac_hold_current_until`
- `input_number.<zone>_hvac_event_cool_setpoint`
- `input_number.<zone>_hvac_eco_cool_setpoint`
- `input_select.<zone>_hvac_comfort_fan_mode`

## Why Helpers Matter

Helpers make the automation readable.

Instead of guessing why the thermostat changed, someone can check:

```text
Effective Mode: Event
Effective Reason: Calendar event or pre-cool window is active.
```

That is useful for humans first. It also gives an AI assistant a safe, narrow control panel.

## Suggested Priority Order

1. Blockers
2. Admin Comfort
3. Hold Current
4. Calendar event or pre-cool
5. Eco override
6. Manual Cool
7. Occupancy
8. Office/school schedule
9. Eco fallback
