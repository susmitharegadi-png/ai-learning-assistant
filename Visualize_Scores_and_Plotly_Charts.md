# Visualize Scores and Plotly Charts with Caching

## Overview

This module visualizes the distribution of detected emotions using an interactive Plotly pie chart. It helps users and educators quickly understand how frequently each emotion appears across all analyzed sessions.

The visualization is displayed in the **Emotions** tab of the Streamlit application and automatically adjusts to the available screen width.

---

## Features

- Interactive Plotly pie chart
- Displays emotion distribution
- Hover tooltips for each emotion
- Responsive layout using Streamlit columns
- Suitable for analytics dashboard

---

## Implementation

```python
with tab1:
    col1, col2 = st.columns(2)

    with col1:
        emotion_counts = df["emotion"].value_counts()

        fig1 = px.pie(
            values=emotion_counts.values,
            names=emotion_counts.index,
            title="Emotion Distribution"
        )

        st.plotly_chart(fig1, use_container_width=True)
```

---

## Code Explanation

### `st.columns(2)`

Creates two columns inside the **Emotions** tab.

```python
col1, col2 = st.columns(2)
```

---

### `emotion_counts`

Counts how many times each emotion appears in the dataset.

```python
emotion_counts = df["emotion"].value_counts()
```

Example:

| Emotion | Count |
|----------|------:|
| Confused | 18 |
| Curious | 12 |
| Frustrated | 9 |
| Confident | 6 |
| Bored | 5 |

---

### `px.pie()`

Creates an interactive pie chart.

```python
fig1 = px.pie(
    values=emotion_counts.values,
    names=emotion_counts.index,
    title="Emotion Distribution"
)
```

- **values** → Number of occurrences of each emotion.
- **names** → Emotion labels.
- **title** → Chart title.

---

### `st.plotly_chart()`

Displays the Plotly chart in the Streamlit application.

```python
st.plotly_chart(fig1, use_container_width=True)
```

The `use_container_width=True` option makes the chart automatically fit the available space.

---

## Output

The chart displays the percentage distribution of emotions such as:

- Confused
- Curious
- Frustrated
- Confident
- Bored

Users can hover over each slice to view detailed values and percentages.

---

## Benefits

- Easy visualization of emotion trends.
- Helps educators identify common learner emotions.
- Improves dashboard usability through interactive charts.
- Supports real-time analytics and reporting.

---

## Conclusion

The Emotion Distribution Pie Chart provides an intuitive overview of detected emotions across all sessions. Using Plotly Express and Streamlit, the visualization is interactive, responsive, and easy to interpret, making it a valuable component of the analytics dashboard.
