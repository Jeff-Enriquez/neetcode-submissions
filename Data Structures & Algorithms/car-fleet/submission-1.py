class Solution:
    """Solution class for calculating car fleets arriving at a target."""

    # Time Complexity: O(nlogn)
    # Space Complexity: O(n)
    def carFleet(self, target: int, position: list[int], speed: list[int]) -> int:
        """Calculates the number of car fleets that will arrive at the target.
        
        A car fleet is formed when faster cars behind catch up to slower cars
        ahead. Cars cannot pass each other.

        Args:
            target: The destination position.
            position: List of starting positions for each car.
            speed: List of speeds for each car.

        Returns:
            The number of car fleets that will arrive at the target.
        """
        
        pos_speed: list[tuple[int,int]] = []
        for i in range(len(position)):
            pos_speed.append((position[i], speed[i]))
        pos_speed.sort(reverse=True)

        hours: list[int] = []
        for ps in pos_speed:
            hours.append((target - ps[0]) / ps[1])
        
        result: int = 0
        hour_of_last_fleet: int = -1
        for hour in hours:
            if hour > hour_of_last_fleet:
                result += 1
                hour_of_last_fleet = hour

        return result
