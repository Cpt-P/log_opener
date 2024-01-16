import java.io.*;
import java.nio.file.*;
import java.util.*;
import java.awt.datatransfer.*;
import java.awt.Toolkit;

public class LogOpener {
    private static Scanner scanner = new Scanner(System.in);
    private static String[] logPaths = {"%appdata%/.minecraft/sklauncher/sklauncher_logs.txt",
                                       "%appdata%/.minecraft/logs/latest.log",
                                       "%appdata%/.minecraft/crash-reports/crash-<date>.txt"};
    private static File logFile;
    private static PrintWriter logWriter;
    private static Clipboard clipboard = Toolkit.getDefaultToolkit().getSystemClipboard();

    public static void main(String[] args) {
        logFile = new File("log_" + new Date().toString().replace(" ", "_").replace(":", "_") + ".txt");
        try {
            logFile.createNewFile();
            logWriter = new PrintWriter(new FileWriter(logFile));
            logWriter.println("LogOpener started at " + new Date());
        } catch (IOException e) {
            System.out.println("Error creating or writing to the log file: " + e.getMessage());
            e.printStackTrace();
            System.exit(1);
        }

        System.out.println("Welcome to LogOpener, a simple Java program to open Minecraft logs and crash reports.");
        System.out.println("Please choose one of the following options:");
        System.out.println("1. Open the launcher log");
        System.out.println("2. Open the latest game log");
        System.out.println("3. Open the latest crash report");
        System.out.println("4. Exit the program");

        while (true) {
            System.out.print("Enter your choice (1-4): ");
            String input = scanner.nextLine();
            logWriter.println("User input: " + input);
            switch (input) {
                case "1": openLog(0); break;
                case "2": openLog(1); break;
                case "3": openLog(2); break;
                case "4": exitProgram(); break;
                default: System.out.println("Invalid input. Please enter a number between 1 and 4."); break;
            }
        }
    }

    private static void openLog(int index) {
        try {
            String filePath = logPaths[index];
            filePath = filePath.replace("%appdata%", System.getenv("APPDATA"));
            if (index == 2) filePath = replaceDate(filePath);
            File file = new File(filePath);
            if (file.exists()) {
                String content = new String(Files.readAllBytes(file.toPath()));
                clipboard.setContents(new StringSelection(content), null);
                System.out.println("The file content has been copied to the clipboard.");
                logWriter.println("The file content has been copied to the clipboard.");
            } else {
                System.out.println("The file does not exist: " + filePath);
                logWriter.println("The file does not exist: " + filePath);
            }
        } catch (IOException e) {
            System.out.println("Error opening or reading the file: " + e.getMessage());
            e.printStackTrace();
            logWriter.println("Error opening or reading the file: " + e.getMessage());
        }
    }

    private static String replaceDate(String filePath) {
        try {
            File dir = new File(filePath).getParentFile();
            if (dir.exists()) {
                File[] files = dir.listFiles();
                if (files != null && files.length > 0) {
                    Arrays.sort(files, (f1, f2) -> Long.compare(f2.lastModified(), f1.lastModified()));
                    String fileName = files[0].getName();
                    String date = fileName.substring(6, fileName.indexOf('-'));
                    filePath = filePath.replace("<date>", date);
                }
            }
        } catch (Exception e) {
            System.out.println("Error replacing the date: " + e.getMessage());
            e.printStackTrace();
            logWriter.println("Error replacing the date: " + e.getMessage());
        }
        return filePath;
    }

    private static void exitProgram() {
        System.out.println("Thank you for using LogOpener. Goodbye!");
        logWriter.println("Thank you for using LogOpener. Goodbye!");
        logWriter.println("LogOpener ended at " + new Date());
        logWriter.close();
        scanner.close();
        System.exit(0);
    }
}
