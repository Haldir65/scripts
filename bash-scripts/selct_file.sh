
#!/bin/bash

files="$(ls -A .)"
select filename in ${files}; do echo "You selected ${filename}"; break; done
1) file1
2) file2
3) file3

