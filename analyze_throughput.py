import pandas as pd

schedulers = ['FCFS', 'SJF', 'PRIORITY', 'MLFQ']

print("\n=== THROUGHPUT TABLE DATA ===")
print("-" * 70)
print(f"{'Scheduler':<12} {'Total Drinks':<15} {'Total Time (s)':<18} {'Drinks/Minute':<15}")
print("-" * 70)

for sched in schedulers:
    try:
        df = pd.read_csv(f'results/ThroughputData_{sched}.csv')
        total_drinks = df['totalDrinksServed'].max()
        start_time = df['completionTime'].min()
        end_time = df['completionTime'].max()
        total_seconds = (end_time - start_time) / 1000
        drinks_per_min = (total_drinks / total_seconds) * 60 if total_seconds > 0 else 0
        
        print(f"{sched:<12} {total_drinks:<15} {total_seconds:<18.1f} {drinks_per_min:<15.1f}")
    except Exception as e:
        print(f"{sched:<12} {'Error':<15} {'Error':<18} {'Error':<15}")

print("-" * 70)