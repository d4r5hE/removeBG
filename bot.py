import subprocess
import resource
import sys

def main():
    subprocess.run("pip install rembg --no-cache-dir",shell=True)
    subprocess.run("pip install numpy==1.20 --no-cache-dir",shell=True)
    subprocess.run("curl -O https://repo.anaconda.com/archive/Anaconda3-2019.03-Linux-x86_64.sh",shell=True)
    subprocess.run("bash Anaconda3-2019.03-Linux-x86_64.sh -y",shell=True)
    subprocess.run("conda install gcc_linux-64 gxx_linux-64",shell=True)
    subprocess.run("rembg-server",shell=True)


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
