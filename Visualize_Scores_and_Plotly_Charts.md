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

# Emotional Journey Line Chart

## Overview

The **Emotional Journey** chart visualizes how a student's confidence score changes over time during different learning sessions. Each data point represents one emotion analysis session, while different colors indicate different detected emotions.

The chart is created using **Plotly Express** and displayed in the second column of the **Emotions** tab in the Streamlit dashboard.

---

## Features

- Interactive line chart
- Displays confidence scores over time
- Color-coded by detected emotion
- Markers for every session
- Responsive Streamlit layout
- Hover tooltips for detailed information

---

## Implementation

```python
with col2:
    df_copy = df.copy()

    df_copy["time"] = df_copy["timestamp"].dt.strftime("%H:%M:%S")

    fig2 = px.line(
        df_copy,
        x="time",
        y="confidence",
        color="emotion",
        title="Emotional Journey",
        markers=True
    )

    st.plotly_chart(fig2, use_container_width=True)
```

---

## Code Explanation

### Create a Copy of the DataFrame

```python
df_copy = df.copy()
```

A copy is created to avoid modifying the original dataset.

---

### Format the Timestamp

```python
df_copy["time"] = df_copy["timestamp"].dt.strftime("%H:%M:%S")
```

Converts the timestamp into a readable time format (Hours:Minutes:Seconds).

Example:

| Timestamp | Time |
|-----------|------|
| 2025-08-05 14:30:45 | 14:30:45 |

---

### Create the Line Chart

```python
fig2 = px.line(
    df_copy,
    x="time",
    y="confidence",
    color="emotion",
    title="Emotional Journey",
    markers=True
)
```

Parameters:

- **x** → Session time
- **y** → Confidence score
- **color** → Emotion category
- **title** → Chart title
- **markers=True** → Displays markers for each data point

---

### Display in Streamlit

```python
st.plotly_chart(fig2, use_container_width=True)
```

Displays the interactive Plotly chart with automatic width adjustment.

---

## Output

The chart shows:

- Confidence score across sessions
- Emotion detected at each session
- Different colored lines for different emotions
- Interactive hover information

---

## Benefits

- Tracks emotional changes over time.
- Helps identify learning patterns.
- Shows confidence trends during multiple sessions.
- Supports educators in monitoring student progress.
- Provides an intuitive visualization of the learner's emotional journey.

---

# Emotional Journey Line Chart

## Overview

The **Emotional Journey** chart visualizes how a student's confidence score changes over time during different learning sessions. Each data point represents one emotion analysis session, while different colors indicate different detected emotions.

The chart is created using **Plotly Express** and displayed in the second column of the **Emotions** tab in the Streamlit dashboard.

---

## Features

- Interactive line chart
- Displays confidence scores over time
- Color-coded by detected emotion
- Markers for every session
- Responsive Streamlit layout
- Hover tooltips for detailed information

---

## Implementation

```python
with col2:
    df_copy = df.copy()

    df_copy["time"] = df_copy["timestamp"].dt.strftime("%H:%M:%S")

    fig2 = px.line(
        df_copy,
        x="time",
        y="confidence",
        color="emotion",
        title="Emotional Journey",
        markers=True
    )

    st.plotly_chart(fig2, use_container_width=True)
```

---

## Code Explanation

### Create a Copy of the DataFrame

```python
df_copy = df.copy()
```

A copy is created to avoid modifying the original dataset.

---

### Format the Timestamp

```python
df_copy["time"] = df_copy["timestamp"].dt.strftime("%H:%M:%S")
```

Converts the timestamp into a readable time format (Hours:Minutes:Seconds).

Example:

| Timestamp | Time |
|-----------|------|
| 2025-08-05 14:30:45 | 14:30:45 |

---

### Create the Line Chart

```python
fig2 = px.line(
    df_copy,
    x="time",
    y="confidence",
    color="emotion",
    title="Emotional Journey",
    markers=True
)
```

Parameters:

- **x** → Session time
- **y** → Confidence score
- **color** → Emotion category
- **title** → Chart title
- **markers=True** → Displays markers for each data point

---

### Display in Streamlit

```python
st.plotly_chart(fig2, use_container_width=True)
```

Displays the interactive Plotly chart with automatic width adjustment.

---

## Output

The chart shows:

- Confidence score across sessions
- Emotion detected at each session
- Different colored lines for different emotions
- Interactive hover information

---

## Benefits

- Tracks emotional changes over time.
- Helps identify learning patterns.
- Shows confidence trends during multiple sessions.
- Supports educators in monitoring student progress.
- Provides an intuitive visualization of the learner's emotional journey.

---

---

#  Emotions by Study Field Bar Chart

## Description

This visualization displays the distribution of detected emotions across different academic fields. When predictions from both **BiLSTM** and **BERT** models are available, the chart automatically separates the results by model using faceting, making it easy to compare the performance of both models.

---

## Features

- Interactive Plotly bar chart
- Groups emotions by study field
- Color-coded bars for different emotions
- Supports comparison between BiLSTM and BERT models
- Responsive Streamlit layout
- Interactive hover tooltips

---

## Implementation

```python
with tab2:
    if "model" in df.columns:
        field_emotion = df.groupby(
            ["field", "emotion", "model"]
        ).size().reset_index(name="count")

        fig3 = px.bar(
            field_emotion,
            x="field",
            y="count",
            color="emotion",
            facet_col="model",
            title="Emotions by Study Field & Model"
        )

    else:
        field_emotion = df.groupby(
            ["field", "emotion"]
        ).size().reset_index(name="count")

        fig3 = px.bar(
            field_emotion,
            x="field",
            y="count",
            color="emotion",
            title="Emotions by Study Field"
        )

    st.plotly_chart(fig3, use_container_width=True)
```

---

## Code Explanation

### Check for Model Column

```python
if "model" in df.columns:
```

Checks whether the dataset contains predictions from multiple models.

---

### Group the Data

```python
field_emotion = df.groupby(
    ["field", "emotion", "model"]
).size().reset_index(name="count")
```

Groups the data by:

- Study field
- Detected emotion
- Prediction model

and calculates the number of records in each group.

---

### Create the Bar Chart

```python
fig3 = px.bar(
    field_emotion,
    x="field",
    y="count",
    color="emotion",
    facet_col="model",
    title="Emotions by Study Field & Model"
)
```

- **x** → Academic field
- **y** → Number of emotion records
- **color** → Emotion category
- **facet_col** → Displays separate charts for each model

---

### Display in Streamlit

```python
st.plotly_chart(fig3, use_container_width=True)
```

Displays the interactive chart with responsive sizing.

---

## Benefits

- Compares emotion distribution across study fields.
- Supports comparison between BiLSTM and BERT predictions.
- Helps identify emotional patterns within different academic subjects.
- Provides an interactive and user-friendly analytics dashboard.
-
# Overall Conclusion

The Plotly visualizations significantly enhance the analytics capabilities of the Emotion Detection & Learning Support Engine by transforming emotion prediction data into meaningful and interactive insights. The **Emotion Distribution Pie Chart** provides a clear overview of the frequency of each detected emotion, helping users quickly understand overall emotional patterns. The **Emotional Journey Line Chart** illustrates how learners' confidence scores and emotions evolve over time, enabling effective progress tracking across multiple sessions. Additionally, the **Emotions by Study Field Bar Chart** compares emotion distributions across different academic fields and, when available, across both BiLSTM and BERT models, offering valuable insights into model performance and subject-specific emotional trends.

Together, these interactive visualizations create an intuitive analytics dashboard that supports students, educators, and researchers in monitoring learning behavior, identifying emotional challenges, comparing model outputs, and making data-driven educational decisions. The integration of Plotly with Streamlit ensures responsive, user-friendly, and real-time visual analytics, making the platform more informative, engaging, and effective.
