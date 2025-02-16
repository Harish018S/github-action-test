from flask import Flask, request, jsonify
import sqlite3
import duckdb
import re
import openai
import os

app = Flask(__name__)

def extract_sql_from_task(task_description):
    """Use an LLM to extract a SQL query from the task description."""
    response = openai.ChatCompletion.create(
        model="gpt-4-turbo",
        messages=[
            {"role": "system", "content": "Extract only the SQL query from the given instruction."},
            {"role": "user", "content": task_description}
        ]
    )
    return response["choices"][0]["message"]["content"].strip()

def is_safe_query(query):
    """Ensure that the query does not modify or delete data."""
    unsafe_patterns = [r'\bDELETE\b', r'\bUPDATE\b', r'\bDROP\b', r'\bINSERT\b', r'\bALTER\b']
    for pattern in unsafe_patterns:
        if re.search(pattern, query, re.IGNORECASE):
            return False
    return True

def execute_sql(query, db_path, engine):
    """Execute the SQL query on the specified database engine (SQLite or DuckDB)."""
    if engine == "sqlite":
        conn = sqlite3.connect(db_path)
    else:
        conn = duckdb.connect(db_path)
    
    try:
        cursor = conn.cursor()
        cursor.execute(query)
        result = cursor.fetchall()
        columns = [desc[0] for desc in cursor.description]
        conn.close()
        return {"columns": columns, "data": result}
    except Exception as e:
        return str(e)

@app.route('/run', methods=['POST'])
def run_task():
    task_description = request.args.get('task', '')
    if not task_description:
        return jsonify({"error": "Task description missing"}), 400

    try:
        query = extract_sql_from_task(task_description)
        if not is_safe_query(query):
            return jsonify({"error": "Unsafe SQL query detected"}), 400
        
        # Identify database
        db_path = None
        engine = None
        if "sqlite" in task_description.lower():
            db_path = "/data/ticket-sales.db"  # Example SQLite DB
            engine = "sqlite"
        elif "duckdb" in task_description.lower():
            db_path = "/data/analytics.duckdb"  # Example DuckDB
            engine = "duckdb"
        
        if not db_path or not os.path.exists(db_path):
            return jsonify({"error": "Database file not found"}), 404
        
        result = execute_sql(query, db_path, engine)
        return jsonify(result), 200
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
