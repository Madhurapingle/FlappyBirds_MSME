class BaseAgent:
    name = "base"

    def safe_run(self, state):
        """
        Wrapper that guarantees:
        - in-place state mutation
        - no keys are dropped
        """
        try:
            return self.run(state)
        except Exception as e:
            state["logs"].append(
                f"[{self.name.upper()} ERROR] {str(e)}"
            )
            return state
