class Solution:
    """Solution class for daily temperatures calculation."""

    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        """Calculate days until a warmer temperature for each day.

        Uses a monotonic stack approach iterating from right to left to
        efficiently determine the number of days until a higher temperature.

        Args:
            temperatures: List of daily temperatures.

        Returns:
            List where each element represents the number of days to wait
            for a warmer temperature. Zero if no warmer day exists.
        """
        stack: list[int] = []
        output: list[int] = [0] * len(temperatures)
        for i in range(len(temperatures) - 1, -1, -1):
            temperature: int = temperatures[i]
            while stack:
                if temperatures[stack[-1]] > temperature:
                    output[i] = stack[-1] - i
                    break
                stack.pop()
            stack.append(i)
        return output
