def build_ui():
    return {
        'content': '**take an action**',
        'components': [
            {
                'type':1,
                'components': [
                    {
                        'type': 2,
                        'label': 'up!',
                        'style': 1,
                        'custom_id': 'up'
                    },
                    {
                        'type': 2,
                        'label': 'down!',
                        'style': 1,
                        'custom_id': 'down'
                    },
                    {
                        'type': 2,
                        'label': 'show!',
                        'style': 1,
                        'custom_id': 'show'
                    }
                ]
            },
            {
                'type':1,
                'components':[
                    {
                        'type':3,
                        'custom_id': 'select',
                        'options':[
                            {
                                'label': "up!",
                                'value': "up",
                                "description": "make the number 1 bigger",
                            },
                            {
                                'label': "down!",
                                'value': "down",
                                "description": "make the number 1 smaller",
                            },
                        ],
                        'placeholder': 'you know the drill',
                        'min_values': 1,
                        'max_values': 1,
                    }
                ]
            }
        ]
    }