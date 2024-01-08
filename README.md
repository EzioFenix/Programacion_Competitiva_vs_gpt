# GPT 4.0 vs Humano (Programación competitiva)

## Lista de reproducción:



1. Heart Rate: https://youtu.be/Gw79ZzgppPY

****

# Heart Rate (Problema 1,kattis)

A common method for determining your own heart rate is to place your index and third finger on your neck to the side of your windpipe. You then count how many beats you feel in a span of 15 seconds, multiply that number by four and that gives you a measure of your heart rate in beats per minute (BPM). This method gives a good estimate, but is not quite accurate. In general, if you measure $b$ beats in $p$ seconds the BPM is calculated as $ \frac{60b}{p} $.

For this problem, we assume that all heart rates are constant and do not change. If $t$ is the amount of time (in seconds) between each beat of your heart, we define your Actual Beats Per Minute (ABPM) as $ \frac{60}{t} $.

## Input

The input starts with an integer $N (1 \leq N \leq 1000)$ indicating the number of cases to follow. Each of the next $N$ lines specify one case, consisting of the integer $b (2 \leq b \leq 1000)$ as well as $p (0 < p < 1000)$ as described above. The value of $p$ is a real number specified to 4 decimal places.

## Output

For each case, print on a single line the minimum possible ABPM, the calculated BPM, and the maximum possible ABPM, separated by a space. Your answer will be considered correct if its absolute or relative error does not exceed $10^{-4}$.

**Sample Input 1**

```
2
6 5.0000
2 3.1222
```

**Sample output 1**

```
60.0000 72.0000 84.0000
19.2172 38.4344 57.6517
```



## GPT4 (adoc) Solution 

```python
import sys

def calculate_heart_rates(b, p):
    bpm = 60 * b / p
    min_abpm = 60 * (b - 1) / p
    max_abpm = 60 * (b + 1) / p
    return min_abpm, bpm, max_abpm

# Read the number of cases
n = int(sys.stdin.readline().strip())

# Process each case
for _ in range(n):
    b, p = map(float, sys.stdin.readline().split())
    min_abpm, bpm, max_abpm = calculate_heart_rates(b, p)
    sys.stdout.write(f"{min_abpm:.4f} {bpm:.4f} {max_abpm:.4f}\n")

```



## Human Solution 

```python
import sys

def calculate(b,p):
    bpmMax= (60 * (b+1))/p
    bpmMin= (60 * (b-1))/p
    mid=(bpmMax-bpmMin)/2 +bpmMin

    return (bpmMin,mid,bpmMax)

def main():
    cases=int(sys.stdin.readline().strip())

    for i in range(cases):
        b,p=sys.stdin.readline().strip().split()
        min,mid,max=calculate(int(b),float(p))
        print(f"{min:.4f} {mid:.4f} {max:.4f}\n")


if __name__=="__main__":
    main()
```





## Links

[Heart Rate – Kattis, Kattis](https://open.kattis.com/problems/heartrate)
