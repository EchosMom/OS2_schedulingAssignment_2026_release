#!/bin/bash

PATRONS = (7 25 35 50 100 200 250)
SCHEDULERS = (0 1 2 3 )
RUNS = 5

for patrons in "${PATRONS[@]}"; do  
    for shedulers in "${SCHEDULERS[@]}"; do
        for runs in $(seq 1 $RUNS); do
            SEED = $((patrons*10000 + schedulers * 1000 + run))
            echo "Running: Patron num=$patrons, Scheduler=$schedulers, Run num=$runs"
            make run ARGS = "$patrons $scheduleers 0 $SEED"
        done
    done
done

echo "Done."