import pandas as pd

schedulers = ['FCFS', 'SJF', 'PRIORITY', 'MLFQ']
results = {}

for sched in schedulers:
    df = pd.read_csv(f'results/{sched}.csv')
    df.columns = df.columns.str.strip()
    results[sched] = df

print("\n=== CORRECT TURNAROUND TIME STATISTICS ===")
print(f"{'Scheduler':<12} {'Median (ms)':<15} {'Mean (ms)':<15} {'Skew'}")
print("-" * 55)

for sched in schedulers:
    df = results[sched]
    median_tt = df['TurnaroundTime'].median()
    mean_tt = df['TurnaroundTime'].mean()
    skew_type = "Huge right skew" if (mean_tt - median_tt) > 1000 else "Small right skew"
    print(f"{sched:<12} {median_tt:<15.0f} {mean_tt:<15.0f} {skew_type}")