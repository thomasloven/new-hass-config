vacuum = "vacuum.xiaomi_vacuum_cleaner"
zones = {
        "hallen": 24,
        "koket": 22,
        "vardagsrummet": 23,
        "sovrum": 17,
        "kontoret": 16,
        "barnrum": 1,
        }
# 18: Tröskel mellan kök och hall
# 19: Tröskel mellan hall och vardagsrum
# 20: Tvättstuga

# vacuum = data.entity_id
# zones = data.zones


toClean = []
for k,v in zones.items():
    if hass.states.is_state(f'input_boolean.dammsug_{k}', 'on'):
        toClean.append(v)


hass.services.call( "vacuum", "send_command", {
    "entity_id": "vacuum.xiaomi_vacuum_cleaner",
    "command": "app_segment_clean",
    "params": toClean,
    })
