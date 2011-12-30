
import sys
import subprocess

def run_command(args, cwd=None, verbose=False):
    try:
        # remember shell=False, so use git.cmd on windows, not just git
        p = subprocess.Popen(args, stdout=subprocess.PIPE, cwd=cwd)
    except EnvironmentError:
        if verbose:
            # this is for py2.5 compatibility. When we're >=py2.6, use 'as'.
            e = sys.exc_info()[1]
            print ("unable to run %s: %s" % (args[0], e))
        return None
    stdout = p.communicate()[0].strip()
    if p.returncode != 0:
        if verbose:
            print ("unable to run %s (error)" % args[0])
        return None
    return stdout

