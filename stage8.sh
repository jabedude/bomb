#!/bin/bash

echo temper > %d\ %c\ %d                        # Create and put the xor's hiddenmessage
printf "\0" >> %d\ %c\ %d                       # Append a null bute
python2 -c "print 'a' * 80" >> %d\ %c\ %d       # Add 80 bytes to meet the 63 byte requirement
