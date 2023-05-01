import random

class EnvironmentalImpactAssessor:
    def __init__(self, env, resource_allocator, traffic_simulator, material_processor):
        self.env = env
        self.resource_allocator = resource_allocator
        self.traffic_simulator = traffic_simulator
        self.material_processor = material_processor
        self.noise_impact = 0
        self.air_quality_impact = 0
        self.waste_management_impact = 0
        self.resource_consumption_impact = 0

    def assess_impact(self):
        while True:
            self.noise_impact += random.uniform(0.1, 1) * self.resource_allocator.total_allocated_resources
            self.air_quality_impact += random.uniform(0.1, 1) * self.traffic_simulator.num_vehicles
            self.waste_management_impact += random.uniform(0.1, 1) * self.material_processor.storage.level
            self.resource_consumption_impact += random.uniform(0.1, 1) * sum(resource.capacity for resource in self.resource_allocator.resources.values())


            yield self.env.timeout(1)  # Assess impact every day

    def start(self):
        self.env.process(self.assess_impact())