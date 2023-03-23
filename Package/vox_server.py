import os
import subprocess

def run_background_exe(exe_path):
    # Check if the executable is already running
    if any(os.path.basename(exe_path) in p.decode() for p in subprocess.check_output('tasklist').split(b'\n')):
        
        return
    else:
        
        # Create a startupinfo object to configure the new process
        startupinfo = subprocess.STARTUPINFO()
        startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW
        startupinfo.wShowWindow = subprocess.SW_HIDE

        # Redirect stdout and stderr to DEVNULL
        stdout = stderr = subprocess.DEVNULL

        # Start the new process with the startupinfo object and redirected output
        subprocess.Popen(exe_path, startupinfo=startupinfo, stdout=stdout, stderr=stderr)
