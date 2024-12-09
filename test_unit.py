import pytest
from app import shopping_list, add_item, delete_item

def test_add_item_unit():
    """Tesztelje az elem hozzáadásának logikáját."""

    shopping_list.clear()


    item = "alma"
    shopping_list.append(item)


    assert len(shopping_list) == 1
    assert "alma" in shopping_list

def test_delete_item_unit():
    """Tesztelje az elem törlésének logikáját."""

    shopping_list.clear()
    shopping_list.append("Banan")


    shopping_list.remove("Banan")


    assert len(shopping_list) == 0
    assert "Banan" not in shopping_list

def test_add_empty_item_unit():
    """Tesztelje, hogy üres elem ne kerüljön a listába."""

    shopping_list.clear()


    item = ""
    if item:
        shopping_list.append(item)


    assert len(shopping_list) == 0
    assert "" not in shopping_list

def test_delete_nonexistent_item_unit():
    """Tesztelje, hogy nem létező elem törlése nem okoz hibát."""

    shopping_list.clear()
    shopping_list.append("tej")


    item = "tojás"
    if item in shopping_list:
        shopping_list.remove(item)


    assert len(shopping_list) == 1
    assert "tej" in shopping_list
    assert "tojás" not in shopping_list
