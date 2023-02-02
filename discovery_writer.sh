#!/bin/bash
while true; do
  cat DATABASE | /opt/homebrew/bin/jq '[{targets: [.targets[]]}]' > prometheus/file_sd.json & sleep 10; 
done
