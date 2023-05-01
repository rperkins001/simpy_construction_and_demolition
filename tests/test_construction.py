import simpy
from src.construction_project import ConstructionProject


def test_construction_project():
    env = simpy.Environment()
    name = "Test Construction Project"
    num_workers = 100
    num_trucks = 20
    equipment_specs = [# Define equipment specifications
    {
        "type": "excavator",
        "num": 2,
        "fuel_capacity": 200,
        "fuel_usage_rate": 5,
        "capacity": 100,
        "power": 300,
        "maintenance_duration": 4  # Add maintenance_duration (in hours, for example)
    },
    {
        "type": "crane",
        "num": 1,
        "fuel_capacity": 150,
        "fuel_usage_rate": 4,
        "capacity": 50,
        "power": 200,
        "maintenance_duration": 6  # Add maintenance_duration (in hours, for example)
    }
    ]  
    traffic_flow_specs = {# Define traffic flow specifications  
        "num_entrances": 2,
        "num_exits": 2,
        "entrance_rate": 5,
        "exit_rate": 5,
        "num_vehicles": 10
    }  
    
    processing_time_range = (1, 3)
    storage_capacity = 1000

    project = ConstructionProject(env, name, num_workers, num_trucks, equipment_specs, traffic_flow_specs, processing_time_range, storage_capacity)
    project.setup()
    simulation_time = 30* 8
    env.run(until=simulation_time)  # pass project.run() directly to env.run()

test_construction_project()
