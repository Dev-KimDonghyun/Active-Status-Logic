import psutil

cpuTread = psutil.cpu_count() # CPU Logical Core
cpuCore = psutil.cpu_count(logical = False) # CPU Physical Core
cpuOperation = psutil.cpu_percent(interval = 0.1, percpu = False) # CPU Rate Of Operation
totalMemory = round((psutil.virtual_memory().total) / (1024 ** 3)) # Total Memory Stroage (Gigabyte)
memoryOperation = (psutil.virtual_memory().percent) # Memory Rate Of Operation

print(f'This CPU of PC has {cpuTread} logical core, {cpuCore} physical core, {totalMemory}GB Memory.\nAnd CPU Rate Of Operation is {cpuOperation}%, Memory Rate Of Operation is {memoryOperation}%.')