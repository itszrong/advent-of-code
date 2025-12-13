import java.io.*;
import java.util.*;

public class Day1P2 {
    public static void main(String[] args) {
        try {
            File file = new File("data_ex.txt");
            Scanner scanner = new Scanner(file);

            while (scanner.hasNextLine()) {
                String line = scanner.nextLine();
                System.out.println(line);
            }

            scanner.close();
        } catch (FileNotFoundException e) {
            System.err.println("Error reading file: " + e.getMessage());
        }
    }
}
