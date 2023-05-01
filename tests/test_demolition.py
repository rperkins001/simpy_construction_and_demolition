import simpy
from src.demolition_project import DemolitionProject

def test_demolition_project():
    env = simpy.Environment()
    name = "Test Demolition Project"
    num_workers = 50
    num_trucks = 10
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
        "maintenance_duration": 4  # Add maintenance_duration (in hours, for example)
    }
    ]  
    traffic_flow_specs = {
        "num_entrances": 2,
        "num_exits": 2,
        "entrance_rate": 5,
        "exit_rate": 5,
        "num_vehicles": 10
    }
    processing_time_range = (1, 3)
    storage_capacity = 500

    project = DemolitionProject(env, name, num_workers, num_trucks, equipment_specs, traffic_flow_specs, processing_time_range, storage_capacity)
    project.setup()
    simulation_time = 30*4
    env.run(until=simulation_time)

test_demolition_project()
