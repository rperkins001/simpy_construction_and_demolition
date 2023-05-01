class ResourceAllocator:
    def __init__(self, resources):
        self.resources = resources
        self.total_allocated_resources = 0

    def allocate_resources(self, resource_type, num_resources):
        if resource_type not in self.resources:
            raise ValueError(f"Invalid resource type: {resource_type}")

        resource = self.resources[resource_type]
        req = resource.request()

        # Update the total_allocated_resources attribute
        self.total_allocated_resources += num_resources

        return req

    def release_resources(self, request):
        request.resource.release(request)

        # Update the total_allocated_resources attribute
        self.total_allocated_resources -= 1
