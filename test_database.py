#!/usr/bin/env python3
"""
Test script for SQLite remarks database functionality
Run this to verify the database operations work correctly
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Import the database functions
from streamlit_dashboard1 import (
    init_database, load_remarks, save_remark,
    delete_remark, clear_all_remarks, DB_FILE
)

def test_database():
    """Test all database operations"""
    print("Testing SQLite Remarks Database...")
    print(f"Database file: {DB_FILE}")

    # Initialize database
    print("Initializing database...")
    init_database()

    # Test 1: Load empty database
    print("Test 1: Loading remarks from empty database...")
    data = load_remarks()
    print(f"   Loaded data: {data}")
    assert data == {"remarks": {}}, "Empty database should return empty dict"

    # Test 2: Save a remark
    print("Test 2: Saving a remark...")
    cell_key = "FOOD SALES|Jul-25"
    remark_text = "Test remark for July 2025"
    result = save_remark(cell_key, remark_text)
    print(f"   Save result: {result}")
    assert result == True, "Save should return True"

    # Test 3: Load and verify saved remark
    print("Test 3: Loading remarks after save...")
    data = load_remarks()
    print(f"   Loaded data: {data}")
    assert cell_key in data.get("remarks", {}), "Cell key should exist in loaded data"
    assert data["remarks"][cell_key] == remark_text, "Remark text should match"

    # Test 4: Update existing remark
    print("Test 4: Updating existing remark...")
    new_remark = "Updated test remark"
    result = save_remark(cell_key, new_remark)
    assert result == True, "Update should return True"

    data = load_remarks()
    assert data["remarks"][cell_key] == new_remark, "Remark should be updated"

    # Test 5: Save another remark
    print("Test 5: Saving second remark...")
    cell_key2 = "SERVICE CHARGE|Aug-25"
    remark_text2 = "Another test remark"
    save_remark(cell_key2, remark_text2)

    data = load_remarks()
    assert len(data["remarks"]) == 2, "Should have 2 remarks"
    assert cell_key2 in data["remarks"], "Second cell key should exist"

    # Test 6: Delete a remark
    print("Test 6: Deleting a remark...")
    result = delete_remark(cell_key)
    assert result == True, "Delete should return True"

    data = load_remarks()
    assert cell_key not in data["remarks"], "Deleted remark should not exist"
    assert cell_key2 in data["remarks"], "Other remark should still exist"

    # Test 7: Clear all remarks
    print("Test 7: Clearing all remarks...")
    result = clear_all_remarks()
    assert result == True, "Clear all should return True"

    data = load_remarks()
    assert data == {"remarks": {}}, "Database should be empty after clear"

    print("All tests passed! Database functionality is working correctly.")
    print("SQLite remarks system is ready for deployment!")

if __name__ == "__main__":
    test_database()
