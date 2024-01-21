# util.py

from datetime import datetime, timedelta
from sqlalchemy import func
from models import Attendance

def calculate_attendance_percentage(start_date, end_date):
    total_days = (end_date - start_date).days + 1
    present_days = Attendance.query.filter(Attendance.marked_time >= start_date, Attendance.marked_time <= end_date).count()
    attendance_percentage = (present_days / total_days) * 100
    return attendance_percentage

def analyze_trends(start_date, end_date):
    trends = []
    current_date = start_date
    while current_date <= end_date:
        attendance = Attendance.query.filter(func.date(Attendance.marked_time) == current_date).count()
        trends.append({'date': current_date.strftime('%Y-%m-%d'), 'attendance': attendance})
        current_date += timedelta(days=1)
    return trends
