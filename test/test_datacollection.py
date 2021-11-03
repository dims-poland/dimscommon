import unittest
import subprocess
from configparser import ConfigParser

import dimscommon.datacollection as dc


class TestDatacollection(unittest.TestCase):
    def test_construct(self):
        import subprocess

        docker_compose = subprocess.Popen(["sudo", "docker-compose", "up"],
                                stdin =subprocess.PIPE,
                                stdout=subprocess.PIPE,
                                stderr=subprocess.PIPE,
                                universal_newlines=True,
                                bufsize=0)
        docker_compose.stdin.close()
        
        col = dc.DataCollection(ConfigParser())

    def test_insert(self):
        pass


if __name__ == "__main__":
    unittest.main()