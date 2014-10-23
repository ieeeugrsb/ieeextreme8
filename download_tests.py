#!/bin/python
# -*- coding: utf-8 -*-
############################################################################
#  download_tests.py: Download all testcases from HackRank.                #
#  Copyright (C) 2014 Benito Palacios Sánchez                              #
#                                                                          #
#  This program is free software: you can redistribute it and/or modcify   #
#  it under the terms of the GNU General Public License as published by    #
#  the Free Software Foundation, either version 2 of the License, or       #
#  (at your option) any later version.                                     #
#                                                                          #
#  This program is distributed in the hope that it will be useful,         #
#  but WITHOUT ANY WARRANTY; without even the implied warranty of          #
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the            #
#  GNU General Public License for more details.                            #
#                                                                          #
#  You should have received a copy of the GNU General Public License       #
#  along with this program. If not, see <http://www.gnu.org/licenses/>.    #
############################################################################
import urllib2
import sys


def downloadtest(slug, problemId, testId, command, cookie):
    # Get the REST API URL.
    URL_API = "http://ieee.hackerrank.com/rest/contests/%s/testcases/%d/%d/%s"
    url = URL_API % (slug, problemId, testId, command)

    try:
        # Create the URL Opener and set cookies
        opener = urllib2.build_opener()
        opener.addheaders.append(('Cookie', cookie))

        # Send request
        req = opener.open(url)

        # Get returned address (it can be the same if error).
        next_url = req.geturl()

        # Check HTTP returned code
        if req.getcode() != 200:
            print "Error code: %d" % req.getcode()
            return False
        elif next_url != url:
            # Send request for testcase file
            test = urllib2.urlopen(req.geturl())

            # Save the output in a file
            filename = '%s%02d.txt' % (command[8:], testId)
            f = open(filename, 'w')
            f.write(test.read())
            f.close()

            # Return successfull
            return True
        else:
            print "Invalid cookies?"
            return False
    except urllib2.HTTPError as e:
        if e.code != 500:
            print "Error de petición -> " + str(e)
        return False


def downloadproblem(slug, problemId, cookie):
    COMMAND = ["testcaseinput", "testcaseoutput"]

    # While the input exists... Download the output too
    num = 0
    while downloadtest(slug, problemId, num, COMMAND[0], cookie):
        # Download output now
        downloadtest(slug, problemId, num, COMMAND[1], cookie)

        # Incremente testcase
        num = num + 1


if __name__ == "__main__":
    # Constants
    CONTEST_SLUG = "ieeextreme8"    # CHALLENGE ID
    NUM_PROBLEMS = range(3, 26)     # PROBLEMS RANGE

    # Get cookies
    cookie = sys.argv[0]

    # For each problem, download its testcases
    for n in NUM_PROBLEMS:
        sys.stdout.write("Downloading problem: %02d... " % n)
        sys.stdout.flush()
        downloadproblem(CONTEST_SLUG, n, cookie)
        sys.stdout.write("Done!")
        raw_input()     # Wait for a Enter press
