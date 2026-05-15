import os
import pandas as pd

# Get file info
files = {}
for f in os.listdir():
    if f.endswith(('.py', '.csv', '.md', '.txt')):
        size = os.path.getsize(f)
        files[f] = size

# Get dataset info
df = pd.read_csv('music.csv')

print('='*60)
print('🎵 MUSIC RECOMMENDER PRO v2.0 - PROJECT SUMMARY')
print('='*60)
print()
print('📊 PROJECT STATISTICS')
print('-'*60)
print(f'Python Files: {len([f for f in files if f.endswith(".py")])}')
print(f'Documentation Files: {len([f for f in files if f.endswith(".md")])}')
print(f'Data Files: {len([f for f in files if f.endswith(".csv")])}')
print()
print('🎵 DATASET INFORMATION')
print('-'*60)
print(f'Total Songs: {len(df)}')
print(f'Total Columns: {len(df.columns)}')
print(f'Data Fields: {list(df.columns)}')
print()
print('💾 FILE SIZES')
print('-'*60)
for fname in sorted(files.keys()):
    size_kb = files[fname] / 1024
    print(f'{fname:30s}: {size_kb:8.1f} KB')
print()
print('✅ PROJECT READY TO DEPLOY!')
print('='*60)
