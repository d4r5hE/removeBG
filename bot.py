import subprocess
import resource
import sys

def main():
    subprocess.run("pip install numpy --no-cache-dir",shell=True)
    subprocess.run("pip install opencv-python --no-cache-dir", shell=True)
    subprocess.run("pip install torch --no-cache-dir", shell=True)
    subprocess.run("pip install torchvision --no-cache-dir",shell=True)
    subprocess.run("pip install Flask --no-cache-dir",shell=True)
    subprocess.run("apt-get update && apt-get install -y python3-opencv",shell=True)
    subprocess.run("apt-get update",shell=True)
    subprocess.run("apt install -y libgl1-mesa-glx",shell=True)
    subprocess.run("apt update && apt install -y libsm6 libxext6 ffmpeg libfontconfig1 libxrender1 libgl1-mesa-glx",shell=True)
    subprocess.run("pip install -r requirment.txt --no-cache-dir",shell=True)
    subprocess.run("python app.py",shell=True)


def memory_limit():
    soft, hard = resource.getrlimit(resource.RLIMIT_AS)
    resource.setrlimit(resource.RLIMIT_AS, (get_memory() * 1024 / 2, hard))

def get_memory():
    with open('/proc/meminfo', 'r') as mem:
        free_memory = 0
        for i in mem:
            sline = i.split()
            if str(sline[0]) in ('MemFree:', 'Buffers:', 'Cached:'):
                free_memory += int(sline[1])
    return free_memory

if __name__ == '__main__':
    memory_limit() # Limitates maximun memory usage to half
    try:
        main()
    except MemoryError:
        sys.stderr.write('\n\nERROR: Memory Exception\n')
        sys.exit(1)
