# score_tracker.py

class ScoreTracker:
    def __init__(self):
        """
        A class to track the scores of both players based on the number of discs.
        """
        self.player1_score = 0  # Score for player 1 (Black)
        self.player2_score = 0  # Score for player 2 (White)

    def update_score(self, board):
        """
        Update the scores based on the current state of the board.

        Args:
            board (list): The current game board.
        """
        self.player1_score = sum(row.count(1) for row in board)  # Count of player 1's discs
        self.player2_score = sum(row.count(-1) for row in board)  # Count of player 2's discs

    def get_scores(self):
        """
        Get the current scores of both players.

        Returns:
            tuple: A tuple containing (player1_score, player2_score).
        """
        return self.player1_score, self.player2_score
