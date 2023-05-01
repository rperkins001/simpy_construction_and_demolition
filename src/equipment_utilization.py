import simpy
import random

class ConstructionEquipment:
    def __init__(self, env, equipment_id, equipment_type, fuel_capacity, fuel_usage_rate, fuel_station, capacity, power, maintenance_duration):
        self.env = env
        self.equipment_id = equipment_id
        self.equipment_type = equipment_type
        self.fuel_capacity = fuel_capacity
        self.fuel_level = fuel_capacity
        self.fuel_usage_rate = fuel_usage_rate
        self.fuel_station = fuel_station
        self.capacity = capacity
        self.power = power
        self.maintenance_duration = maintenance_duration
        self.broken = False

        self.env.process(self.operate())

    def operate(self):
        while True:
            # Simulate the actual operation of the equipment
            yield self.env.timeout(random.uniform(1, 5))
            self.fuel_level -= self.fuel_usage_rate

            if self.fuel_level <= 0.1 * self.fuel_capacity:
                self.env.process(self.refuel())

            if random.random() < 0.01:  # 1% chance of equipment malfunction
                self.broken = True
                self.env.process(self.maintenance())

    def refuel(self):
        print(f"Equipment {self.equipment_id} refueling...")
        with self.fuel_station.request() as req:
            yield req
            yield self.env.timeout(1)  # Simulate refueling time
            self.fuel_level = self.fuel_capacity

    def maintenance(self):
        print(f"Equipment {self.equipment_id} undergoing maintenance...")
        yield self.env.timeout(self.maintenance_duration)
        self.broken = False
        print(f"Equipment {self.equipment_id} maintenance completed.")

def generate_equipment(env, equipment_specs, fuel_station):
    equipment_list = []
    for equipment_spec in equipment_specs:
        equipment_type = equipment_spec["type"]
        num_equipment = equipment_spec["num"]
        fuel_capacity = equipment_spec["fuel_capacity"]
        fuel_usage_rate = equipment_spec["fuel_usage_rate"]
        capacity = equipment_spec["capacity"]
        power = equipment_spec["power"]
        maintenance_duration = equipment_spec["maintenance_duration"]

        for i in range(num_equipment):
            equipment = ConstructionEquipment(env, i, equipment_type, fuel_capacity, fuel_usage_rate, fuel_station, capacity, power, maintenance_duration)
            equipment_list.append(equipment)

    return equipment_list