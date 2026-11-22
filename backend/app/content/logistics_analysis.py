"""Análisis matemático real con NumPy del Proyecto 01: Red Logística LOGISPAÑA (10_Proyecto_Red_Logistica.md)."""
from __future__ import annotations

from collections import deque
from typing import Any

import numpy as np

# Datos exactos de P01 Datos.xlsx transcritos en _contexto_mpi/10_Proyecto_Red_Logistica.md
CENTERS: list[dict[str, Any]] = [
    {"code": "M", "name": "Madrid", "type": "hub nacional", "x": 38, "y": 48},
    {"code": "B", "name": "Barcelona", "type": "hub nacional", "x": 82, "y": 36},
    {"code": "V", "name": "Valencia", "type": "hub nacional", "x": 72, "y": 58},
    {"code": "Z", "name": "Zaragoza", "type": "hub regional", "x": 60, "y": 30},
    {"code": "S", "name": "Sevilla", "type": "hub regional", "x": 18, "y": 78},
    {"code": "BI", "name": "Bilbao", "type": "hub regional", "x": 46, "y": 12},
    {"code": "MA", "name": "Málaga", "type": "distribución", "x": 34, "y": 89},
    {"code": "MU", "name": "Murcia", "type": "distribución", "x": 58, "y": 82},
    {"code": "VA", "name": "Valladolid", "type": "distribución", "x": 28, "y": 28},
    {"code": "CO", "name": "Córdoba", "type": "distribución", "x": 34, "y": 68},
    {"code": "AL", "name": "Alicante", "type": "distribución", "x": 82, "y": 78},
    {"code": "GI", "name": "Gerona", "type": "distribución", "x": 92, "y": 16},
]

FLOWS: list[dict[str, Any]] = [
    {"source": "Madrid", "target": "Zaragoza", "flow": 850},
    {"source": "Madrid", "target": "Valencia", "flow": 780},
    {"source": "Madrid", "target": "Sevilla", "flow": 620},
    {"source": "Madrid", "target": "Valladolid", "flow": 430},
    {"source": "Zaragoza", "target": "Barcelona", "flow": 760},
    {"source": "Zaragoza", "target": "Bilbao", "flow": 410},
    {"source": "Zaragoza", "target": "Valencia", "flow": 390},
    {"source": "Barcelona", "target": "Gerona", "flow": 520},
    {"source": "Barcelona", "target": "Valencia", "flow": 610},
    {"source": "Barcelona", "target": "Zaragoza", "flow": 300},
    {"source": "Valencia", "target": "Murcia", "flow": 570},
    {"source": "Valencia", "target": "Alicante", "flow": 640},
    {"source": "Valencia", "target": "Madrid", "flow": 350},
    {"source": "Sevilla", "target": "Córdoba", "flow": 480},
    {"source": "Sevilla", "target": "Málaga", "flow": 530},
    {"source": "Córdoba", "target": "Madrid", "flow": 260},
    {"source": "Málaga", "target": "Sevilla", "flow": 240},
    {"source": "Bilbao", "target": "Valladolid", "flow": 310},
    {"source": "Valladolid", "target": "Madrid", "flow": 290},
    {"source": "Murcia", "target": "Valencia", "flow": 220},
    {"source": "Alicante", "target": "Valencia", "flow": 260},
    {"source": "Gerona", "target": "Barcelona", "flow": 180},
]

HISTORICAL_DEMAND: list[dict[str, Any]] = [
    {"year": 2016, "volume": 15.2},
    {"year": 2017, "volume": 16.1},
    {"year": 2018, "volume": 17.0},
    {"year": 2019, "volume": 18.4},
    {"year": 2020, "volume": 18.0},
    {"year": 2021, "volume": 19.6},
    {"year": 2022, "volume": 20.8},
    {"year": 2023, "volume": 22.1},
    {"year": 2024, "volume": 23.4},
    {"year": 2025, "volume": 24.8},
]


def _compute_demand_models() -> dict[str, Any]:
    years = np.array([d["year"] for d in HISTORICAL_DEMAND], dtype=float)
    vols = np.array([d["volume"] for d in HISTORICAL_DEMAND], dtype=float)
    t = years - 2016.0
    t_2028 = 2028.0 - 2016.0
    v_2025 = vols[-1]

    models = []
    for deg in [1, 2, 3]:
        coeffs = np.polyfit(t, vols, deg)
        preds = np.polyval(coeffs, t)
        rmse = float(np.sqrt(np.mean((vols - preds) ** 2)))
        pred_2028 = float(np.polyval(coeffs, t_2028))
        pct_inc = float((pred_2028 - v_2025) / v_2025 * 100.0)
        models.append(
            {
                "degree": deg,
                "coefficients": [round(float(c), 8) for c in coeffs],
                "rmse": round(rmse, 4),
                "prediction_2028": round(pred_2028, 3),
                "pct_increase_vs_2025": round(pct_inc, 2),
                "fitted_series": [round(float(x), 3) for x in preds],
            }
        )
    return {"historical": HISTORICAL_DEMAND, "models": models}


def _compute_pagerank(A: np.ndarray, damping: float = 0.85, tol: float = 1e-13) -> tuple[np.ndarray, float]:
    """Calcula PageRank ponderado (estilo MATLAB centrality(G,'pagerank','Importance',W)) con residuo."""
    n = A.shape[0]
    if n == 0:
        return np.array([]), 0.0
    # Matriz columna-estocástica P donde P[j, i] = A[i, j] / sum_k A[i, k]
    out_sums = A.sum(axis=1)
    P = np.zeros((n, n), dtype=float)
    for i in range(n):
        if out_sums[i] > 0:
            P[:, i] = A[i, :] / out_sums[i]
        else:
            # Nodo colgante (dangling node, como Murcia/Alicante tras la DANA de Valencia)
            P[:, i] = 1.0 / n
    G = damping * P + (1.0 - damping) / n * np.ones((n, n), dtype=float)
    r = np.ones(n, dtype=float) / n
    for _ in range(5000):
        r_next = G @ r
        if np.linalg.norm(r_next - r, 2) < tol:
            r = r_next
            break
        r = r_next
    r = r / r.sum()
    res = float(np.linalg.norm(G @ r - r, 2))
    return r, res


def _compute_markov_3_methods(A: np.ndarray) -> dict[str, Any]:
    """Reto 4: calcula equilibrio Markov mediante 3 métodos (potencias, eig y sistema lineal) + norma residuo."""
    n = A.shape[0]
    out_sums = A.sum(axis=1)
    P = np.zeros((n, n), dtype=float)
    for i in range(n):
        if out_sums[i] > 0:
            P[:, i] = A[i, :] / out_sums[i]
        else:
            P[:, i] = 1.0 / n

    # Método 1: Iteración de potencias (x_{k+1} = P x_k)
    x_pow = np.ones(n, dtype=float) / n
    iters = 0
    for iters in range(1, 5000):
        x_next = P @ x_pow
        if np.linalg.norm(x_next - x_pow, 2) < 1e-13:
            x_pow = x_next
            break
        x_pow = x_next
    x_pow = x_pow / x_pow.sum()
    res_pow = float(np.linalg.norm(P @ x_pow - x_pow, 2))

    # Método 2: Autovector asociado a λ = 1 (eig)
    eigvals, eigvecs = np.linalg.eig(P)
    idx = int(np.argmin(np.abs(eigvals - 1.0)))
    x_eig = np.real(eigvecs[:, idx])
    if x_eig.sum() < 0:
        x_eig = -x_eig
    x_eig = x_eig / x_eig.sum()
    res_eig = float(np.linalg.norm(P @ x_eig - x_eig, 2))

    # Método 3: Sistema lineal (P - I)x = 0 con restricción sum(x) = 1
    M = P - np.eye(n)
    M[-1, :] = 1.0
    rhs = np.zeros(n, dtype=float)
    rhs[-1] = 1.0
    try:
        x_sys = np.linalg.solve(M, rhs)
        x_sys = x_sys / x_sys.sum()
        res_sys = float(np.linalg.norm(P @ x_sys - x_sys, 2))
    except np.linalg.LinAlgError:
        x_sys = x_eig
        res_sys = res_eig

    return {
        "distribution": x_eig,
        "methods": [
            {"method": "Iteración de potencias (Pᵏ·x₀)", "iterations": iters, "residual_norm": res_pow},
            {"method": "Autovectores (eig, λ = 1)", "iterations": 1, "residual_norm": res_eig},
            {"method": "Sistema lineal ((P−I)x = 0, Σx = 1)", "iterations": 1, "residual_norm": res_sys},
        ],
    }


def _compute_betweenness(names: list[str], edges: list[dict[str, Any]]) -> dict[str, float]:
    """Centralidad de intermediación (Brandes sobre dígrafo no ponderado)."""
    adj: dict[str, list[str]] = {u: [] for u in names}
    for e in edges:
        adj[e["source"]].append(e["target"])
    cb = {u: 0.0 for u in names}
    for s in names:
        stack: list[str] = []
        pred: dict[str, list[str]] = {w: [] for w in names}
        sigma: dict[str, float] = {w: 0.0 for w in names}
        sigma[s] = 1.0
        dist: dict[str, int] = {w: -1 for w in names}
        dist[s] = 0
        q: deque[str] = deque([s])
        while q:
            v = q.popleft()
            stack.append(v)
            for w in adj[v]:
                if dist[w] < 0:
                    q.append(w)
                    dist[w] = dist[v] + 1
                if dist[w] == dist[v] + 1:
                    sigma[w] += sigma[v]
                    pred[w].append(v)
        delta = {w: 0.0 for w in names}
        while stack:
            w = stack.pop()
            for v in pred[w]:
                if sigma[w] > 0:
                    delta[v] += (sigma[v] / sigma[w]) * (1.0 + delta[w])
            if w != s:
                cb[w] += delta[w]
    return cb


def analyze_network(disabled_center: str | None = None) -> dict[str, Any]:
    """Ejecuta el análisis completo de la red LOGISPAÑA (normal o con escenario de caída de nodo, ej. Valencia)."""
    active_centers = [c for c in CENTERS if c["name"] != disabled_center]
    names = [c["name"] for c in active_centers]
    idx_map = {name: i for i, name in enumerate(names)}
    n = len(names)

    active_flows = [f for f in FLOWS if f["source"] != disabled_center and f["target"] != disabled_center]
    removed_flows = [f for f in FLOWS if f["source"] == disabled_center or f["target"] == disabled_center]

    A = np.zeros((n, n), dtype=float)
    for f in active_flows:
        A[idx_map[f["source"]], idx_map[f["target"]]] = f["flow"]

    in_flow = A.sum(axis=0)
    out_flow = A.sum(axis=1)
    total_vol = in_flow + out_flow
    in_deg = (A > 0).sum(axis=0)
    out_deg = (A > 0).sum(axis=1)
    total_deg = in_deg + out_deg

    markov = _compute_markov_3_methods(A)
    pr, pr_res = _compute_pagerank(A, damping=0.85)
    betw = _compute_betweenness(names, active_flows)

    max_vol = float(total_vol.max()) if n and total_vol.max() > 0 else 1.0
    max_deg = float(total_deg.max()) if n and total_deg.max() > 0 else 1.0
    max_pr = float(pr.max()) if n and pr.max() > 0 else 1.0
    max_betw = max(betw.values()) if betw and max(betw.values()) > 0 else 1.0

    # Si estamos simulando una caída (DANA Valencia), calculamos también el baseline normal para mostrar deltas
    baseline_rank: dict[str, int] = {}
    if disabled_center:
        base = analyze_network(disabled_center=None)
        for pos, row in enumerate(base["ranking_pagerank"], start=1):
            baseline_rank[row["name"]] = pos

    node_metrics = []
    for i, c in enumerate(active_centers):
        name = c["name"]
        node_metrics.append(
            {
                "code": c["code"],
                "name": name,
                "type": c["type"],
                "x": c["x"],
                "y": c["y"],
                "in_flow": int(in_flow[i]),
                "out_flow": int(out_flow[i]),
                "total_volume": int(total_vol[i]),
                "in_degree": int(in_deg[i]),
                "out_degree": int(out_deg[i]),
                "total_degree": int(total_deg[i]),
                "markov_pct": round(float(markov["distribution"][i] * 100.0), 2),
                "pagerank_pct": round(float(pr[i] * 100.0), 2),
                "betweenness": round(float(betw[name]), 2),
                "norm_volume": round(float(total_vol[i] / max_vol), 3),
                "norm_degree": round(float(total_deg[i] / max_deg), 3),
                "norm_pagerank": round(float(pr[i] / max_pr), 3),
                "norm_betweenness": round(float(betw[name] / max_betw), 3),
                "is_isolated": bool(in_deg[i] == 0 and out_deg[i] == 0),
                "is_dangling": bool(out_deg[i] == 0),
            }
        )

    ranking_pr = sorted(node_metrics, key=lambda item: item["pagerank_pct"], reverse=True)
    for pos, item in enumerate(ranking_pr, start=1):
        item["rank_now"] = pos
        if disabled_center and item["name"] in baseline_rank:
            item["rank_before"] = baseline_rank[item["name"]]
            item["rank_delta"] = baseline_rank[item["name"]] - pos  # positivo = sube puestos
        else:
            item["rank_before"] = pos
            item["rank_delta"] = 0

    return {
        "disabled_center": disabled_center,
        "centers_all": CENTERS,
        "nodes": node_metrics,
        "ranking_pagerank": ranking_pr,
        "active_flows": active_flows,
        "removed_flows": removed_flows,
        "summary": {
            "active_centers_count": n,
            "active_routes_count": len(active_flows),
            "removed_routes_count": len(removed_flows),
            "total_weekly_tonnes": int(sum(f["flow"] for f in active_flows)),
            "lost_weekly_tonnes": int(sum(f["flow"] for f in removed_flows)),
            "pagerank_residual": pr_res,
        },
        "markov_methods": markov["methods"],
        "demand": _compute_demand_models(),
    }
