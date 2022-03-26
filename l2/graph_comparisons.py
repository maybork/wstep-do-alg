from algorithms import bubblesort as bbl
from algorithms import insertionsort as ins
from algorithms import selectionsort as sel
import testsuite
import plotly.express as px
import pandas as pd
import time


NS = [10, 20, 50, 100, 200, 500, 1000]
# NS = [10, 20, 50, 100, 200, 500, 1000, 1500, 2000, 2500, 5000, 7500, 10000]

tested_algs = (
    bbl.bubblesort,
    bbl.bubblesort_naive,
    bbl.bubblesort_smart,
    ins.insertionsort,
    sel.selectionsort,
)

averages = {}
maxima = {}
for alg in tested_algs:
    print(f"running tests for {alg.__name__}")
    start = time.time()
    averages[alg.__name__] = []
    maxima[alg.__name__] = []
    results = []
    for n in NS:
        # change length to 10
        results.append(testsuite.run_tests(n, 100, alg))
    for avg, mx in results:
        averages[alg.__name__].append(avg)
        maxima[alg.__name__].append(mx)
    end = time.time()
    print(f"done in {end-start:.5f} s")


avgdf = pd.DataFrame.from_dict(averages).set_axis(NS, axis="index")
maxdf = pd.DataFrame.from_dict(maxima).set_axis(NS, axis="index")

avgfig = px.line(
    avgdf,
    markers=True,
    labels={"index": "samples", "value": "timewi [s]", "variable": "algorithm"},
    title="Average runtimes",
    template="plotly_dark",
)
maxfig = px.line(
    maxdf,
    markers=True,
    labels={"index": "samples", "value": "time [s]", "variable": "algorithm"},
    title="Maximum runtimes",
    template="plotly_dark",
)

avgfig.show()
maxfig.show()
