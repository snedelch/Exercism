public class LogLevels {

    public static String message(String logLine) {

        int message_start_index = logLine.indexOf(":");
        String new_str = logLine.substring(message_start_index + 1);
        return new_str.trim();

    }

    public static String logLevel(String logLine) {
        if (logLine.indexOf("ERROR") == 1) {
            return "error";
        } else if (logLine.indexOf("WARNING") == 1) {
            return "warning";
        } else if (logLine.indexOf("INFO") == 1) {
            return "info";
        } else {
            return "non of them";
        }
    }

    public static String reformat(String logLine) {
        String reformat_str = message(logLine) + " (" + logLevel(logLine) + ")";
        return reformat_str;

    }
}
