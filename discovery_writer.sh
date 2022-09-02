#!/bin/bash
set -x
for i in 1 2 3 4 5 6 7 8 9 10 11; do
  cat DATABASE | /opt/homebrew/bin/jq '[{targets: [.targets[]]}]' > prometheus/file_sd.json & sleep 10; 
done
