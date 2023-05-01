import simpy

class TrafficFlowSimulator:
    def __init__(self, env, num_entrances, num_exits, entrance_rate, exit_rate, num_vehicles):
        self.env = env
        self.num_entrances = num_entrances
        self.num_exits = num_exits
        self.entrance_rate = entrance_rate
        self.exit_rate = exit_rate
        self.num_vehicles = num_vehicles
        self.entrance_queue = simpy.Resource(env, capacity=num_entrances)
        self.exit_queue = simpy.Resource(env, capacity=num_exits)

    def total_vehicles(self):
        return self.num_vehicles

    def enter_site(self):
        with self.entrance_queue.request() as req:
            yield req
            yield self.env.timeout(self.entrance_rate)
            print(f"Vehicle entered site at {self.env.now:.2f} hours")

    def leave_site(self):
        with self.exit_queue.request() as req:
            yield req
            yield self.env.timeout(self.exit_rate)
            print(f"Vehicle left site at {self.env.now:.2f} hours")