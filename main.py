import psutil
import matplotlib.pyplot as plt
import time


class SystemPerformanceAnalyzer:
    def __init__(self):
        self.cpu_usage = []
        self.memory_usage = []
        self.disk_io_read = []
        self.disk_io_write = []

    def collect_metrics(self):
        cpu_percent = psutil.cpu_percent()
        virtual_memory = psutil.virtual_memory()
        disk_io = psutil.disk_io_counters()

        self.cpu_usage.append(cpu_percent)
        self.memory_usage.append(virtual_memory.percent)
        self.disk_io_read.append(disk_io.read_bytes)
        self.disk_io_write.append(disk_io.write_bytes)

    def visualize_metrics(self):
        plt.figure(figsize=(12, 8))

        plt.subplot(221)
        plt.plot(self.cpu_usage)
        plt.title('CPU Usage')
        plt.xlabel('Time')
        plt.ylabel('Percentage')

        plt.subplot(222)
        plt.plot(self.memory_usage)
        plt.title('Memory Utilization')
        plt.xlabel('Time')
        plt.ylabel('Percentage')

        plt.subplot(223)
        plt.plot(self.disk_io_read, label='Read')
        plt.plot(self.disk_io_write, label='Write')
        plt.title('Disk I/O')
        plt.xlabel('Time')
        plt.ylabel('Bytes')
        plt.legend()

        plt.tight_layout()
        plt.show()


# Example usage
if __name__ == "__main__":
    analyzer = SystemPerformanceAnalyzer()

    # Collect metrics for a certain duration
    for _ in range(50):
        analyzer.collect_metrics()
        time.sleep(1)  # Wait for 1 second between each measurement

    # Visualize collected metrics
    analyzer.visualize_metrics()
