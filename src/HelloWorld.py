#!/usr/bin/python3
#-----------------------------------------------------------------------------
# This file is part of the 'draft_SLAC_template'. It is subject to
# the license terms in the LICENSE.txt file found in the top-level directory
# of this distribution and at:
#    https://confluence.slac.stanford.edu/display/ppareg/LICENSE.html.
# No part of the 'draft_SLAC_template', including this file, may be
# copied, modified, propagated, or distributed except according to the terms
# contained in the LICENSE.txt file.
#-----------------------------------------------------------------------------

import sys
import oracledb


def main():
    un = 'system'
    cs = 'oracle/XEPDB1'
    pw = "admin_password"

    with oracledb.connect(user=un, password=pw, dsn=cs) as connection:
        with connection.cursor() as cursor:
            sql = """select sysdate from dual"""
            for r in cursor.execute(sql):
                print(r)

    if len(sys.argv)<2:
        print("syntax: HelloWorld <your name>")
        return
    n = ' '.join(sys.argv[1:])
    print("Hey there %s.  What's shakin'?"%(n))

    return

if __name__=='__main__':
    main()
