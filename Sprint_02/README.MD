# 📘 Indexing in Databases: B-Tree, Hash, and Bitmap

This README explains three common indexing techniques used in databases:

- 🔵 B-Tree Indexing
- 🟢 Hash Indexing
- 🟡 Bitmap Indexing

---

## 🔵 B-Tree Indexing

### 📌 What is it?
B-Tree (Balanced Tree) is a tree data structure where data is stored in a sorted manner across multiple levels. Each node contains multiple keys and has multiple children, making it efficient for searching, inserting, and deleting.

### ⚙️ How it works:
- Data is kept in **sorted order**.
- Supports **logarithmic time** operations: search, insert, delete.
- Great for **range and sorted** queries.

### ✅ Use Cases:
- General-purpose indexing in relational databases.
- Ideal for queries like:
  - `WHERE age BETWEEN 20 AND 30`
  - `ORDER BY name`
  - `WHERE id = 101`

---

## 🟢 Hash Indexing

### 📌 What is it?
Hash Indexing uses a **hash function** to convert a key into a hash value, which maps directly to a bucket that stores the data.

### ⚙️ How it works:
- A hash function maps the key (e.g., `email`) to a bucket.
- Excellent for **exact match** lookups.
- Does **not** maintain order of keys.

### 🚨 Collisions:
A **collision** occurs when different keys produce the same hash value. These are handled using methods like **chaining** or **open addressing**.

### ✅ Use Cases:
- Ideal for equality-only lookups:
  - `WHERE email = 'abc@example.com'`
- Used in in-memory databases (e.g., Redis) or for high-speed key-value access.

---

## 🟡 Bitmap Indexing

### 📌 What is it?
Bitmap Indexing uses **bit arrays** (bitmaps) to represent data. Each distinct value in a column has a corresponding bitmap where each bit indicates if the row has that value.

### ⚙️ How it works:
- One bitmap per distinct column value.
- Bit operations (AND, OR, NOT) are extremely fast.
- Most efficient with **low-cardinality** columns.

### ✅ Use Cases:
- OLAP systems, analytics, data warehouses.
- Filtering on boolean or categorical fields like:
  - `gender`, `status`, `is_active`, `region`, etc.

---

## 🆚 Comparison Table

| Feature               | B-Tree Index        | Hash Index          | Bitmap Index              |
|-----------------------|---------------------|----------------------|--------------------------|
| Best for              | Range + Equality     | Exact Equality        | Low-cardinality filters|
| Ordered data support  | ✅ Yes               | ❌ No                | ❌ No                  |
| Range queries         | ✅ Supported         | ❌ Not supported     | ❌ Not efficient       |
| Sorting               | ✅ Yes               | ❌ No                | ❌ No                  |
| Space efficiency      | ⚠️ Moderate          | ⚠️ Moderate           | ✅ Very efficient     |
| Performance (equality)| ⚡️ Fast              | ⚡️⚡️ Very Fast         | ⚡️⚡️ Very Fast      |
| Use case type         | OLTP (transactions) | OLTP, in-memory      | OLAP (analytics)         | 

---

## 📦 Summary

- Use **B-Tree** for general-purpose indexing, especially when range or sorted queries are required.
- Use **Hash** indexing for **pure equality** lookups with no need for sorting or range queries.
- Use **Bitmap** indexing when dealing with **low-cardinality** columns in analytics-heavy environments.

---

