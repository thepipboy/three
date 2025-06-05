def generate_cubic_chunks(world_size):
    """
    Generates a cubic chunk Minecraft world (16x16x16 chunks)
    Each chunk is a 3D numpy array (16x16x16 blocks)
    """
    import numpy as np
    
    # Create empty world dictionary (chunk coordinates as keys)
    world = {}
    
    # Generate chunks in all three dimensions
    for x in range(world_size):
        for y in range(world_size):
            for z in range(world_size):
                # Create empty chunk (air blocks = 0)
                chunk = np.zeros((16, 16, 16), dtype=np.uint8)
                
                # Add bedrock at bottom layer (y=0)
                if y == 0:
                    chunk[:, :, 0] = 7  # Bedrock ID
                
                # Store chunk in world
                world[(x, y, z)] = chunk
    
    print(f"Generated {world_size}x{world_size}x{world_size} cubic world")
    return world

# Generate a 4x4x4 chunk cubic world
minecraft_world = generate_cubic_chunks(4)