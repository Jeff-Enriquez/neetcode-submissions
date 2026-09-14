class Solution:
    """Solver for Reverse Polish Notation evaluation problems."""

    def evalRPN(self, tokens: list[str]) -> int:  # pylint: disable=invalid-name
        """Evaluate a Reverse Polish Notation expression.

        Args:
            tokens: A list of strings representing the RPN expression.
                Each element is either an integer or an operator (+, -, *, /).

        Returns:
            The integer result of evaluating the expression.
        """
        stack: list[int] = []
        for token in tokens:
            if token in "+-*/":
                num2: int = stack.pop()
                num1: int = stack.pop()
                if token == "+":
                    stack.append(num1 + num2)
                elif token == "-":
                    stack.append(num1 - num2)
                elif token == "*":
                    stack.append(num1 * num2)
                else:
                    stack.append(int(num1 / num2))
            else:
                stack.append(int(token))
        return stack.pop()
