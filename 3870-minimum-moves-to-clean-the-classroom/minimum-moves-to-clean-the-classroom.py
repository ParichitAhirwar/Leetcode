class Solution:
    def minMoves(self, classroom: List[str], energy: int) -> int:
        m, n = len(classroom), len(classroom[0])

        # Find start and assign an ID to each litter cell.
        sr = sc = -1
        litter_id = [[-1] * n for _ in range(m)]
        litter_count = 0

        for r in range(m):
            for c in range(n):
                if classroom[r][c] == 'S':
                    sr, sc = r, c
                elif classroom[r][c] == 'L':
                    litter_id[r][c] = litter_count
                    litter_count += 1

        full_mask = (1 << litter_count) - 1

        # State = (row, col, collected_mask, remaining_energy)
        queue = deque([(sr, sc, 0, energy)])

        # Using a set avoids allocating a potentially large 4D array.
        visited = {(sr, sc, 0, energy)}

        directions = [
            (-1, 0),
            (1, 0),
            (0, -1),
            (0, 1)
        ]

        moves = 0

        while queue:
            for _ in range(len(queue)):
                r, c, mask, e = queue.popleft()

                # All litter collected.
                if mask == full_mask:
                    return moves

                # Can't make another move with zero energy.
                if e == 0:
                    continue

                for dr, dc in directions:
                    nr, nc = r + dr, c + dc

                    # Outside the classroom.
                    if not (0 <= nr < m and 0 <= nc < n):
                        continue

                    # Obstacle.
                    if classroom[nr][nc] == 'X':
                        continue

                    # Moving costs 1 energy.
                    new_energy = e - 1
                    new_mask = mask

                    # Collect litter.
                    if classroom[nr][nc] == 'L':
                        idx = litter_id[nr][nc]
                        new_mask |= 1 << idx

                    # Reset energy on R.
                    if classroom[nr][nc] == 'R':
                        new_energy = energy

                    state = (nr, nc, new_mask, new_energy)

                    if state not in visited:
                        visited.add(state)
                        queue.append(state)

            moves += 1

        return -1