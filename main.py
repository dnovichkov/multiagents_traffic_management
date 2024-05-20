import logging
from src.utils import get_excel_data
from src.agents.scene import Scene
from src.agents.agents_dispatcher import AgentsDispatcher
from src.entities.traffic_light_entity import TrafficLightEntity
from src.entities.car_entity import CarEntity


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")

    logging.info("Welcome to the traffic management app")

    scene = Scene()
    dispatcher = AgentsDispatcher(scene)

    traffic_lights = get_excel_data('TrafficManagement.xlsx', 'TrafficLights')
    logging.info(f'TrafficLights: {traffic_lights}')
    for tr_light in traffic_lights:
        entity = TrafficLightEntity(tr_light, scene)
        dispatcher.add_entity(entity)

    cars = get_excel_data('TrafficManagement.xlsx', 'Cars')
    logging.info(f'Cars: {cars}')
    for car in cars:
        entity = CarEntity(car, scene)
        dispatcher.add_entity(entity)

    scenario_duration = 600
    time_step = 10
    steps_count = scenario_duration // time_step
    for _ in range(steps_count):
        dispatcher.set_next_time_step(time_step)
