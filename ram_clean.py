import os
import subprocess

def clear_cache():
    subprocess.run(["sudo", "purge"], capture_output=True)

def get_free_memory():
    vm_stat = subprocess.run(["vm_stat"], capture_output=True, text=True).stdout
    for line in vm_stat.split("\n"):
        if "Pages free" in line:
            free_mem_pages = int(line.split()[2].strip('.'))
            return free_mem_pages * 4096 / (1024 * 1024)  # Convert pages to MB

def main():
    print("Current free memory: {:.2f} MB".format(get_free_memory()))
    print("Clearing cache and purging inactive memory...")
    clear_cache()
    print("Cache cleared.")
    print("New free memory: {:.2f} MB".format(get_free_memory()))

if __name__ == "__main__":
    main()
