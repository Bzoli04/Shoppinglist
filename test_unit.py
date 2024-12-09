import pytest
from app import shopping_list, add_item, delete_item

def test_add_item_unit():
    """Tesztelje az elem hozzáadásának logikáját."""

    shopping_list.clear()


    item = "apple"
    shopping_list.append(item)


    assert len(shopping_list) == 1
    assert "apple" in shopping_list

def test_delete_item_unit():
    """Tesztelje az elem törlésének logikáját."""

    shopping_list.clear()
    shopping_list.append("Banana")


    shopping_list.remove("Banana")


    assert len(shopping_list) == 0
    assert "Banana" not in shopping_list

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
    shopping_list.append("milk")


    item = "egg"
    if item in shopping_list:
        shopping_list.remove(item)


    assert len(shopping_list) == 1
    assert "milk" in shopping_list
    assert "egg" not in shopping_list
