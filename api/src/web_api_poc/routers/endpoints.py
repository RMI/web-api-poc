from fastapi import APIRouter, Depends, HTTPException
from typing import List, Dict, Any
import os
import psycopg2
from psycopg2.extras import RealDictCursor
from dotenv import load_dotenv
from ..models.dvdrental import TableList, Column, Film, FilmList, Rental, RentalList, Actor, ActorList


# Load environment variables
load_dotenv()

# Create router
endpoints = APIRouter(
    prefix="/api",
    tags=["Database Operations"],
    responses={404: {"description": "Not found"}},
)

# Database connection parameters
DB_HOST = os.getenv("DB_HOST", "database")  # Use the service name from docker-compose
DB_PORT = os.getenv("POSTGRES_PORT", "5432")
DB_NAME = os.getenv("POSTGRES_DB", "dvdrental")
DB_USER = os.getenv("POSTGRES_USER", "postgres")
DB_PASS = os.getenv("POSTGRES_PASSWORD", "postgres")

def get_db_connection():
    """Create and return a database connection"""
    try:
        conn = psycopg2.connect(
            host=DB_HOST,
            port=DB_PORT,
            dbname=DB_NAME,
            user=DB_USER,
            password=DB_PASS
        )
        return conn
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Database connection error: {str(e)}")

@endpoints.get("/tables", response_model=TableList)
async def get_tables():
    """Get a list of all tables in the dvdrental database"""
    conn = None
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("""
            SELECT table_name
            FROM information_schema.tables
            WHERE table_schema = 'public'
            ORDER BY table_name;
        """)
        tables = [row[0] for row in cursor.fetchall()]
        return tables
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error retrieving tables: {str(e)}")
    finally:
        if conn:
            conn.close()

@endpoints.get("/tables/{table_name}/schema", response_model=List[Column])
async def get_table_schema(table_name: str):
    """Get schema information for a specific table"""
    conn = None
    try:
        conn = get_db_connection()
        cursor = conn.cursor(cursor_factory=RealDictCursor)
        cursor.execute("""
            SELECT column_name, data_type, is_nullable
            FROM information_schema.columns
            WHERE table_name = %s
            ORDER BY ordinal_position;
        """, (table_name,))
        columns = cursor.fetchall()
        if not columns:
            raise HTTPException(status_code=404, detail=f"Table '{table_name}' not found")
        return columns
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error retrieving schema: {str(e)}")
    finally:
        if conn:
            conn.close()

@endpoints.get("/films/category/{category_name}", response_model=FilmList)
async def get_films_by_category(category_name: str, limit: int = 10, skip: int = 0):
    """Get films by category name"""
    conn = None
    try:
        conn = get_db_connection()
        cursor = conn.cursor(cursor_factory=RealDictCursor)
        cursor.execute("""
            SELECT f.film_id, f.title, f.description, f.release_year, f.length, f.rating
            FROM film f
            JOIN film_category fc ON f.film_id = fc.film_id
            JOIN category c ON fc.category_id = c.category_id
            WHERE c.name = %s
            ORDER BY f.title
            LIMIT %s OFFSET %s;
        """, (category_name, limit, skip))
        films = cursor.fetchall()
        if not films:
            raise HTTPException(status_code=404, detail=f"No films found in category '{category_name}'")
        return films
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error retrieving films: {str(e)}")
    finally:
        if conn:
            conn.close()

@endpoints.get("/films/search", response_model=FilmList)
async def search_films(title: str = None, actor: str = None, limit: int = 10, skip: int = 0):
    """Search films by title and/or actor name"""
    conn = None
    try:
        conn = get_db_connection()
        cursor = conn.cursor(cursor_factory=RealDictCursor)
        
        query = """
            SELECT DISTINCT f.film_id, f.title, f.description, f.release_year, 
                   f.length, f.rating, f.rental_rate
            FROM film f
        """
        params = []
        where_clauses = []
        
        if actor:
            query += """
                JOIN film_actor fa ON f.film_id = fa.film_id
                JOIN actor a ON fa.actor_id = a.actor_id
            """
            where_clauses.append("(a.first_name ILIKE %s OR a.last_name ILIKE %s)")
            params.extend([f"%{actor}%", f"%{actor}%"])
        
        if title:
            where_clauses.append("f.title ILIKE %s")
            params.append(f"%{title}%")
        
        if where_clauses:
            query += " WHERE " + " AND ".join(where_clauses)
        
        query += """
            ORDER BY f.title
            LIMIT %s OFFSET %s;
        """
        params.extend([limit, skip])
        
        cursor.execute(query, params)
        films = cursor.fetchall()
        if not films:
            raise HTTPException(status_code=404, detail="No films found matching the criteria")
        return films
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error searching films: {str(e)}")
    finally:
        if conn:
            conn.close()
