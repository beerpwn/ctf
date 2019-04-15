#!/bin/bash
# Cron. But worse.
#
# Copyright (c) 2019, SuckMore Software, a division of WPI Digital Holdings Ltd.
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
# 1. Redistributions of source code must retain the above copyrig
#    notice, this list of conditions and the following disclaimer.
# 2. Redistributions in binary form must reproduce the above copyright
#    notice, this list of conditions and the following disclaimer in the
#    documentation and/or other materials provided with the distribution.
# 3. All advertising materials mentioning features or use of this software
#    must display the following acknowledgement:
#    This product includes software developed by SuckMore Software, a division
#    of WPI Digital Holdings Ltd.
# 4. Neither the name of the SuckMore Software, a division of WPI Digital Holdings
#    Ltd, nor the names of its contributors may be used to endorse or promote
#    products derived from this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY SuckMore Software, a division of
# WPI Digital Holdings Ltd., ''AS IS'' AND ANY EXPRESS OR IMPLIED WARRANTIES,
# INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND
# FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL
# SuckMore Software, a division of WPI Digital Holdings Ltd.
# DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
# (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND
# ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
# SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

file="/etc/deadline"

cron() {
    second=0
    minute=0
    hour=0
    day=1;
    month=1;
    year=2019;

    while true; do
        sleep 1;
        target_second=`cut -d " " -f 6 $file`
        target_minute=`cut -d " " -f 5 $file`
        target_hour=`cut -d " " -f 4 $file`
        target_day=`cut -d " " -f 3 $file`
        target_month=`cut -d " " -f 2 $file`
        target_year=`cut -d " " -f 1 $file`

        if [[ "$second" -eq 59 ]]; then
            minute=$((minute+1));
            second=0;
        elif [[ "$minute" -eq 59 ]]; then
            hour=$((hour+1));
            second=0;
            minute=0;
        else
            second=$((second+1));
        fi

        if [[ "$year" -eq "$target_year" ]] \
            && [[ "$month" -eq "$target_month" ]] \
            && [[ "$day" -eq "$target_day" ]] \
            && [[ "$hour" -eq "$target_second" ]] \
            && [[ "$minute" -eq "$target_minute" ]] \
            && [[ "$second" -eq "$target_hour" ]]; then
            # echo "WPI{}" > /home/ctf/flag.txt
            exec_flag
        fi

        rm /etc/faketimerc
        echo "$year-$month-$day $hour:$minute:$second" > /etc/faketimerc
    done
}