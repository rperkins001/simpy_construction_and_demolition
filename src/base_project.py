import simpy
from abc import ABC, abstractmethod

class BaseProject(ABC):
    def __init__(self, env, name):
        self.env = env
        self.name = name
        self.resources = {}  # A dictionary to store resources used in the project
        self.modules = []  # A list to store modules (e.g., traffic flow, material processing) used in the project

    def add_resource(self, resource_name, resource):
        """Add a resource to the project."""
        self.resources[resource_name] = resource

    def add_module(self, module):
        """Add a module to the project."""
        self.modules.append(module)

    @abstractmethod
    def run(self):
        """Run the simulation for the project.
        
        This method should be implemented in subclasses and should define the main simulation logic.
        """
        pass

    def setup(self):
        """Set up the initial state of the project.
        
        This method can be overridden in subclasses to set up the initial state of the project,
        such as initializing resources or adding modules.
        """
        # Example setup actions for a construction project
        self.add_resource("workers", 100)
        self.add_resource("trucks", 20)

        # Add modules (e.g., TrafficFlowSimulator or MaterialProcessor) for the project
        # self.add_module(TrafficFlowSimulator(self.env))
        # self.add_module(MaterialProcessor(self.env))

    def update(self):
        """Update the state of the project during the simulation.
        
        This method can be overridden in subclasses to update the state of the project
        as the simulation progresses, such as updating resource allocation or module states.
        """
        # Example update actions for a construction project
        # self.allocate_workers()
        # self.allocate_trucks()

        # Update modules
        for module in self.modules:
            module.update()

    def teardown(self):
        """Clean up the project after the simulation has finished.
        
        This method can be overridden in subclasses to clean up the project
        after the simulation has completed, such as releasing resources or generating reports.
        """
        # Example teardown actions for a construction project
        self.resources.clear()
        self.modules.clear()

        # Generate a report
        # self.generate_report()
        
