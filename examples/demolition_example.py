import simpy
from src.demolition_project import DemolitionProject

def main():
    env = simpy.Environment()

    equipment_specs = [
        {'type': 'excavator', 
         'num': 10, 
         'fuel_capacity': 100,
         'fuel_usage_rate': 5,
         'capacity': 20,
         'power': 100,
         'maintenance_duration': 30}, 
        {'type': 'dump truck',
         'num': 5,
         'fuel_capacity': 50,
         'fuel_usage_rate': 3,
         'capacity': 10,
         'power': 50,
         'maintenance_duration': 20
         }
        ]
    traffic_flow_specs = {
        'num_entrances': 1,
        'num_exits': 1,
        'entrance_rate': 60,  # vehicles per hour
        'exit_rate': 60,  # vehicles per hour
        'num_vehicles': 3
        }
    
    processing_time_range = (10, 20)
    storage_capacity = 100


    demolition_project = DemolitionProject(env, "Building demolition", num_workers=30, num_trucks=5, 
                                           equipment_specs=equipment_specs, traffic_flow_specs=traffic_flow_specs,
                                           processing_time_range=processing_time_range, storage_capacity=storage_capacity)
    demolition_project.setup()
    env.process(demolition_project.run())
    env.run()

if __name__ == "__main__":
    main()