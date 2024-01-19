
def add_box(log: str, symbol: str = '#', line_length: int = 79):
    """
    :param log: Message to be logged
    :param symbol: Any symbol to be used for the box such as #,$,@,= or alphanumberic
    :param line_length: length of the log lines
    :return: str
    """
    log_str = "\n"
    log_str += line_length * symbol
    log_str += "\n"
    if log:
        log_split = log.split("\n")
        for lg in log_split:
            logs_list = [lg[i: i + line_length-4] for i in range(0, len(lg), line_length-4)]
            for ll in logs_list:
                log_str += symbol+" "
                log_str += ll.ljust(line_length-4)
                log_str += " "+symbol+ "\n"
    log_str += line_length * symbol
    log_str += "\n"
    return log_str

if __name__ == "__main__":
    print(add_box("log str"))
