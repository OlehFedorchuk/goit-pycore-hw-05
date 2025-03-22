import sys

def parse_log_line(line: str) -> dict:
    """Parses a log line into a dictionary with keys: date, time, level, message."""
    parts = line.split(" ", 3)
    if len(parts) < 4:
        return None 
    return {"date": parts[0], "time": parts[1], "level": parts[2], "message": parts[3]}

def load_logs(file_path: str) -> list:
    """Loads logs from a file and returns a list of parsed entries."""
    logs = []
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            logs = [parse_log_line(line.strip()) for line in file if parse_log_line(line.strip())]
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        sys.exit(1)
    except Exception as e:
        print(f"File read error: {e}")
        sys.exit(1)
    return logs

def filter_logs_by_level(logs: list, level: str) -> list:
    """Filters logs by a given log level (e.g., ERROR, INFO)."""
    return [log for log in logs if log["level"].lower() == level.lower()]

def count_logs_by_level(logs: list) -> dict:
    """Counts the number of log entries for each log level."""
    log_counts = {}
    for log in logs:
        log_counts[log["level"]] = log_counts.get(log["level"], 0) + 1
    return log_counts

def display_log_counts(counts: dict):
    """Formats and displays the log count as a table."""
    print("\nLog Level       | Count")
    print("----------------|------")
    for level in ["INFO", "DEBUG", "ERROR", "WARNING"]:
        print(f"{level.ljust(16)}| {counts.get(level, 0)}")

def display_filtered_logs(logs: list, level: str):
    """Displays detailed log entries for a specific log level."""
    print(f"\nLog details for level '{level.upper()}':")
    for log in logs:
        print(f"{log['date']} {log['time']} - {log['message']}")

def main():
    """Main function to handle arguments and execute log analysis."""
    if len(sys.argv) < 2:
        print("Usage: python main.py /path/to/logfile.log [log_level]")
        sys.exit(1)

    file_path = sys.argv[1]
    log_level = sys.argv[2] if len(sys.argv) > 2 else None

    logs = load_logs(file_path)
    log_counts = count_logs_by_level(logs)

    display_log_counts(log_counts)

    if log_level:
        filtered_logs = filter_logs_by_level(logs, log_level)
        if filtered_logs:
            display_filtered_logs(filtered_logs, log_level)
        else:
            print(f"\nNo log entries found for level '{log_level.upper()}'.")

if __name__ == "__main__":
    main()