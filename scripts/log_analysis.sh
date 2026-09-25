#!/bin/bash

LOG_FILE="logs/application.log"

echo "=============================="
echo "     LOG ANALYSIS REPORT"
echo "=============================="

echo ""
echo "Total Records:"
wc -l < "$LOG_FILE"

echo ""
echo "INFO Records:"
grep -c "INFO" "$LOG_FILE"

echo ""
echo "ERROR Records:"
grep -c "ERROR" "$LOG_FILE"

echo ""
echo "ERROR Details:"
grep "ERROR" "$LOG_FILE"

echo ""
echo "Log Level Summary:"
awk '{print $3}' "$LOG_FILE" | sort | uniq -c