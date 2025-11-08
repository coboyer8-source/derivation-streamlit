#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov  8 15:22:06 2025

@author: corinneboyer
"""

import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# Fonction et dérivée
def f(x):
    return np.sin(x)

def df(x):
    return np.cos(x)

# Point fixe
x0 = np.pi / 4
y0 = f(x0)

# Curseur interactif
dx = st.slider("Choisis Δx", min_value=0.01, max_value=2.0, value=1.0, step=0.01)
x1 = x0 + dx
y1 = f(x1)

# Calculs
slope_secant = (y1 - y0) / (x1 - x0)
slope_tangent = df(x0)
x_vals = np.array([x0 - 1, x1 + 1])
y_secant = y0 + slope_secant * (x_vals - x0)
y_tangent = y0 + slope_tangent * (x_vals - x0)

# Tracé
fig, ax = plt.subplots(figsize=(8, 6))
x = np.linspace(0, 2 * np.pi, 400)
ax.plot(x, f(x), label='f(x) = sin(x)', color='black')
ax.plot(x0, y0, 'ro', label='x₀')
ax.plot(x1, y1, 'bo', label='x₀ + Δx')
ax.plot(x_vals, y_secant, 'b--', label='Sécante')
ax.plot(x_vals, y_tangent, 'orange', label='Tangente')
ax.plot([x0, x1], [y0, y0], 'g-', lw=2)
ax.plot([x1, x1], [y0, y1], 'purple', lw=2)

# Annotations
# ax.annotate(f"x₀ = {x0:.2f}", (x0, y0), textcoords="offset points", xytext=(-30, -15), color='red')
# ax.annotate(f"x₀ + Δx = {x1:.2f}", (x1, y1), textcoords="offset points", xytext=(10, -15), color='blue')
# ax.annotate(f"f(x₀) = {y0:.2f}", (x0, y0), textcoords="offset points", xytext=(-30, 10), color='red')
# ax.annotate(f"f(x₀ + Δx) = {y1:.2f}", (x1, y1), textcoords="offset points", xytext=(10, 10), color='blue')
ax.annotate(f"Δx = {dx:.2f}", ((x0 + x1)/2, y0), textcoords="offset points", xytext=(0, -20),
            ha='center', color='green', fontsize=10)
ax.annotate(f"Δf = {y1 - y0:.2f}", (x1, (y0 + y1)/2), textcoords="offset points", xytext=(10, 0),
             va='center', color='purple', fontsize=10)

# Mise en forme
ax.set_xlim(0, 2 * np.pi)
ax.set_ylim(-1.5, 1.5)
ax.set_title("Visualisation interactive de la dérivée")
ax.set_xlabel("x")
ax.set_ylabel("f(x)")
ax.grid(True)
ax.legend(loc='upper right')

st.pyplot(fig)
