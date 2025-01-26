DEFAULTS = {
    'label': "{icon}",
    'label_alt': "Brightness {percent}%",
    'tooltip': True,
    'brightness_icons': [
        "\udb80\udcde",  # Icon for 0-25% brightness
        "\udb80\udcdd",  # Icon for 26-50% brightness
        "\udb80\udcdf",  # Icon for 51-75% brightness
        "\udb80\udce0"   # Icon for 76-100% brightness
    ],
    'brightness_toggle_level': [],
    'brightness_menu': {
        'blur': True,
        'round_corners': True,
        'round_corners_type': 'normal',
        'border_color': 'System',
        'alignment': 'right',
        'direction': 'down',
        'distance': 6
    },
    'hide_unsupported': True,
    'auto_light': False,
    'auto_light_icon': "\udb80\udce1",
    'auto_light_night_level': 50,
    'auto_light_night_start_time': "20:00",
    'auto_light_night_end_time': "06:30",
    'auto_light_day_level': 100,
    'container_padding': {'top': 0, 'left': 0, 'bottom': 0, 'right': 0},
    'animation': {
        'enabled': True,
        'type': 'fadeInOut',
        'duration': 200
    },
    'callbacks': {
        'on_left': 'toggle_label',
        'on_middle': 'do_nothing',
        'on_right': 'do_nothing'
    },
}

VALIDATION_SCHEMA = {
    'label': {
        'type': 'string',
        'default': DEFAULTS['label']
    },
    'label_alt': {
        'type': 'string',
        'default': DEFAULTS['label_alt']
    },
    'tooltip': {
        'type': 'boolean',
        'required': False,
        'default': DEFAULTS['tooltip']
    },
    'brightness_icons': {
        'type': 'list',
        'default': DEFAULTS['brightness_icons'],
        "schema": {
            'type': 'string',
            'required': False
        }
    },
    'brightness_toggle_level': {
        'type': 'list',
        'default': DEFAULTS['brightness_toggle_level'],
        "schema": {
            'type': 'integer',
            'required': False
        }
    },
    'brightness_menu': {
        'type': 'dict',
        'required': False,
        'schema': {
            'blur': {
                'type': 'boolean',
                'default': DEFAULTS['brightness_menu']['blur']
            },
            'round_corners': {
                'type': 'boolean',
                'default': DEFAULTS['brightness_menu']['round_corners']
            },
            'round_corners_type': {
                'type': 'string',
                'default': DEFAULTS['brightness_menu']['round_corners_type']
            },
            'border_color': {
                'type': 'string',
                'default': DEFAULTS['brightness_menu']['border_color']
            },
            'alignment': {
                'type': 'string',
                'default': DEFAULTS['brightness_menu']['alignment']
            },
            'direction': {
                'type': 'string',
                'default': DEFAULTS['brightness_menu']['direction']
            },
            'distance': {
                'type': 'integer',
                'default': DEFAULTS['brightness_menu']['distance']
            }
        },
        'default': DEFAULTS['brightness_menu']
    },
    'hide_unsupported': {
        'type': 'boolean',
        'required': False,
        'default': DEFAULTS['hide_unsupported']
    },
    'auto_light': {
        'type': 'boolean',
        'required': False,
        'default': DEFAULTS['auto_light']
    },
    'auto_light_icon': {
        'type': 'string',
        'required': False,
        'default': DEFAULTS['auto_light_icon']
    },
    'auto_light_night_level': {
        'type': 'integer',
        'required': False,
        'default': DEFAULTS['auto_light_night_level']
    },
    'auto_light_night_start_time': {
        'type': 'string',
        'required': False,
        'default': DEFAULTS['auto_light_night_start_time']
    },
    'auto_light_night_end_time': {
        'type': 'string',
        'required': False,
        'default': DEFAULTS['auto_light_night_end_time']
    },
    'auto_light_day_level': {
        'type': 'integer',
        'required': False,
        'default': DEFAULTS['auto_light_day_level']
    },
    'container_padding': {
        'type': 'dict',
        'required': False,
        'schema': {
            'top': {
                'type': 'integer',
                'default': DEFAULTS['container_padding']['top']
            },
            'left': {
                'type': 'integer',
                'default': DEFAULTS['container_padding']['left']
            },
            'bottom': {
                'type': 'integer',
                'default': DEFAULTS['container_padding']['bottom']
            },
            'right': {
                'type': 'integer',
                'default': DEFAULTS['container_padding']['right']
            }
        },
        'default': DEFAULTS['container_padding']
    },
    'animation': {
        'type': 'dict',
        'required': False,
        'schema': {
            'enabled': {
                'type': 'boolean',
                'default': DEFAULTS['animation']['enabled']
            },
            'type': {
                'type': 'string',
                'default': DEFAULTS['animation']['type']
            },
            'duration': {
                'type': 'integer',
                'default': DEFAULTS['animation']['duration']
            }
        },
        'default': DEFAULTS['animation']
    },
    'callbacks': {
        'type': 'dict',
        'schema': {
            'on_left': {
                'type': 'string',
                'default': DEFAULTS['callbacks']['on_left'],
            },
            'on_middle': {
                'type': 'string',
                'default': DEFAULTS['callbacks']['on_middle'],
            },
            'on_right': {
                'type': 'string',
                'default': DEFAULTS['callbacks']['on_right'],
            }
        },
        'default': DEFAULTS['callbacks']
    }
}
