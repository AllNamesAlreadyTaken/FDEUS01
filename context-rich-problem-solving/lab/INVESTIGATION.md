##codebase data-flow map

This codebase runs a straightforward event pipeline where raw dictionaries are ingested into Event objects using customer_id, normalized to a consistent format, enriched with derived metadata, and exported as JSONL records with a shared schema version, while companion reporting services read the same Event list to produce per-customer counts and value totals; tests validate each stage’s core behavior so the flow remains predictable as the code evolves.

## Agent discovery pattern

The discovery pattern went across the files in order after running pytest, then identified some renamed  files and directories.  It then recalled pytest to make sure it was correct.

## Audit findings

I was unable to fully embrace audit due to time constraints, but I would naturally chekc the audits for validaty in any codebase audit toggled by the hash command codebase

## Self-correction

copilot went in and scanned the full codebase more deeply

## Summary

codebase mapped the content closely but not exactly.  The refactor added a few changes and files.  I didn't capture the category exactly.
