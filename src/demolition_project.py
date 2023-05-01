import simpy
from .base_project import BaseProject
from .resource_allocation import ResourceAllocator
from .equipment_utilization import generate_equipment
from .traffic_flow import TrafficFlowSimulator
from .material_processing import MaterialProcessor
from .environmental_impact import EnvironmentalImpactAssessor

class DemolitionProject(BaseProject):
    def __init__(self, env, name, num_workers, num_trucks, equipment_specs, traffic_flow_specs, processing_time_range, storage_capacity):
        super().__init__(env, name)
        self.num_workers = num_workers
        self.num_trucks = num_trucks
        self.equipment_specs = equipment_specs
        self.traffic_flow_specs = traffic_flow_specs
        self.traffic_simulator = None
        self.processing_time_range = processing_time_range
        self.storage_capacity = storage_capacity
        self.material_processor = None
        self.environmental_impact_assessor = None

    def setup(self):
        super().setup()
        # Set up resources specific to the demolition project
        self.resources["workers"] = simpy.Resource(self.env, capacity=self.num_workers)
        self.resources["trucks"] = simpy.Resource(self.env, capacity=self.num_trucks)
        self.resources["fuel_station"] = simpy.Resource(self.env, capacity=1)  # Add fuel station resource
        self.resource_allocator = ResourceAllocator(self.resources)
        self.traffic_simulator = TrafficFlowSimulator(self.env, **self.traffic_flow_specs)
        self.equipment_list = generate_equipment(self.env, self.equipment_specs, self.resources["fuel_station"])
        self.material_processor = MaterialProcessor(self.env, self.equipment_list, self.processing_time_range, self.storage_capacity)
        self.material_processor.start()
        self.environmental_impact_assessor = EnvironmentalImpactAssessor(self.env, self.resource_allocator, self.traffic_simulator, self.material_processor)
        self.environmental_impact_assessor.start()

    def run(self):
        """Run the simulation for the demolition project."""
        print(f"Starting demolition project: {self.name}")

        # Run the project for a specified number of days (e.g., 30 days)
        num_days = 30
        hours_per_day = 8

        for day in range(num_days):
            print(f"Day {day}:")
            # Execute daily tasks, like allocating workers and trucks
            yield self.env.process(self.daily_tasks(day))

        total_simulation_time = num_days * hours_per_day
        yield self.env.timeout(total_simulation_time)

        print(f"Demolition project {self.name} completed.")

    def daily_tasks(self, day):
        # Implement daily tasks for the demolition project
        print(f"Allocating workers and trucks for day {day}")

        workers_request = self.resource_allocator.allocate_resources("workers", 8)
        trucks_request = self.resource_allocator.allocate_resources("trucks", 4)

        yield workers_request & trucks_request
        yield self.env.timeout(8)  # Simulate 8 hours of work
        print(f"Day {day} completed.")

        self.resource_allocator.release_resources(workers_request)
        self.resource_allocator.release_resources(trucks_request)