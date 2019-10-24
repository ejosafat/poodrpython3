from Bicycle03 import Part, Parts


class PartsFactory:
    @staticmethod
    def build(config, part_class=Part, parts_class=Parts):
        return parts_class(
            [part_class(
                name=part_config[0],
                description=part_config[1],
                needs_spare=part_config[2] if len(part_config) == 3 else True
            ) for part_config in config]
        )


road_config = (
    ('chain', '10-speed'),
    ('tire_size', '23'),
    ('tape_color', 'red'),
)

mountain_config = (
    ('chain', '10-speed'),
    ('tire_size', '2.1'),
    ('front_shock', 'Manitou', False),
    ('rear_shock', 'Fox'),
)

road_parts = PartsFactory.build(road_config)
mountain_parts = PartsFactory.build(mountain_config)
print(mountain_parts.parts)
