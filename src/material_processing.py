import simpy
import random

class MaterialProcessor:
    def __init__(self, env, equipment_list, processing_time_range, storage_capacity):
        self.env = env
        self.equipment_list = equipment_list
        self.processing_time_range = processing_time_range
        self.storage_capacity = storage_capacity
        self.storage = simpy.Container(self.env, capacity=self.storage_capacity)

    def process_materials(self):
        while True:
            processing_equipment = random.choice(self.equipment_list)
            if not processing_equipment.broken:
                processing_time = random.uniform(*self.processing_time_range)
                yield self.env.timeout(processing_time)
                processed_materials = processing_equipment.capacity
                yield self.storage.put(processed_materials)
                print(f"{processed_materials} units of material processed by equipment {processing_equipment.equipment_id}")

    def start(self):
        self.env.process(self.process_materials())

