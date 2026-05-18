import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import glob
import os

# Set style
sns.set_style("whitegrid")
plt.rcParams['figure.figsize'] = (12, 8)

# Load all results
results = {}
throughput_data = {}

# Get all CSV files in results folder
for file in glob.glob("results/*.csv"):
    # Get filename without path
    filename = os.path.basename(file)

    df = pd.read_csv(file)
    df.columns = df.columns.str.strip() 
    
    # Check if it's a throughput file
    if 'ThroughputData' in filename:
        scheduler = filename.replace('ThroughputData_', '').replace('.csv', '')
        throughput_data[scheduler] = df
        print(f"Loaded throughput data for {scheduler}")
    else:
        scheduler = filename.replace('.csv', '')
        results[scheduler] = df
        print(f"Loaded main data for {scheduler}")

# Print statistics
print("\n" + "="*50)
print("SCHEDULER STATISTICS")
print("="*50)

for scheduler, df in results.items():
    print(f"\n{scheduler} SCHEDULER:")
    print(f"  Total drinks served: {len(df)}")
    print(f"\n  Response Time (ms):")
    print(f"    Mean: {df['ResponseTime'].mean():.2f}")
    print(f"    Median: {df['ResponseTime'].median():.2f}")
    print(f"    Std Dev: {df['ResponseTime'].std():.2f}")
    print(f"  Waiting Time (ms):")
    print(f"    Mean: {df['WaitingTime'].mean():.2f}")
    print(f"    Median: {df['WaitingTime'].median():.2f}")
    print(f"  Turnaround Time (ms):")
    print(f"    Mean: {df['TurnaroundTime'].mean():.2f}")
    print(f"    Median: {df['TurnaroundTime'].median():.2f}")

# Create box plots
if results:
    fig, axes = plt.subplots(1, 3, figsize=(15, 5))
    metrics = ['ResponseTime', 'WaitingTime', 'TurnaroundTime']
    
    for i, metric in enumerate(metrics):
        data = [df[metric] for df in results.values()]
        bp = axes[i].boxplot(data, labels=results.keys(), patch_artist=True)
        axes[i].set_title(f'{metric} Distribution')
        axes[i].set_ylabel('Time (ms)')
        axes[i].set_yscale('log')
    
    plt.tight_layout()
    plt.savefig('results/metrics_comparison.png', dpi=150)
    print("\n✓ Saved: results/metrics_comparison.png")

# Throughput over time
if throughput_data:
    fig, ax = plt.subplots(figsize=(12, 6))
    for scheduler, df in throughput_data.items():
        ax.plot(df['completionTime']/1000, df['totalDrinksServed'], 
                label=scheduler, linewidth=2)
    ax.set_xlabel('Time (seconds)')
    ax.set_ylabel('Total Drinks Served')
    ax.set_title('Throughput Comparison Over Time')
    ax.legend()
    ax.grid(True, alpha=0.3)
    plt.savefig('results/throughput_comparison.png', dpi=150)
    print("✓ Saved: results/throughput_comparison.png")

# Fairness analysis
if results:
    fig, ax = plt.subplots(figsize=(12, 6))
    for scheduler, df in results.items():
        patron_avg = df.groupby('PatronID')['ResponseTime'].mean()
        ax.plot(patron_avg.index, patron_avg.values, 'o-', label=scheduler, alpha=0.7)
    ax.set_xlabel('Patron ID')
    ax.set_ylabel('Average Response Time (ms)')
    ax.set_title('Fairness: Response Time by Patron')
    ax.legend()
    ax.grid(True, alpha=0.3)
    plt.savefig('results/fairness_analysis.png', dpi=150)
    print("✓ Saved: results/fairness_analysis.png")

print("\n✅ Analysis complete! Check the results/ folder for graphs.")