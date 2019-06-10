#!/usr/bin/env fish


# @Author: S. Sharma <silentcat>
# @Date:   2019-06-10T12:03:03-05:00
# @Email:  silentcat@protonmail.com
# @Last modified by:   silentcat
# @Last modified time: 2019-06-10T12:30:44-05:00

set cnt 1
set arg_count (count $argv)

if test $arg_count -gt 0
  set cnt $argv[1]
end
set dir ""

for i in (seq $cnt)
  set dir "$dir"../
end

cd $dir 2> /dev/null
