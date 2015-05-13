#!/usr/bin/env python
# encoding: utf-8

import sys
import os
import unittest
import pexpect
from Naked.toolshed.shell import execute
from Naked.toolshed.system import file_exists, make_path

class CryptoMultiFileParallelEncryptTest(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def submit_same_passphrase(self, system_command):
        child = pexpect.spawn(system_command)
        child.expect("Please enter your passphrase: ")
        child.sendline("test")
        child.expect("Please enter your passphrase again: ")
        child.sendline("test")
        child.interact()
        return child


    # text files
    def test_multifile_encrypt_parallel_txt(self):
        command = "crypto --parallel 4 testdir12"
        child = self.submit_same_passphrase(command)
        for i in range(10):
            self.assertTrue(file_exists(make_path("testdir12", "file0"+str(i)+".txt.crypt"))) #test that new encrypted file exists
        child.close()

        # cleanup
        for i in range(10):
            os.remove(make_path("testdir12","file0"+str(i)+".txt.crypt"))



