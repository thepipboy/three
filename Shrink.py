def has_diagonal_structure(matrix, block_id):
    """
    Checks if a 2D grid contains a diagonal structure
    Input: 2D array (block grid), block ID to check
    Returns: True if main diagonal contains specified block
    """
    size = min(len(matrix), len(matrix[0]))
    
    for i in range(size):
        # Check main diagonal
        if matrix[i][i] != block_id:
            return False
    
    return True

# Example usage (check for nether portal frame)
portal_frame = [
    [0, 0, 0, 0],
    [0, 1, 0, 0],
    [0, 0, 1, 0],
    [0, 0, 0, 1]
]

is_portal = has_diagonal_structure(portal_frame, 1)  # 1 = Obsidian
print("Valid portal frame" if is_portal else "Invalid frame")