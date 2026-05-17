#!/bin/bash

PATRONS=(7 25 35 50 100 200 250)
SCHEDULERS=(0 1 2 3)
RUNS=10

for patrons in "${PATRONS[@]}"; do  
    for schedulers in "${SCHEDULERS[@]}"; do
        for runs in $(seq 1 $RUNS); do
            SEED=$((patrons*10000 + schedulers * 1000 + runs))
            echo "Running: Patron num=$patrons, Scheduler=$schedulers, Run num=$runs"
            java -cp bin barScheduling.SchedulingSimulation $patrons $schedulers 0 $SEED
        done
    done
done

echo "Done."