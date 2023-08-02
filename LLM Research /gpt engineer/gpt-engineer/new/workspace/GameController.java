import java.util.Scanner;

public class GameController {
    private SudokuBoard board;
    private InputValidator validator;
    private GameRenderer renderer;

    public GameController() {
        board = new SudokuBoard();
        validator = new InputValidator();
        renderer = new GameRenderer();
    }

    public void startGame() {
        boolean gameFinished = false;
        Scanner scanner = new Scanner(System.in);

        while (!gameFinished) {
            renderer.renderBoard(board);

            System.out.print("Enter row (1-9): ");
            int row = scanner.nextInt();

            System.out.print("Enter column (1-9): ");
            int col = scanner.nextInt();

            System.out.print("Enter value (1-9): ");
            int value = scanner.nextInt();

            if (validator.isValidInput(row, col, value)) {
                board.setCellValue(row - 1, col - 1, value);
                if (board.isBoardFull()) {
                    gameFinished = true;
                    System.out.println("Congratulations! You solved the Sudoku puzzle.");
                }
            } else {
                System.out.println("Invalid input. Please try again.");
            }
        }

        scanner.close();
    }
}
