
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from math import gcd

from database import (
    create_table,
    save_kpk,
    get_all_history,
    get_history_by_id,
    delete_history
)

app = FastAPI(
    title="KPK Calculator API",
    description="REST API untuk menghitung KPK menggunakan Python dan SQLite",
    version="1.0.0"
)


# Membuat database ketika aplikasi dimulai
@app.on_event("startup")
def startup():
    create_table()


# Model input
class KPKRequest(BaseModel):
    bilangan1: int = Field(gt=0)
    bilangan2: int = Field(gt=0)


# Fungsi menghitung KPK
def hitung_kpk(a, b):
    return abs(a * b) // gcd(a, b)


# 1. Halaman utama
@app.get("/")
def home():
    return {
        "message": "Selamat datang di KPK Calculator API",
        "documentation": "/docs"
    }


# 2. Menghitung dan menyimpan KPK
@app.post("/kpk")
def calculate_kpk(data: KPKRequest):

    a = data.bilangan1
    b = data.bilangan2

    hasil = hitung_kpk(a, b)

    record_id = save_kpk(a, b, hasil)

    return {
        "status": "success",
        "id": record_id,
        "bilangan1": a,
        "bilangan2": b,
        "hasil_kpk": hasil
    }


# 3. Menampilkan semua riwayat
@app.get("/riwayat")
def history():

    data = get_all_history()

    return {
        "total": len(data),
        "data": data
    }


# 4. Menampilkan riwayat berdasarkan ID
@app.get("/riwayat/{record_id}")
def history_detail(record_id: int):

    data = get_history_by_id(record_id)

    if data is None:
        raise HTTPException(
            status_code=404,
            detail="Riwayat tidak ditemukan"
        )

    return data


# 5. Menghapus riwayat
@app.delete("/riwayat/{record_id}")
def remove_history(record_id: int):

    deleted = delete_history(record_id)

    if not deleted:
        raise HTTPException(
            status_code=404,
            detail="Riwayat tidak ditemukan"
        )

    return {
        "status": "success",
        "message": "Riwayat berhasil dihapus"
    }
