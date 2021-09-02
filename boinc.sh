#!/bin/bash

osascript\
	-e "tell application \"Terminal\" to activate"\
	-e "tell application \"System Events\" to tell process \"Terminal\" to keystroke \"t\" using command down"\
	-e "tell application \"Terminal\" to do script \"ssh -t peter@192.168.0.179 'boinctui && uptime && hostname'\" in selected tab of front window"\
	-e "tell application \"System Events\" to tell process \"Terminal\" to keystroke \"t\" using command down"\
	-e "tell application \"Terminal\" to do script \"ssh -t peter@192.168.0.119 'boinctui && uptime && hostname'\" in selected tab of front window"\
	-e "tell application \"System Events\" to tell process \"Terminal\" to keystroke \"t\" using command down"\
	-e "tell application \"Terminal\" to do script \"ssh -t peter@192.168.0.142 'boinctui && uptime && hostname'\" in selected tab of front window"