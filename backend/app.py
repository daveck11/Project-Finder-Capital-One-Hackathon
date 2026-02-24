import sqlite3
from flask_cors import CORS
from flask import Flask, jsonify, request
import pickle
import pandas as pd

app = Flask(__name__)
CORS(app)



 #product
with open(r"postList.pkl","rb") as f:
    prod = pickle.load(f)
    df =pd.DataFrame(prod)

with open(r"similarity.pkl","rb") as f:
    similarity_mat= pickle.load(f)



def post_recommend(course):
    postIndex  = df[df['course']=='Biology'].index[0]
    distances_ = similarity_mat[postIndex]
    post_list = sorted(list(enumerate(distances_)),reverse=True,key=lambda x:x[1])[1:4]
    recommended_df = df.iloc[[i[0] for i in post_list]]
    return recommended_df





def get_db_connection():
    try:
        conn = sqlite3.connect(r'Sqlite3.db')
        conn.row_factory = sqlite3.Row
        return conn
    except sqlite3.Error as error:
        print("Database connection error:", error)
        return None


@app.route('/getPosts', methods=['GET'])
def getPosts():
    conn = get_db_connection()
    if conn is None:
        return jsonify({"error": "Database connection failed"}), 500

    try:
        cursor = conn.cursor()
        posts = [dict(row) for row in cursor.execute("SELECT posts.*, s.email FROM posts JOIN students s ON posts.student = s.student_ID")]
        return jsonify(posts)

    except sqlite3.Error as error:
        print("Database error:", error)
        return jsonify({"error": "Database query failed"}), 500

    finally:
        conn.close()



@app.route('/getCourse', methods=['GET'])
def getCourse():
    conn = get_db_connection()
    if conn is None:
        return jsonify({"error": "Database connection failed"}), 500

    try:
        cursor = conn.cursor()
        posts = [dict(row) for row in cursor.execute("SELECT DISTINCT course FROM posts")]
        return jsonify(posts)

    except sqlite3.Error as error:
        print("Database error:", error)
        return jsonify({"error": "Database query failed"}), 500

    finally:
        conn.close()


@app.route('/getSkills', methods=['GET'])
def getSkills():
    conn = get_db_connection()
    if conn is None:
        return jsonify({"error": "Database connection failed"}), 500

    try:
        cursor = conn.cursor()
        posts = [dict(row) for row in cursor.execute("SELECT DISTINCT skills FROM posts")]
        return jsonify(posts)

    except sqlite3.Error as error:
        print("Database error:", error)
        return jsonify({"error": "Database query failed"}), 500

    finally:
        conn.close()


@app.route('/getRecommendations', methods=['GET'])
def getRecommendations():
    course = request.args.get('course', default="Biology")
    recommendations = post_recommend(course)

    if recommendations is None:
        return jsonify({"error": "Course not found"}), 404


    return jsonify(recommendations.to_dict(orient="records"))

if __name__ == '__main__':
    app.run(debug=True, port=5000)
