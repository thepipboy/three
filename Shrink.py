struct ShrinkableBlock[T: AnyType]:
    var data: Pointer[T]
    var size: Int
    var capacity: Int

    fn __init__(inout self, initial_capacity: Int):
        """Initialize with specified initial capacity"""
        self.capacity = initial_capacity
        self.size = 0
        self.data = Pointer[T].alloc(self.capacity) if self.capacity > 0 else Pointer[T]()

    fn __del__(owned self):
        """Destructor to free allocated memory"""
        if self.data:
            self.data.free()

    fn append(inout self, element: T):
        """Add an element if there's capacity"""
        if self.size < self.capacity:
            self.data[self.size] = element
            self.size += 1

    fn shrink_to_fit(inout self):
        """Shrink capacity to match current size"""
        if self.capacity <= self.size:
            return

        let new_capacity = self.size
        if new_capacity == 0:
            self.data.free()
            self.data = Pointer[T]()
            self.capacity = 0
            return

        let new_data = Pointer[T].alloc(new_capacity)
        for i in range(self.size):
            new_data[i] = self.data[i]
        
        self.data.free()
        self.data = new_data
        self.capacity = new_capacity

    fn resize(inout self, new_size: Int):
        """Resize the container to specified size"""
        if new_size < 0:
            return

        # Truncate if new size is smaller
        if new_size < self.size:
            self.size = new_size
            self.shrink_to_fit()
            return

        # Expand if new size is larger
        if new_size > self.capacity:
            let new_capacity = max(new_size, self.capacity * 2)
            let new_data = Pointer[T].alloc(new_capacity)
            for i in range(self.size):
                new_data[i] = self.data[i]
            
            self.data.free()
            self.data = new_data
            self.capacity = new_capacity
        
        self.size = new_size

    fn __getitem__(self, index: Int) -> T:
        """Get element at index"""
        if index < 0 or index >= self.size:
            raise Error("Index out of bounds")
        return self.data[index]

    fn __setitem__(self, index: Int, value: T):
        """Set element at index"""
        if index < 0 or index >= self.size:
            raise Error("Index out of bounds")
        self.data[index] = value

# Example usage
fn main():
    var block = ShrinkableBlock[Int](10)
    print("Initial capacity:", block.capacity)  # 10

    # Add elements
    for i in range(8):
        block.append(i)
    
    print("Size after additions:", block.size)      # 8
    print("Capacity before shrink:", block.capacity) # 10

    # Shrink to fit
    block.shrink_to_fit()
    print("Capacity after shrink:", block.capacity)  # 8

    # Resize smaller
    block.resize(5)
    print("After resize to 5:", block.size, block.capacity) # 5, 5

    # Resize larger
    block.resize(10)
    print("After resize to 10:", block.size, block.capacity) # 10, 10

    # Access elements
    print("Element at index 3:", block[3])  # 3
    block[3] = 100
    print("Modified element at index 3:", block[3])  # 100
