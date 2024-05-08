#!/usr/bin/python3
import argparse
import subprocess
import sys

# Usage: ./get_input.py > 1.in
# You must fill in SESSION following the instructions below.
# DO NOT run this in a loop, just once.

# You can find SESSION by using Chrome tools:
# 1) Go to https://adventofcode.com/2022/day/1/input
# 2) right-click -> inspect -> click the "Application" tab.
# 3) Refresh
# 5) Click https://adventofcode.com under "Cookies"
# 6) Grab the value for session. Fill it in.
SESSION = '53616c7465645f5fd62d8611b0d602f15194995b6f4b771fb0f3127c2c04f859e0419260d08133204b442bbc606f692e3d8402bcf52881f3ab2f266526216356'

useragent = 'https://github.com/zibiax/aoc2023/blob/main/get_input.py by martin.evenbom@gmail.com'
parser = argparse.ArgumentParser(description='Read input')
parser.add_argument('--year', type=int, default=2023)
parser.add_argument('--day', type=int, default=1)
args = parser.parse_args()

cmd = f'curl https://adventofcode.com/{args.year}/day/{args.day}/input --cookie "session={SESSION}" -A "{useragent}"'
try:
    output = subprocess.check_output(cmd, shell=True)
    output = output.decode('utf-8')
    print(output, end='')
except subprocess.CalledProcessError as e:
    print(f"Error: {e}", file=sys.stderr)
