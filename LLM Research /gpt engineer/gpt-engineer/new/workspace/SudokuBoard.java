public class SudokuBoard {
    private final int SIZE = 9;
    private Cell[][] board;

    public SudokuBoard() {
        board = new Cell[SIZE][SIZE];
        // Initialize the board with empty cells
        for (int row = 0; row < SIZE; row++) {
            for (int col = 0; col < SIZE; col++) {
                board[row][col] = new Cell();
            }
        }
    }

    // Add methods to manipulate the board state (e.g., setCellValue, getCellValue, etc.)
}
