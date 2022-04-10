from logic import symulacja_urzedu  # type: ignore
import pandas as pd
import plotly.express as px

CLIENTS = 30
TRIALS = 100

df = {"u1": [], "u2": []}
for _ in range(TRIALS):
    df["u1"].append(symulacja_urzedu(CLIENTS, 3, 3, 3, 0))
    df["u2"].append(symulacja_urzedu(CLIENTS, 2, 2, 2, 3))

pdf = pd.DataFrame(df)
# figure for non-sorted queues
figure = px.histogram(
    pdf,
    labels={
        "value": "czas obsługi wszystkich klientów [ticks]",
    },
    title=f"{CLIENTS} klientów {TRIALS} razy, zadania nieposortowane",
    template="plotly_dark",
    text_auto=True,
)
figure.show()

df = {"u1": [], "u2": []}
for _ in range(TRIALS):
    df["u1"].append(symulacja_urzedu(CLIENTS, 3, 3, 3, 0, True))
    df["u2"].append(symulacja_urzedu(CLIENTS, 2, 2, 2, 3, True))
pdf = pd.DataFrame(df)
# figure for sorted queues
figure = px.histogram(
    pdf,
    labels={
        "value": "czas obsługi wszystkich klientów [ticks]",
    },
    title=f"{CLIENTS} klientów {TRIALS} razy, zadania posortowane rosnąco",
    template="plotly_dark",
    text_auto=True,
)
figure.show()

df = {"u1": [], "u2": []}
for _ in range(TRIALS):
    df["u1"].append(symulacja_urzedu(CLIENTS, 3, 3, 3, 0, True, True))
    df["u2"].append(symulacja_urzedu(CLIENTS, 2, 2, 2, 3, True, True))
pdf = pd.DataFrame(df)
# figure for revsorted queues
figure = px.histogram(
    pdf,
    labels={
        "value": "czas obsługi wszystkich klientów [ticks]",
    },
    title=f"{CLIENTS} klientów {TRIALS} razy, zadania posortowane malejąco",
    template="plotly_dark",
    text_auto=True,
)
figure.show()
