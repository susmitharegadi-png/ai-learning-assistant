# Entity Relationship (ER) Diagram

## Entities

### Users

| Attribute | Key | Description |
|-----------|-----|-------------|
| email | Primary Key (PK) | Unique identifier for the user |
| name | | User's name |
| password | | Encrypted password |
| role | | Student, Educator, or Admin |
| login_count | | Number of user logins |
| created_at | | Account creation timestamp |

---

### Emotion_Records

| Attribute | Key | Description |
|-----------|-----|-------------|
| record_id | Primary Key (PK) | Unique record ID |
| email | Foreign Key (FK) | References Users.email |
| field | | Academic field |
| input_text | | Student's learning problem |
| predicted_emotion | | Primary detected emotion |
| secondary_emotion | | Secondary detected emotion |
| confidence_score | | Prediction confidence |
| model_used | | BiLSTM or BERT |
| ai_response | | AI-generated learning support |
| response_type | | Gemini AI or Template |
| emotion_scores | | Probability scores |
| timestamp | | Date and time of analysis |
| csv_logged | | Indicates whether stored in CSV |

---

## Relationship

- One **User** can create **many Emotion_Records**.
- Each **Emotion_Record** belongs to **one User**.

**Cardinality:** `1 : Many (1:M)`

---

## ER Diagram

```text
+-----------------------+
|        USERS          |
+-----------------------+
| PK email              |
| name                  |
| password              |
| role                  |
| login_count           |
| created_at            |
+-----------------------+
          |
          | 1
          |
          | creates
          |
          | M
+-------------------------------+
|      EMOTION_RECORDS          |
+-------------------------------+
| PK record_id                  |
| FK email                      |
| field                         |
| input_text                    |
| predicted_emotion             |
| secondary_emotion             |
| confidence_score              |
| model_used                    |
| ai_response                   |
| response_type                 |
| emotion_scores                |
| timestamp                     |
| csv_logged                    |
+-------------------------------+
```

## Normalization

- Separate **Users** and **Emotion_Records** tables reduce data redundancy.
- `email` is the Primary Key in **Users** and the Foreign Key in **Emotion_Records**.
- The design follows basic normalization principles and maintains data integrity.

## Use Cases

- User registration and login
- Emotion detection
- Mixed emotion analysis
- AI-generated learning support
- Session history management
- CSV logging
- Analytics and reporting
