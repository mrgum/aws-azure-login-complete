#!/usr/bin/env python3

import configparser
import os
import sys

"""
--profile

"""

def azure_profiles():
	profiles = []
	profile_prefix='profile '

	config = configparser.ConfigParser()
	config.read(os.path.expanduser('~/.aws/config'))
	for section in config.sections():
		if 'azure_tenant_id' in config[section]:
			if section.startswith(profile_prefix):
				profiles.append(section[len(profile_prefix):])
	return profiles


def completion_hook(cmd, curr_word, prev_word):
    potential_matches = azure_profiles()
    matches = [k for k in potential_matches if k.startswith(curr_word)]
    return matches


def main():
    results = completion_hook(*sys.argv[1:])
    if len(results):
          print("\n".join(results))


if __name__ == "__main__":
    main()
